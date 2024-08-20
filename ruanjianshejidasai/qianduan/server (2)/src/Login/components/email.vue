<template>
  <div class="login_page">
    <el-card class="box-card">
      <div slot="header" class="clearfix">
        <h2 class="login-title">用户注册</h2>
        <h3></h3>
      </div>

      <div>
        <div class="user_logon_develop_ym">

          <el-form ref="add_form" :model="ruleForm" :rules="rules" label-width="100px">
            <el-form-item class="form" label="用户名" prop="username">
              <el-input v-model="ruleForm.username" placeholder="请输入用户名"></el-input>
            </el-form-item>
            <el-form-item class="form" label="个人邮箱" prop="email">
              <el-input v-model="ruleForm.email" placeholder="请输入个人邮箱"></el-input>
            </el-form-item>
            <el-form-item class="form" label="密码" prop="password">
              <el-input type="password" v-model="ruleForm.password" placeholder="请输入密码" show-password></el-input>
            </el-form-item>
            <el-form-item class="form" label="确认密码: " prop="checkPass">
              <el-input type="password" v-model="ruleForm.checkPass" placeholder="请确认密码:" autocomplete="off"
                        show-password></el-input>
            </el-form-item>
<!--            <el-form-item class="form" label="邮箱验证码" prop="emailcode">-->
<!--              <el-input v-model="ruleForm.emailcode" placeholder="请输入验证码" style="width: 50%"> </el-input>-->
<!--              <el-button type="primary" round style="margin-left: 80px" @click="submitCode">发送验证码</el-button>-->
<!--            </el-form-item>-->
            <el-form-item>
              <el-button type="success" style="margin-left: 0;margin-top: 10px" @click="onSubmit('add_form')">注册
              </el-button>
              <el-button type="info" style="margin-left: 50px" @click="resetForm('add_form')">重置</el-button>
              <el-button style="margin-left: 50px" @click="addtest()">返回</el-button>
            </el-form-item>

          </el-form>

        </div>
      </div>
    </el-card>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "LogonDevelop",
  data() {
    var validateRepassword = (rule, value, callback) => {
      if (value === "") {
        callback(new Error("请输入确认密码"));
      } else if (value !== this.ruleForm.password) {
        callback(new Error("两次的密码不一致"));
      } else {
        callback();
      }
    };
    return {
      ruleForm: {
        username: '',
        password: '',
        email: '',
        time: "",
        checkPass: '',
        emailcode:'',
        session_id:''
      },
      rules: {
        username: [{required: true, message: "账号不可为空", trigger: "blur"}],
        password: [
          {required: true, message: "密码不可为空", trigger: "blur"},
          {min: 6, max: 15, message: '长度在 6 到 15 个字符', trigger: 'change'}],
        email: [
          {required: true, message: "邮箱不可为空", trigger: "blur"},
          {
            type: 'string',
            message: '邮箱格式不正确',
            trigger: 'blur',
            transform(value) {
              if (!/^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+(.[a-zA-Z0-9_-])+/.test(value)) {
                return true
              }
            }
          },
        ],
        checkPass: [
          {required: true, validator: validateRepassword, trigger: "change"},
          {min: 6, max: 15, message: '长度在 6 到 15 个字符', trigger: 'change'}
        ],
      }
    };
  },
  methods: {
    onSubmit() {
      const _this = this;
      this.$refs['add_form'].validate((valid) => {
        console.log(11111)
        if (valid) {
          axios({
            method:'POST',
            url:'api/students/signup',
            data:{
              account:this.ruleForm.username,
              password:this.ruleForm.password,
              mail:this.ruleForm.email,
              session_id:this.ruleForm.session_id
            }
          }).then((resp)=>{
            if (resp.data.ret === 0) {
              _this.$message.success("注册成功！");
              this.$router.push('/')
            }
            if (resp.data.ret !== 0) {
              _this.$message.error(resp.data.msg);
              console.log(resp.data.msg)
            }
          })
        } else {
          _this.$message.error("校验失败！")
        }
      })
    },
    addtest() {
      this.$router.push('/')
    },

    resetForm(formName) {
      this.$refs[formName].resetFields();
    },
  },

}
</script>
<style scoped>
.login_page {
  width: 100%;
  height: 100%;
  background-image: url("../../assets/tea.png");
  background-size: 100% 100%;
  position: fixed;
  background-attachment: fixed !important;
}

.user_logon_develop_ym {
  width: 500px;
  margin: auto;
}

.box-card {
  border-radius: 40px;
  /*margin-left: 680px;*/
  margin: auto;
  margin-top: 50px;
  width: 600px;
  //height: 445px;
}

.form {
  margin-left: -20px;
  width: 500px;
}

.login-title {
  text-align: center;
  margin: 10px auto -15px auto;
  color: #303133;
}
</style>
