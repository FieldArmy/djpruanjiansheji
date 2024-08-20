<!--登录页找回密码-->
<template>
  <div class="login_page">
    <el-container>
      <el-main>
        <el-card class="box-card" >
          <div slot="header" >
            <h2 class="login-title">找回密码</h2>
          </div>
          <div>

            <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px" class="form">
              <el-form-item style="margin-left: 25px"  label="用户名:" prop="username" align="left">
                <el-input v-model="ruleForm.username" placeholder="请输入用户名:" style="width: 250px"></el-input>
              </el-form-item>
              <el-form-item style="margin-left: 25px" label="邮 箱 :" prop="email" align="left">
                <el-input v-model="ruleForm.email" placeholder="请输入邮箱:" style="width: 250px"></el-input>
              </el-form-item>
              <el-form-item style="margin-left: 25px" label="新密码:" prop="password" align="left">
                <el-input placeholder="请输入新密码" v-model="ruleForm.password" style="width: 250px" show-password></el-input>
              </el-form-item>
              <el-form-item style="margin-left: 25px" label="确认密码:" prop="changePass" align="left">
                <el-input placeholder="请确认密码" v-model="ruleForm.changePass" style="width: 250px" show-password></el-input>
              </el-form-item>
              <el-form-item class="form" label="邮箱验证码" prop="emailcode">
                <el-input v-model="ruleForm.emailcode" placeholder="请输入验证码" style="width: 50%"> </el-input>
                <el-button type="primary" round style="margin-left: 80px" @click="submitCode">发送验证码</el-button>
              </el-form-item>
              <el-button type="primary" style="margin-left: 110px;margin-top: 8px" @click="getpass('ruleForm')" plain>确定</el-button>
              <el-button type="cuccess" style="margin-left: 90px" @click="addRoutes1()">返回</el-button>

            </el-form>
          </div>

        </el-card>
      </el-main>
    </el-container>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "ForgetPassword",
  data() {
    var validateRepassword = (rule, value, callback) => {
      if (value === "") {
        callback(new Error("此项不能为空"));
      } else if (value !== this.ruleForm.password) {
        callback(new Error("两次的密码不一致"));
      } else {
        callback();
      }
    };
    return {
      ruleForm: {
        username: "",
        email: "",
        password: "",
        changePass:'',
        emailcode:''
      },
      info: {},
      rules: {
        email: [
          {required: true, message: '邮箱不能为空', trigger: 'blur'},
        ],
        username: [
          {required: true, message: '用户名不能为空', trigger: 'blur'},
        ],
        password: [
          {required: true, message: '密码不能为空', trigger: 'blur'},
        ],
        changePass: [
          {required: true, validator: validateRepassword, trigger: "change"},
          {min: 6, max: 15, message: '长度在 6 到 15 个字符', trigger: 'change'}
        ],
      },
    }
  },
  methods: {
    getpass() {
      this.$refs['ruleForm'].validate((valid) => {
        if (valid) {
          console.log(this.ruleForm.username + '/' + this.ruleForm.email + '/' + this.ruleForm.password)
          axios({
            method:'POST',
            url:'api/students/findpassword',
            data:{
              account:this.ruleForm.username,
              password:this.ruleForm.password,
              mail:this.ruleForm.email,
              code:this.ruleForm.emailcode,
              session_id:this.ruleForm.session_id
            }
          }).then((resp)=>{
            if (resp.data.ret === 0) {
              this.$message.success("修改成功！");
            }
            if (resp.data.ret !== 0) {
              this.$message.error(resp.data.msg);
              console.log(resp.data.msg)
            }
          })
        }
      })

    },
    submitCode(){
      axios({
        method:'POST',
        url:'api/students/givecode',
        data:{
          mail:this.ruleForm.email
        }
      }).then((resp)=>{
        console.log(resp.data)
        this.ruleForm.session_id=resp.data.session_id
      }).catch((err)=>{console.log(err,this.ruleForm.email)})
    },
    addRoutes1() {
      this.$router.push("/Login_Teacher")  //返回登录页
    }
  }
}
</script>

<style scoped>
.login_page {
  width: 100%;
  height: 100%;
  /*background: url(https://pic.imgdb.cn/item/613a49d144eaada739e42e35.jpg);*/
  /*background-size: 100% 100%;*/
  background-size: cover;
  position: fixed;
  background-attachment: fixed!important;
}

.login-title {
  text-align: center;
  margin: 0 auto 10px auto;
  margin-top: 10px;
  color: #303133;
}

.text {
  font-size: 14px;
}

.item {
  padding: 18px 0;
}

.form {
  margin-left: 30px;
  margin-top: 10px;
}

.box-card {
  border-radius: 40px;
  margin: auto;
  margin-top: 150px;
  width: 550px;
  height: 550px;

}
.clearfix:before,
.clearfix:after {
  display: table;
  content: "";
}
</style>
