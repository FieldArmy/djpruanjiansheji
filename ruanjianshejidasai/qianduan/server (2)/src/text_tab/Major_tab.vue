<template>
  <div id="tab-box">
    <!--输出用户的数据，若有的话输出-->
    <div id="mark-box" v-if="(show == 0)?false:true">
      <span>高考分数：{{ mark }}</span>
      <el-divider direction="vertical"></el-divider>
      <span>高考位次：{{ rank }}</span>
      <el-divider direction="vertical"></el-divider>
      <span>
                科目：
                <span v-for="(item,index) in sub" :key="index" class="sub-box">{{ item }}</span>
            </span>
      <el-divider direction="vertical"></el-divider>
      <!--      修改按钮      -->
      <el-button @click="showDialog = true" title="点我修改个人信息" style="border: 0">
        <i class="el-icon-edit"></i>
      </el-button>
    </div>

    <el-tabs v-model="activeName" @tab-click="handleTabClick" >
      <el-tab-pane v-for="(item,index) in fun" :label="item.name" :key="index" :name="item.name">
        <router-view :name="item.cnm" v-if="item.show"></router-view>
      </el-tab-pane>
    </el-tabs>

    <!--dialog弹框，用于输入用户信息-->
    <el-dialog
        :visible.sync="showDialog"
        title="请填写您的高考信息"
        width="30vw"
        :before-close="Close_dialog"
        id="dialog-box"
    >
      <span class="dia-tit">高考科目</span>
      <el-checkbox-group v-model="check_data" id="check-box" style="margin-top: 15px" :max="3">
        <el-checkbox label="物理">物理</el-checkbox>
        <el-checkbox label="化学">化学</el-checkbox>
        <el-checkbox label="生物">生物</el-checkbox>
        <el-checkbox label="政治">政治</el-checkbox>
        <el-checkbox label="历史">历史</el-checkbox>
        <el-checkbox label="地理">地理</el-checkbox>
      </el-checkbox-group>
      <br>
      <br>
      <span class="dia-tit">高考分数</span>
      <br>
      <el-input v-model="data_fenshu" placeholder="请输入100-750分区间的整数" max="750" min="100" style="margin-top: 15px"></el-input>
      <br>
      <br>
      <span class="dia-tit">高考位次</span>
      <br>
      <el-input v-model="data_paiming" placeholder="请输入对应排名" style="margin-top: 15px"></el-input>
      <div id="dialog_button">
        <el-button type="success" @click="Con_dialog" >确定</el-button>
        <el-button type="warning" @click="Close_dialog">取消</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
import  axios from 'axios'
export default {
  name: "Major_tab",
  data(){
    return{
      num:0,
      user_name:'',
      activeName:'智能填报',
      fun:[
        {
          name:'智能填报',
          cnm:'fil',
          show:true,
        },
        {
          name:'个人志愿表',
          cnm:'fom',
          show: false,
        },
      ],

      // 是否显示dialog（dialog默认数据）
      showDialog:false,
      check_data:[],
      data_fenshu:null,
      data_paiming:null,


      // 判断次用户是否已经填写了数据，以及获取到接收到的数据
      show:0,
      mark:null,
      rank:null,
      sub:[],
    }
  },
  methods:{
    // 确认按钮功能，如果数据正确就传给数据库
    Con_dialog(){
      if(this.data_fenshu == null || this.data_paiming == null){
        this.$message.warning('保存失败,未填写分数或位次！');
      }
      else if(this.data_fenshu < 100 || this.data_fenshu > 750){
        this.$message.warning('保存失败，输入分数区间有误！');
      }
      else if(this.check_data.length == 0){
        this.$message.warning('请选择科目！');
      }else if(this.check_data.length<3)
        this.$message.warning(("请选择三门科目！"))
      else {
        this.data_Axios();
      }
    },

    // 取消 / 关闭 dialog 函数
    Close_dialog(){
      this.$confirm(null,{
        title:'警告',
        message:'关闭之前是否保存所做修改？',
        confirmButtonText:'保存',
        cancelButtonText:'取消',
      }).then(()=>{
        this.Con_dialog();
      }).catch(()=>{
        if(this.show == 0){
          this.$message.error("第一次使用请进行保存！");
        }else {
          this.$message.info('已取消保存！');
          this.showDialog = false;
        }
      })
    },

    // 点击确定之后添加考生的信息
    data_Axios(){
      axios({
        method:'POST',
        url:'api/students/grades',
        data:{
          action:'add_stu',
          stu_grd:parseInt(this.data_fenshu),
          address:'山东',
          subject:this.check_data,
          id:'学生',
          ranking:parseInt(this.data_paiming),
          account:this.$cookies.get('user_name'),
        }
      }).then((resp)=>{
          console.log(resp.data)
        if(resp.data.ret ===0){
          this.$message.success('保存成功！');
          this.showDialog = false;
          // 及时更新数据
          this.get_Axios();
        }
        else{
          this.$message.error(resp.data.msg);
        }
      }).catch((err)=>{
        console.log(err)})
    },

    // 数据接收
    get_Axios(){
        axios({
          method:'GET',
          url:'api/students/grades',
          params:{
            action:'get_stu',
            account:this.$cookies.get('user_name')
            // account:'12345678'
          }
        }).then((resp)=>{
          console.log('@@@@',resp.data)
          if(resp.data.ret ===0){
            this.show = 1;
            this.rank = resp.data.ranking;
            this.mark = resp.data.stu_grd;
            this.sub = resp.data.subject;
          }
        })
    },


    // 特定标签进行渲染，避免出现数据不同步情况
    handleTabClick(tab){
      let name = tab.name;
      switch (name){
        case '智能填报':
        {
          this.fun[0].show = true;
          this.fun[1].show = false;
        }break;
        case '个人志愿表':
        {
          this.fun[0].show = false;
          this.fun[1].show = true;
        }
      }
    },
  },
  mounted(){
    console.log(111)
    axios({
      method:'GET',
      url:'api/students/checkdata',
      params:{
        account:this.$cookies.get('user_name')
      }
    }).then((resp)=>{
      if(resp.data.ret===0){
        this.showDialog=false
        this.get_Axios()
        this.show=1
      }else{
        this.$message.error(resp.data.msg)
        this.showDialog=true
      }
    })
  }
}
</script>

<style scoped>
#tab-box{
  margin: 0 10px;
  padding: 0;
}

#mark-box{
  background-color: white;
  width: 35vw;
  /*border: 1px solid blue;*/
  border-radius: 25px;
  padding: 5px;
  text-align: center;
  margin: 0 0 0 auto;
  box-shadow: 0 2px 3px 0 rgba(0, 0, 0, 0.1);
}

.sub-box{
  display: inline-block;
  width: 70px;
  height: 30px;
  border: 1px solid rgba(255, 85, 143, 0.35);
  border-radius: 15px;
  text-align: center;
  line-height: 30px;
  margin: 0 5px;
}

.sub-box:hover{
  box-shadow: 0 2px 3px 0 rgba(0, 0, 0, 0.1);
}

/deep/.el-tabs__item:focus.is-active.is-focus:not(:active) {
  box-shadow: none;
  border-top-left-radius: 20px;
  border-top-right-radius: 20px;
}

/deep/.el-dialog__title{
  font-size: 24px;
  font-weight: 700;
  margin-top: 15px;
}

#dialog-box{
  text-align: center;
  padding: 10px;
}

.dia-tit{
  color: #333;
  font-size: 20px;
  font-weight: 700;
}

#check-box{
  width: 300px;
  text-align: left;
  margin: 0 auto;
  padding-left: 50px;
}

.el-dialog__body .el-input{
  width: 15vw!important;
}

#dialog_button{
  margin-top: 20px;
}
</style>