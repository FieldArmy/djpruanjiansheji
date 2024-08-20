<template>
  <div class="login_page">
    <el-card class="el-card">
      <div slot="header" >
        <h2 class="login-title">管理员登录</h2>
      </div>
      <el-form ref="loginForm" :model="form" :rules="rules" label-width="80px" class="login-box">

        <el-form-item class="form" label="账号" prop="username">
          <el-input type="text" placeholder="请输入账号" v-model="form.username"/>
        </el-form-item>
        <el-form-item class="form" label="密码" prop="password">
          <el-input type="password" placeholder="请输入密码" v-model="form.password" @keyup.enter="enterSearchMember" show-password/>
        </el-form-item>
        <el-form-item>
<!--          <el-button type="primary" style="margin-left: 65px;margin-top: 10px" @click="onSubmit('loginForm')">登录-->
<!--          </el-button>-->
          <el-button type="primary" style="margin-left: 65px;margin-top: 10px" @click="onSubmit()">登录
          </el-button>
          <el-button type="plain" class="btn2" style="margin-left: 35px" @click="get()">返回</el-button>
        </el-form-item>
      </el-form>
    </el-card>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Login",
  data() {
    return {
      form: {
        username: '',
        password: ''
      },
      //表单验证，需要在 el-form-item 元素中增加prop属性
      rules: {
        username: [
          {required: true, message: "账号不可为空", trigger: "blur"}
        ],
        password: [
          {required: true, message: "密码不可为空", trigger: "blur"}
        ]
      },
    }
  },

  methods: {
    onSubmit() {
      // this.$refs['loginForm'].validate((valid) => {
        // if (valid) {
      if(this.form.username == ''){this.$message.warning("请输入用户名！")}
      else if(this.form.password == ''){this.$message.warning("请输入密码！")}
      else {
        axios({
          method:'POST',
          url:'api/manager/signin',
          data:{
            account:this.form.username,
            password:this.form.password
          }
        }).then((resp)=>{
          if (resp.data.ret ===0) {
            window.sessionStorage.setItem("user", this.form.username);
            // console.log(this.user);  //admin
            this.$router.push('admain');
            this.$message.success("登录成功");
            this.$notify.closeAll();
          }
          else{
            this.$message.error("账号不存在或者密码错误！");
          }
        })
      }

    },
    get() {
      this.$router.push('/');
        this.$notify.closeAll();
    },
    open2() {
      let data = [
        '管理员账号：root',
        '密码：123456',
      '(此消息30s后消失)'];
      let newDatas = [];
      const h = this.$createElement;
      for (let i in data) {
        newDatas.push(h('p', null, data[i]));
      }
      this.$notify({
        title: '尊敬的各位评委老师',
        message: h('div', null, newDatas),
        duration: 30000,
      });
    },
    enterSearchMember() {
      this.onSubmit()
    },
  },
  created() {
    this.open2()
    const _this = this;
    document.onkeydown = function (e) {
      var key = window.event.keyCode;
      if (key == 13) {
        _this.enterSearchMember();
      }
    }
  }
}
</script>

<style scoped>
.login_page {
  margin: auto;
  background: url(../assets/admain1.png);
  /*filter: blur(5px);*/
  /*background-size: 100% 100%;*/
  background-size: cover;
  position: fixed;
  background-attachment: fixed!important;
  /*position absolute*/
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: -1;
}

.el-card {
  margin: auto;
  width: 500px;
  height: 350px;
  /*margin-left: 720px;*/
  margin-top: 100px;
  border-radius: 40px;
}

.login-title {
  text-align: center;
  margin: 20px auto 8px auto;
  color: #303133;
}

.form {
  width: 310px;
  margin-left: 50px;
  margin-top: 5px;
}

.btn2 {
  background-color: #70f6e1;
  color: white;
}
</style>
