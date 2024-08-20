<template>
  <div>
    <el-card class="box-card" style="margin-top: 10px;width: 2500px">
      <div slot="header" class="clearfix" style="height: 30px">
        <span class="size_t1">智能填报 </span>
        <el-button type="text" @click="dialogVisible = true"> 【注意事项】</el-button>
      </div>
      <el-dialog title="注意事项" :visible.sync="dialogVisible" width="28%">
        <h3 style="margin-top: -20px">本系统根据2022和2023两年录取数据，进行推荐志愿和预测录取风险.</h3>
        <h3>本系统推荐的院校名单，仅供参考，报考风险由考生本身承担！</h3>
        <h3>以分数优先的原则为用户推荐学校！</h3>
      </el-dialog>

      <!-- 城市级联选择器-->
      <div id="box">
        <!--填报批次-->
        <el-button type="text" class="box-tit" ><h3>填报批次</h3></el-button>
        <el-radio-group v-model="button_checked" size="small" >
          <el-radio-button style="margin-left: 11px" v-model="button_checked" label="ben">本科</el-radio-button>
          <el-radio-button v-model="button_checked" label="zhuan">专科</el-radio-button>
        </el-radio-group>

        <!-- 城市 -->
        <br>
        <el-button type="text" class="box-tit"><h3>就读地区</h3></el-button>
        <div style="margin-top: -5px">
          <el-radio-group v-model="CX.list1" size="small">
            <el-radio-button label="所有地区"></el-radio-button>
            <el-radio-button label="山东"></el-radio-button>
            <el-radio-button label="北京"></el-radio-button>
            <el-radio-button label="天津"></el-radio-button>
            <el-radio-button label="河北"></el-radio-button>
            <el-radio-button label="山西"></el-radio-button>
            <el-radio-button label="辽宁"></el-radio-button>
            <el-radio-button label="吉林"></el-radio-button>
            <el-radio-button label="上海"></el-radio-button>
            <el-radio-button label="江苏"></el-radio-button>
            <el-radio-button label="浙江"></el-radio-button>
            <el-radio-button label="安徽"></el-radio-button>
            <el-radio-button label="福建"></el-radio-button>
            <el-radio-button label="江西"></el-radio-button>
            <el-radio-button label="河南"></el-radio-button>
            <el-radio-button label="湖南"></el-radio-button>
            <el-radio-button label="湖北"></el-radio-button>

            <div style="margin-top: 2px">

              <el-radio-button label="广东"></el-radio-button>
              <el-radio-button label="广西"></el-radio-button>
              <el-radio-button label="黑龙江"></el-radio-button>
              <el-radio-button label="内蒙古"></el-radio-button>
              <el-radio-button label="海南"></el-radio-button>
              <el-radio-button label="重庆"></el-radio-button>
              <el-radio-button label="四川"></el-radio-button>
              <el-radio-button label="贵州"></el-radio-button>
              <el-radio-button label="云南"></el-radio-button>
              <el-radio-button label="西藏"></el-radio-button>
              <el-radio-button label="陕西"></el-radio-button>
              <el-radio-button label="甘肃"></el-radio-button>
              <el-radio-button label="青海"></el-radio-button>
              <el-radio-button label="宁夏"></el-radio-button>
              <el-radio-button label="新疆"></el-radio-button>
            </div>
          </el-radio-group>
        </div>
<!--         本科专业-->
        <el-input v-model="input" placeholder="专业" style="width: 200px; margin-top: 10px" :disabled="button_checked2===false" ></el-input>
        <el-switch
            v-model="button_checked2"
            active-color="#13ce66"
            inactive-color="#ff4949">
        </el-switch>
        <!-- 专业类别-->
        <br/>
        <el-button type="text" class="box-tit"><h3>院校类型</h3></el-button>
        <div style="margin-top: 0px">
          <el-radio-group v-model="CX.list3" size="small">
            <el-radio-button label="综合类"></el-radio-button>
            <el-radio-button label="理工类"></el-radio-button>
            <el-radio-button label="医药类"></el-radio-button>
            <el-radio-button label="农林类"></el-radio-button>
            <el-radio-button label="师范类"></el-radio-button>
            <el-radio-button label="语言类"></el-radio-button>
            <el-radio-button label="财经类"></el-radio-button>
            <el-radio-button label="政法类"></el-radio-button>
            <el-radio-button label="体育类"></el-radio-button>
            <el-radio-button label="艺术类"></el-radio-button>
            <el-radio-button label="民族类"></el-radio-button>
            <el-radio-button label="军事类"></el-radio-button>
          </el-radio-group>
        </div>

        <el-button type="text" class="box-tit"><h3>办学类型</h3></el-button>
        <div style="margin-top: 0;position: relative">
        <el-radio-group v-model="CX.list4" size="small">
          <el-radio-button label="公办"></el-radio-button>
          <el-radio-button label="民办"></el-radio-button>
          <el-radio-button :label="985"></el-radio-button>
          <el-radio-button :label="211"></el-radio-button>
        </el-radio-group>
        </div>


        <el-button type="primary" icon="el-icon-search" @click="get1()"
                   style="margin-left: 20px; padding: 10px" class="tijiao">提交
        </el-button>
      </div>

    </el-card>
    <div>
      <!--显示的表格-->
      <el-card class="box-card2" id="id1" style="overflow:visible;">
        <el-table :data="info.slice((currentPage-1)*pageSize,currentPage*pageSize)" style="overflow-x: visible; " stripe>
          <el-table-column label="学校详细信息" class="Fill_size" align="center">
            <el-table-column prop="college_name" align="center" label="学校名称" width="" class="table-h">
              <template slot-scope="scope">
                <span  @click="major_show(scope.row.majors,scope.row.college_name,scope.row.college_id)" class="a">{{ scope.row.college_name }}</span>
              </template>
            </el-table-column>
            <el-table-column prop="college_id" align="center" label="院校代码" >
              <template slot-scope="scope">
                <span>{{ scope.row.college_id }}</span>
              </template>
            </el-table-column>
            <el-table-column prop="address" align="center" label="学校地址" class="table-h">
              <template slot-scope="scope">
                <span class="a">{{ scope.row.address }}</span>
              </template>
            </el-table-column>
            <el-table-column prop="type" align="center" label="学校类型" class="table-h">
              <template slot-scope="scope">
                <span class="a">{{ scope.row.type }}</span>
              </template>
            </el-table-column>
            <el-table-column prop="plan" align="center" label="2023年计划招生" class="table-h">
              <template slot-scope="scope">
                <span class="a">{{ scope.row.plan }}</span>
              </template>
            </el-table-column>
            <el-table-column prop="low_grades" align="center" label="2023年最低分" class="table-h">
              <template slot-scope="scope">
                <span class="a">{{ scope.row.low_grades }}</span>
              </template>
            </el-table-column>
            <el-table-column prop="low_ranking" align="center" label="2023年最低位次" class="table-h">
              <template slot-scope="scope">
                <span class="a">{{ scope.row.low_ranking }}</span>
              </template>
            </el-table-column>
            <el-table-column prop="college_percent" align="center" label="被录取的概率" class="table-h">
              <template slot-scope="scope">
                <span class="a" @change="num++">{{ scope.row.college_percent +'%'}}</span>
              </template>
            </el-table-column>
          </el-table-column>
        </el-table>

        <el-pagination
            :page-size.sync="pageSize"
            :page-sizes="pageSizes"
            :current-page.sync="currentPage"
            :pager-count="pageCount"
            background
            style="margin-top: 6px"
            layout="sizes,prev, pager, next,jumper,->,total"
            :total=total
        >
        </el-pagination>
      </el-card>
      <div >

        <el-dialog
            :visible.sync="showDialog"
            title="专业"
            width="80vw"
            :before-close="Close_dialog"
            id="dialog-box1"
        >
          <el-table :data="info2.slice((currentPage-1)*pageSize,currentPage*pageSize)" style="overflow-x: visible; " stripe >
            <el-table-column label="专业详细信息" class="Fill_size" align="center">
              <el-table-column prop="major_name" align="center" label="专业名称" width="" class="table-h">
                <template slot-scope="scope">
                  <span class="a">{{ scope.row.major_name }}</span>
                </template>
              </el-table-column>
              <el-table-column prop="major_id" align="center" label="专业代码">
                <template slot-scope="scope">
                  <span>{{ scope.row.major_id }}</span>
                </template>
              </el-table-column>
              <el-table-column prop="major_year" align="center" label="学制" class="table-h">
                <template slot-scope="scope">
                  <span class="a">{{ scope.row.major_year }}</span>
                </template>
              </el-table-column>
              <el-table-column prop="major_pay" align="center" label="学费" class="table-h">
                <template slot-scope="scope">
                  <span class="a">{{ scope.row.major_pay}}</span>
                </template>
              </el-table-column>
              <el-table-column prop="major_plan" align="center" label="计划招生人数" class="table-h">
                <template slot-scope="scope">
                  <span class="a">{{ scope.row.major_plan }}</span>
                </template>
              </el-table-column>
              <el-table-column prop="major_object" align="center" label="限选课目" class="table-h">
                <template slot-scope="scope">
                  <span class="a">{{ scope.row.major_object}}</span>
                </template>
              </el-table-column>
              <el-table-column prop="major_grades" align="center" label="去年最低分数线" class="table-h">
                <template slot-scope="scope">
                  <span class="a">{{ scope.row.major_grades }}</span>
                </template>
              </el-table-column>
              <el-table-column prop="major_ranking" align="center" label="去年最低位次" class="table-h">
                <template slot-scope="scope">
                  <span class="a">{{ scope.row.major_ranking }}</span>
                </template>
              </el-table-column>
              <el-table-column prop="major_percent" align="center" label="专业录取概率" class="table-h">
                <template slot-scope="scope">
                  <span class="a">{{ scope.row.major_percent+'%'}}</span>
                </template>
              </el-table-column>
              <el-table-column align="center" label="操作" class="a" style="padding-left:300px ">
                <template slot-scope="scope">
                  <el-button type="primary"
                             style="padding: 20px"   @click="getadd(scope.row.major_name,scope.row.major_id)">
                    添加
                  </el-button>
                </template>
              </el-table-column>

            </el-table-column>
          </el-table>
          <el-pagination
              :page-size.sync="pageSize"
              :page-sizes="pageSizes"
              :current-page.sync="currentPage"
              :pager-count="pageCount"
              background
              style="margin-top: 6px"
              layout="sizes,prev, pager, next,jumper,->,total"
              :total=total1
          >
          </el-pagination>
        </el-dialog>

        <el-dialog
            v-if="show_dialog(num_dialog)"
            center
            style="margin-top: -160px"
            id="dialog-box"
            title="用户须知"
            :visible.sync="dialogVisible2"
            append-to-body
            destroy-on-close
            @close="close_dialog"
        >
          <span slot="footer" class="dialog-footer"></span>
          <h3>选课、高考分数、高考位次为必填项！</h3>
          <h3>本系统根据2022和2023两年录取数据，进行推荐志愿和预测录取风险.</h3>
          <h3>本系统推荐的院校名单，仅供参考，报考风险由考生本身承担！</h3>
          <el-button @click="dialogVisible2 = false" id="agree_button">同意</el-button>
        </el-dialog>

      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {

  name:'FillVolunteer',
  data() {
    return {
      college_id: '',
      college_name: '',
      check_data:'',
      data_fenshu:'',
      data_paiming:'',
      showDialog:false,
      num:0,
      input:'',
      username:'',
      button_checked: 'ben',
      button_checked2:false,
      dialogVisible: false,
      dialogVisible2: true,
      value: false,
      num2: false,
      a: "0",
      checkList: [],//选课
      checkList1: ["物理", "化学", "生物"],//选课
      panduan: true,//判断本科/专科
      add: "",
      //三个下拉列表
       CX:{
         list1: '',
         list3: '',
         list4:'',
       },
      total: 0,
      total1:0,
      pageSize: 10,  //一页显示多少条
      pageSizes: [5, 10, 15, 20, 50],//每页显示多少条
      currentPage: 1,  //当前位于哪页
      pageCount: 7,   //多少分页按钮
      info: [],
      info2:[],
      num_dialog: '',
      length_ben:'',
      length_zhuan:'',
      //地区
    }
  },
  methods: {
    major_show(majors,name,id){
      this.showDialog = true;
      this.info2=majors
      this.college_id=id
      this.college_name=name
      this.total1=majors.length
    },
    Close_dialog(){
      this.$confirm(null,{
        message:'是否关闭？',
        confirmButtonText:'是',
        cancelButtonText:'否',
      }).then(()=>{
          this.showDialog = false;
      })
    },
    // 获取数据
    get1() {
      const loading = this.$loading({
        lock:true,
        text:'',
        spinner:'',
        background:'rgba(0, 0, 0, 0.7)',
      });

      if (this.CX.list1 === '') this.list1 = '';
      if (this.list4 === '') this.list4 = '';
      if (this.CX.list3 === '') this.list3 = '';

      axios({
        method:'POST',
        url:'api/students/recommend',
        data:{
          action:'rec_list_order',
          first:this.button_checked2===false?'院校优先':'专业优先',
          like:{
            sort_by:'综合排序',
            address:JSON.stringify(this.CX.list1),
            type:[this.CX.list3,this.CX.list4],
            major:[this.input],
            set:this.button_checked==='ben'?'本科':'专科'
          },
          account:this.$cookies.get('user_name')
          // account:'12345678'
        }

      }).then((resp)=>{
        this.info = resp.data.college_major;
        this.total= resp.data.college_major.length
          console.log(this.info)
      }).catch((err)=>{
        console.log(err)
      })

      loading.close();
    },



    choose_major(val) {
      if (val == 'ben')
        return 1;
      else {
        return 2;
      }
    },

    // 是否显示dialog
    show_dialog(val) {
      if (val == 1) {
        return true;
      } else {
        return false
      }
    },

    // 收藏按钮
    getadd(mName,mId) {
      axios({
        method:'POST',
        url:'api/students/gkorder',
        data:{
          action:'add_order',
          data:{
            college_name:this.college_name,
            college_id:this.college_id,
            major_name:mName,
            major_id:mId,
          },
          major_set:this.button_checked==='ben'?'本科':'专科',
          // account:'12345678'
          account:this.$cookies.get('user_name')
        }
      }).then((resp)=>{
        if(resp.data.ret===0){
          this.$message.success('收藏成功')
          console.log(this.college_name)
        }else{
          this.$message.error(resp.data.msg)
        }
      })
    },

    close_dialog() {
      this.$cookies.set('number_dialog_school', 0, '0');
    },


  },

}
</script>

<style scoped>
#dialog-box1{
  text-align: center;
}

.el-form {
  width: 300px;
}


.box-card {
  /*margin-top: -10px;*/
  /*height: 290px;*/
  width: 1574px;
  margin: auto;
}

#box{
  margin: 0;
  padding: 0;
  /*border: 1px solid red;*/
  text-align: left;
}

.box-tit{
  margin-left: 5px;
}

.box-card2 {
  width: 1250px;
  margin: auto;
}

#id1 {
  margin-top: 20px;
}
.el-button{
  padding: 0;
}
.el-table {
  width: 1574px;
  margin: auto;
  margin-top: 25px;
}

.width_form {
  margin-left: 10px;
  width: 160px
}

.a {
  text-decoration: none;
  font-size: 18px;
  color: #5e402f;
  cursor: pointer
}
.a:hover{
  color: blueviolet;
  font-weight: 700;
  font-size: 20px;
}

.tijiao{
  position: absolute;
  left: 260px;
  top: 436px;
}

.b {
  text-decoration: none;
  font-size: 19px;
  color: #5e402f;
}

.b:hover {
  text-decoration: none;
  font-size: 19px;
  color: #ff5b00;
}

.Fill_size {
  /*font:bolder 18px "楷体";*/
  font-size: 20px;
}

.size_t1 {
  font-size: 22px;
}
#dialog-box{
  width: 900px;
  margin: 0 auto;
  display: flex;
  justify-content: center;
  align-items: center;
  position: absolute;
}

#agree_button{
  position: absolute;
  left: 190px;
}

.table-h{
  width: 100px;
}
</style>
