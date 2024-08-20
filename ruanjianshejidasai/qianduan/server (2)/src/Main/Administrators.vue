<template>
  <div class="body">
    <el-backtop>
      <div
          style="{
        height: 100%;
        width: 100%;
        background-color: #f2f5f6;
        box-shadow: 0 0 6px rgba(0,0,0, .12);
        text-align: center;
        line-height: 40px;
        color: #1989fa;
      }"
      >
        UP
      </div></el-backtop>
    <el-container style="height: 100vh">
      <el-header height="70px">
        <div>
          <img  src="../assets/pic.png">
          <h3 class="hh3">志高考</h3>
          <el-button type="text" class="hello2">Hi,管理员</el-button>
          <el-dropdown id="question">
                    <span class="el-dropdown-link">
                      <el-avatar class="img"
                                 src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png"></el-avatar>
                    </span>
            <el-dropdown-menu slot="dropdown" style="width: 80px" align="center">
              <el-button type="text" @click="jump2()">退出登录</el-button>

            </el-dropdown-menu>
          </el-dropdown>
        </div>
      </el-header>

      <el-container>
        <el-aside width="220px" align="left">
          <el-menu
              default-active="2"
              class="el-menu-vertical-demo"
              background-color="#545c64"
              text-color="#fff"
              active-text-color="#ffd04b"
              router
          >

            <el-menu-item index="/admain" style="margin-top: 2px">
              <i class="el-icon-s-claim"></i>
              <span slot="title" class="cebian">用户信息</span>
            </el-menu-item>

            <el-menu-item index="/teacherinfo" >
              <i class="el-icon-s-help"></i>
              <span slot="title" class="cebian">咨询师信息</span>
            </el-menu-item>
            <el-menu-item index="/useropinion" >
              <i class="el-icon-chat-dot-round"></i>
              <span slot="title" class="cebian">用户反馈</span>
            </el-menu-item>

          </el-menu>
        </el-aside>

        <el-main>
          <router-view></router-view>
        </el-main>

      </el-container>
    </el-container>
  </div>
</template>

<script>
export default {
  name: "main",
  data() {
    return {
      isCollapsed: true,
    }
  },
  methods: {
    jump2() {
      window.sessionStorage.clear();//清楚session
      this.$router.push('/')
      this.$message.success("退出成功！")
    },
  }
}
</script>

<style scoped>
.body {
  margin: auto;
}

.el-header {
  font-size: 30px;
  justify-content: space-between;
}

.el-header img {
  margin-left: -10px;
  margin-top: 4px;
  height: 70px;
}
.hh3{
  font: bolder 30px "Adobe 黑体 Std R";
  margin-left:80px;
  margin-top: -63px;
}
.el-menu-item{
  height: 85px;
  line-height: 85px;
}
.el-aside {
  background-color: #545c64;
}

#question {
  position: absolute;
  top: 19px;
  right: 45px;
}

.hello2 {
  /*font-family: "Lithos Pro Regular";*/
  font-size: 18px;
  position: absolute;
  top: 35px;
  right: 110px;
}
/*.hello2:hover{*/
/*  !*font-family: "Lithos Pro Regular";*!*/
/*  font-size: 18px;*/
/*  position: absolute;*/
/*  top: 38px;*/
/*  right: 110px;*/
/*}*/

.img {
  width: 50px;
  height: 50px;
}

.el-main {
  background-color: #defcfc;
}

.cebian{
  font-size:  16px ;
}
.cebian:hover{
  font-size:  16px ;
  color: #ffd04b;
}

.el-menu{
  border: 0 solid transparent;
}
</style>
