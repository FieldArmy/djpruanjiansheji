<template>
  <div>
<!--      <el-button type="primary" @click="getName">buttonCont</el-button>-->
    <el-container style="height: 100vh">
      <el-header id="top-box_main">
        <img src="../assets/pic.png">
        <h3 class="hh3" >志高考</h3>
        <div id="user">
          <el-button type="text" class="hello2">Hi,{{ this.teacher_name }}</el-button>
          <el-dropdown id="question">
            <div id="hide">
              <el-avatar class="img"
                  src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png">
              </el-avatar>
            </div>
            <el-dropdown-menu slot="dropdown" style="width: 100px;text-align: center">
              <el-button type="text" @click="jump1">修改密码</el-button>
              <el-button type="text" @click="jump2">退出登录</el-button>
            </el-dropdown-menu>
          </el-dropdown>
        </div>
      </el-header>

      <el-container>

        <el-aside id="aside-box">
          <el-menu
              default-active="2"
              class="el-menu-demo"
              background-color="#545c64"
              text-color="#fff"
              active-text-color="#ffd04b"
              router
          >
            <el-menu-item index="/consult_student">
              <i class="el-icon-camera-solid"></i>
              <span slot="title" class="cebian">学生问题</span>
            </el-menu-item>

          </el-menu>
        </el-aside>

        <el-main id="body-box">
          <router-view></router-view>
        </el-main>

      </el-container>
    </el-container>
  </div>
</template>

<script>
export default {
  name: "consult_teacher",
  Active_pith: '/stu',
    data(){
      return{
          teacher_name:'',
      }
    },
    methods:{
      getName(){
          this.teacher_name = this.$cookies.get('teacher_name');
          console.log(this.teacher_name);
      },
      jump1() {
        this.$router.push('/tea_changepass')
      },
      jump2() {
        window.sessionStorage.clear();//清楚session
        this.$router.push('/')
        this.$message.success("退出成功！")
      },
      jump3() {
        this.$router.push('/Tea_ForgetPass')
      },
    },
  created() {
    this.getName()
  }
}
</script>

<style scoped>
#top-box_main {
  height: 70px !important;
  /*border: 1px solid pink;*/
  position: relative;
}


#inform {
  width: 500px;
  height: 70px;
  line-height: 70px;
}

#tit {
  vertical-align: middle;
  padding-left: 10px;
  font-weight: 700;
  font-size: 20px;
}

/*用户盒子*/
#user {
  display: flex;
  align-items: center;
  justify-content: center;
  vertical-align: middle;

  width: 200px;
  height: 70px;
  /*border: 1px solid chartreuse;*/
  position: absolute;
  top: 0;
  right: 0;
}

#hide {
  margin-left: 20px;
}

/deep/ .el-button+.el-button{
    margin-left: 0!important;
}

#aside-box {
  width: 220px !important;
  /*height: 1000px;*/
  /*border: 1px solid red;*/
  background-color: #545c64;
}

.el-menu {
  border: 0 solid transparent;
}

.el-menu-item {
  height: 100px;
  line-height: 100px;
  /*padding: 30px 10px!important;*/
}

#body-box {
  /*border: 1px solid blue;*/
  background-color: #defcfc;
}

.cebian {
  font-size: 16px;
}

.cebian:hover {
  font-size: 16px;
  color: #ffd04b;
}
.hello2 {
  font-size: 18px;
  position: absolute;
  top: 35px;
  right: 110px;
}
.el-header img {
  margin-top: 4px;
  margin-left: -10px;
  height: 70px;
}
#question {
  position: absolute;
  top: 19px;
  right: 45px;
}
.hh3 {
  font: bolder 30px "Adobe 黑体 Std R";
  margin-left: 80px;
  margin-top: -60px;
}
.img {
  width: 50px;
  height: 50px;
}
</style>
