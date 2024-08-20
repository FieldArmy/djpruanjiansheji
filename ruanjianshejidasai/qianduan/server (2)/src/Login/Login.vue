<template>
  <div class="login_page">
  <img src="../assets/1.png" class="bgc"/>
    <transition name="hello" appear>
      <div id="card">
        <el-form ref="loginForm" :model="form" :rules="rules" id="form-box" label-width="80px" style="border: 0">
          <div id="input-all">
            <el-form-item label="账号" prop="account">
              <el-input type="text" v-model="form.account" placeholder="请输入账号" class="input-box"/>
            </el-form-item>

            <el-form-item label="密码" prop="password">
              <el-input type="password" v-model="form.password" placeholder="请输入密码" @keyup.enter="enterSearchMember" class="input-box" show-password/>
            </el-form-item>
          </div>

          <el-form-item id="forget-remember">
            <el-checkbox v-model="checked">记住密码</el-checkbox>
            <el-button type="text" @click="addRoutes1" id="post">注册账号</el-button>
            <el-button type="text" @click="addRoutes2" id="forget">忘记密码</el-button>
          </el-form-item>

          <el-form-item>
            <el-button type="primary" @click="onSubmit()" id="loading" class='submit'>登录</el-button>
          </el-form-item>


          <el-form-item id="best-box">
            <el-button type="text" @click="addRoutes3">管理员登录</el-button>
            <el-button type="text" style="margin-left: 100px" @click="addRoutes5">咨询师登录</el-button>
          </el-form-item>
        </el-form>
      </div>
    </transition>
      <div id="police">
          <a href="https://beian.miit.gov.cn/" style="text-decoration: none">
<!--            备案号-->
          </a>
          <br>
          <span>
<!--              建议您使用Chrome、Firefox、Edge、IE10及以上版本和360等主流浏览器浏览本网站-->
          </span>
      </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Login",
  data() {
    return {
      // 初始值
      form: {
        account: '',
        password: ''
      },
      user: "",
      number_dialog: 1,
      //表单验证，需要在 el-form-item 元素中增加prop属性
      rules: {
        account: [
          {required: true, message: "账号不可为空", trigger: "blur"}
        ],
        password: [
          {required: true, message: "密码不可为空", trigger: "blur"}
        ]
      },
      checked: true,

        pingwei:['为了方便您的使用，我们为您提供了用户和管理员账号',
          '用户账号：user',
          '用户密码：12345678',
            '管理员账号：admin',
            '管理员密码：qwe34rt',
            '(此消息30s后消失)'],

        newDatas:[],
    }
  },
  methods: {

    onSubmit() {
      //为表单绑定验证功能
      const _this = this;

      if(this.form.account === ""){this.$message.warning("请输入用户名！")}
      else if(this.form.password === ""){this.$message.warning("请输入密码！")}
      else{
          axios.post("api/students/signin", this.form).then(resp => {
            console.log(resp);//使用vue-router路由到指定界面，该方式称为编程式导航
            console.log(resp.data)
            this.user = this.form.account           //使用vue-router路由到指定界面，该方式称为编程式导航
            if (resp.data.ret === 0) {
              window.sessionStorage.setItem("user", this.user);
              // if(this.isMobile()){
              //     this.$router.push('phone_home');
              // }
              // else {
                  this.$router.push('index');
                this.$notify.closeAll();
              // }
              this.$message.success("登录成功");
              this.$cookies.set('user_name', this.user, '0');
              this.$cookies.set('number_dialog_school', this.number_dialog, '0', {path: '/Fillvolunteer'});
              if (this.checked === true) {
                this.setCookies(this.form.account, this.form.password, 7);
              } else {
                this.clearCookies();
              }
            }
            if (resp.data.ret !== 0) {
              this.$message.error("账号不存在或者密码错误！");
            }
          }).catch((err)=>{ console.log(err)})
      }
    },

    enterSearchMember() {
      this.onSubmit()  //回车之后的执行的方法
    },
    //弹窗提示密码
    open_notify() {
        const h = this.$createElement;
      for (let i in this.pingwei) {
        this.newDatas.push(h('p', null, this.pingwei[i]));
      }

      this.$notify({
          title: '尊敬的各位评委老师',
          message: h('div', null, this.newDatas),
          duration: 30000,
      });
    },

    addRoutes1() {
      this.$router.push('/email');
      this.$notify.closeAll();
    },//注册
    addRoutes2() {
      this.$router.push('/forgetpassword');
        this.$notify.closeAll();
    },//忘记密码
    addRoutes3() {
      this.$router.push('/login_root');
        this.$notify.closeAll();
    },//管理员界面
    addRoutes5() {
      this.$router.push('Login_Teacher');
        this.$notify.closeAll();
    },//咨询师登录
    addRoutes4() {
      this.$router.push('/tealogin');
        this.$notify.closeAll();
    },//咨询师界面

    // 设置Cookies
    setCookies(c_name, c_pwd, c_time) {
      var exdata = new Date();
      // 设置保存时间
      exdata.setTime(exdata.getDay() + 24 * 60 * 60 * 1000 * c_time);

      // 拼接Cookies
      var expare = exdata.toUTCString();
      window.document.cookie = 'userName' + '=' + c_name + ";" + expare + ";path=/";
      window.document.cookie = 'userPwd' + '=' + c_pwd + ";" + expare + ";path=/";
    },

    // 获取Cookies
    getCookies(cname, cpwd) {
      var name = cname + "=";
      var pwd = cpwd + "=";
      // 对Cookies进行解码
      var decodedCookies = decodeURIComponent(document.cookie);

      // 将Cooies进行拆分，放到ca数组中
      var ca = decodedCookies.split(';');

      for (let i = 0; i < ca.length; i++) {
        // 读取每一个ca的值
        var c = ca[i].split('=');
        if (c[0] == ' userName') {
          this.form.account = c[1];
        } else if (c[0] == ' userPwd') {
          this.form.password = c[1];
        }
      }
      return "";
    },

    // 清除Cookies
    clearCookies: function () {
      this.setCookies("", "", -1);
    },

      // 获取手机型号
      isMobile(){
          let flag = navigator.userAgent.match(/(phone|pad|pod|iPhone|iPod|ios|iPad|Android|Mobile|BlackBerry|IEMobile|MQQBrowser|JUC|Fennec|wOSBrowser|BrowserNG|WebOS|Symbian|Windows Phone)/i);
          return flag;
      },
  },

  created() {
    axios({
      method:'GET',
      url:'api/students/flag',
    })
    this.open_notify();
    this.getCookies(this.form.account, this.form.password);
    const _this = this;
    document.onkeydown = function (e) {
      var key = window.event.keyCode;
      if (key == 13) {
        _this.enterSearchMember();
      }
    }
  },
}
</script>

<style scoped>
.login_page {
  width: 100%;
  height: 100%;
  background: url(../assets/2.png);
  background-size: cover;
  position: fixed;
  background-attachment: fixed !important;
}

.bgc{
  display: block;
  width: 45%;
  height: 100%;
}
#card {
  position: absolute;
  top: 45%;
  left: 75%;
  z-index: -999;
  transform: translate(-50%, -50%);
  width: 570px;
  height: 450px;
  //background-color: white;
  //box-shadow: 0 2px 12px 0 rgba(0, 0, 0, .1);
  //border-radius: 20px;
  background: url(../assets/zhigaokao_login.png);
  background-size: cover;
}

#login-title {
  margin: 0;
  padding-top: 40px;
  text-align: center;
}

#form-box {
  width: 450px;
  margin: 160px auto 0 auto;
  /*border: 1px solid blue;*/
}

.submit{
  margin-top: -5px;
  width: 180px;
  height: 30px;
  line-height: 8px;
}

.el-form-item {
  padding: 0;
}

#input-all {
  padding-left: 15px;
}

.input-box {
  width: 300px;
  margin-bottom: 10px;
}

.el-form >>> .el-form-item__error {
  padding-top: 0px !important;
}

#forget-remember {
  position: relative;
  margin-top: -15px;
  margin-bottom: 5px;
}

#post {
  position: absolute;
  left: 120px;
}

#forget {
  position: absolute;
  right: 90px;
}

#loading {
  width: 270px;
  margin-left: 10px;
  border-radius: 40px;
  margin-bottom: 5px;
}

#teacher {
  position: absolute;
  right: 80px;
}

#best-box {
  margin-top: -10px;
}

#police {
    position: fixed;
    bottom: 0;

    width: 100%;
    padding: 20px;
    margin: 0 auto;
    /*height: 200px;*/
    background-color: transparent;
    text-align: center;
    color: #333;
}

@media all and (max-width: 780px){
    #police {
        width: 780px;
        overflow-x: hidden;
    }
}

.hello-enter-active{
  animation: atguigu linear 1.5s forwards;
}


@keyframes atguigu {
  from{
    margin-left: -1000px;
  }
  to{

  }
}

</style>
