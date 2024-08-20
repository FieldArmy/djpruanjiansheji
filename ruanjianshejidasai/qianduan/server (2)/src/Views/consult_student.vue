<template>
  <div>
    <div id="table_box">
      <el-tabs v-model="activeName" style="background-color: white" type="card" >
        <el-tab-pane label="待解答" class="bg_color" name="first">
          <el-table :data="info" stripe style="width: 100%">
            <el-table-column prop="account" align="center" label="考生账号" width="300"></el-table-column>
            <el-table-column prop="question" align="center" label="考生咨询问题"></el-table-column>
            <el-table-column prop="time" align="center" label="咨询时间"></el-table-column>
            <el-table-column label="咨询师操作" width="200">
              <template slot-scope="scope">
                <el-button type="primary" style="margin-bottom: 5px" @click="confirmBox(scope.row.account)">详细信息</el-button>
                <el-button type="success" style="margin-left: 0;margin-bottom: 5px;" @click="returnMessage(scope.row.code)">
                  点击反馈
                </el-button>
              </template>
            </el-table-column>
          </el-table>

        </el-tab-pane>
        <el-tab-pane label="已解答" name="second">
          <el-table :data="info2" stripe style="width: 100%">
            <el-table-column prop="account" align="center" label="账号" width="300"></el-table-column>
            <el-table-column prop="question" align="center" label="考生咨询问题"></el-table-column>
            <el-table-column prop="time" align="center" label="咨询时间"></el-table-column>
            <el-table-column prop="advice" align="center" label="我的回复"></el-table-column>
          </el-table>
        </el-tab-pane>
      </el-tabs>

      <el-dialog title="给学生的建议" :visible.sync="dialogVisible" width="28%">
        <el-input
            type="textarea"
            :rows="8"
            placeholder="请输入内容"
            v-model="text"
            maxlength="300"
            style="width: 99%"
            class="form"
            show-word-limit
        >
        </el-input>
        <div id="button-box">
          <el-button type="primary" @click="getwt()" >提交反馈</el-button>
          <el-button @click="pass_info" >取消反馈</el-button>
        </div>

      </el-dialog>
      <!-- 分页 -->
      <!--            <el-pagination-->
      <!--                :page-size.sync='pageSize'-->
      <!--                :current-page.sync='curPage'-->
      <!--                @size-change="handleSizeChange"-->
      <!--                @current-change="handleCurrentChange"-->
      <!--                layout="prev, pager, next"-->
      <!--                :total="LengthText(student)">-->
      <!--            </el-pagination>-->
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: "consult_student",
  data() {
    return {
      id2:'',
      activeName: 'first',
      text: '',
      student_name: '',
      id: '',
      info: [],
      info2:[],
      // 默认初始页数
      curPage: 1,
      // 显示个数
      pageSize: 10,
      student_show: [],
      dialogVisible: false,
      username:""
    }
  },
  methods: {
    // 调整显示个数
    handleSizeChange(val) {
      this.pageSize = val;
    },
    // 调整页数
    handleCurrentChange(val) {
      this.curPage = val;
    },
    // 调整总条目数
    LengthText(val) {
      let x = val.length;
      if (x != null) {
        return x;
      } else
        return 0;
    },

    // 详细信息
    confirmBox(id) {
      axios({
        method:'GET',
        url:'api/students/grades',
        params:{
          action:'get_stu',
          account:id
        }
      }).then((resp)=>{
        let student_message = [
          "选科：" + resp.data.subject,
          "高考分数：" +resp.data.stu_grd,
          "高考位次：" + resp.data.ranking,
          // "全省考生的百分比：" + parseInt(resp.data.gk_percentage)*100<1?1:10
        ];
        const NewData = [];

        const t = this.$createElement;
        for (const i in student_message) {
          NewData.push(t("p", null, student_message[i]))
        }
        this.$confirm(null, {
          title: '考生详细信息',
          message: t("div", null, NewData),
          confirmButtonText: '确定',
          cancelButtonText: '取消',
        })
      })

    },

    // 返回消息
    returnMessage(id) {
      // this.id = val.id;
      // this.student_name = val.main_square;
      this.dialogVisible = true;
      this.id2=id
    },
    //获取学生的问题
    getinfo() {
      //接受咨询师账号名
      axios({
        method:'POST',
        url:'api/teachers/getquestion',
        data:{
          action:'get_question',
          account:this.$cookies.get('teaName'),
          set_tch:'teacher'
        }
      }).then((resp)=>{
        // console.log(resp.data.question02)
        this.info=resp.data.question02
      })
    },
    //反馈给学生建议
    getwt() {
      axios({
        method:'POST',
        url:'api/teachers/setquestion',
        data:{
          action:'set_question',
          account:this.$cookies.get('teaName'),
          set_tch:'teacher',
          code:this.id2,
          advice:this.text
        }
      }).then((resp)=>{
        console.log(resp.data)
            if (resp.data.ret ===0) {
              this.$message.success("反馈成功")
              this.getinfo()
              this.end_info()
              this.dialogVisible = false
              this.text = ''
            }
      })
    },
    end_info(){
      axios({
        method:'POST',
        url:'api/teachers/getquestion',
        data:{
          action:'get_question',
          account:this.$cookies.get('teaName'),
          set_tch:'teacher'
        }
      }).then((resp)=>{
        // console.log(resp.data.question02)
        this.info2=resp.data.question01
      })
    },
    pass_info() {
      this.dialogVisible = false
      this.text = ""
    },
    // 删除用户
    delStudent() {
      // 定义位置
      let address;

      // 根据当前行查找对应id
      for (let i = 0; i < this.student.length; i++) {
        if (this.student_show == this.student[i]) {
          address = i;
          // console.log(this.student_show.id);
          // console.log(address);
          break;
        }
      }

      if (address >= 0) {
        this.student.splice(address, 1);
        this.$message({
          type: 'success',
          message: '删除成功!'
        });
      } else {
        this.$message({
          type: 'warning',
          message: '已删除或用户不存在'
        });
      }
    },

  },
  created() {
    this.getinfo()
    this.end_info()
  }
}
</script>

<style scoped>
/*.el-message-box .el-message-box__title {*/
/*  font-weight: 700;*/
/*  text-align: center;*/
/*}*/

/*.el-message-box .el-message-box__message p {*/
/*  padding-left: 20px !important;*/
/*  line-height: 40px !important;*/
/*}*/

#table_box {
  margin: 0 auto;
  width: 100%;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
}
#button-box{
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 15px;
}
/*.bg_color{*/
/*  background-color: #00ff51;*/
/*}*/
</style>
