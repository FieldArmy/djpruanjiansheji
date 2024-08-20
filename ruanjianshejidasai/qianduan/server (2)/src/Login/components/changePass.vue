<!--用户修改密码-->
<template>
  <div class="login_page">
    <el-card class="box-card">
<!--      <div>-->
        <div slot="header" class="clearfix">
          <h2 class="login-title">修改密码</h2>
        </div>
        <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px" class="form">
          <el-form-item label="当前密码:" prop="password" align="left">
            <el-input placeholder="请输入当前密码" v-model="ruleForm.password" style="width: 250px" show-password></el-input>
          </el-form-item>

          <el-form-item label="新密码:" prop="new_password" align="left">
            <el-input placeholder="请输入新密码" v-model="ruleForm.new_password" style="width: 250px" show-password></el-input>
          </el-form-item>

          <el-form-item label="确认密码:" prop="changePass" align="left">
            <el-input placeholder="请确认密码" v-model="ruleForm.changePass" style="width: 250px" show-password></el-input>
          </el-form-item>
          <el-button type="primary" @click="get('ruleForm')" class="btn1">确认修改</el-button>
          <el-button @click="addRoutes()" style="margin-left: 40px">返回主页</el-button>
        </el-form>
<!--      </div>-->
    </el-card>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "changePass",
  data() {
    var validateRepassword = (rule, value, callback) => {
      if (value === "") {
        callback(new Error("此项不能为空"));
      } else if (value !== this.ruleForm.new_password) {
        callback(new Error("两次的密码不一致"));
      } else {
        callback();
      }
    };
    return {
      // panduan:false,
      ruleForm: {
        username: "",
        password: "",
        new_password: "",
        changePass:'',
      },
      info: {},
      rules: {
        password: [{required: true, message: '此项不能为空', trigger: 'blur'}],
        new_password: [
          {required: true, message: '此项不能为空', trigger: 'blur'},
          {min: 6, max: 15, message: '长度在 6 到 15 个字符', trigger: 'change'}
        ],
        // changePass: [{required: true, message: '此项不能为空', trigger: 'blur'}],
        changePass: [
          {required: true, validator: validateRepassword, trigger: "change"},
          {min: 6, max: 15, message: '长度在 6 到 15 个字符', trigger: 'change'}
        ],
      },
    }
  },
  methods: {
    get() {

      this.$refs['ruleForm'].validate((valid) => {
        if (valid) {
          this.ruleForm.username = this.$cookies.get('user_name');
          console.log(this.ruleForm.username+'/'+this.ruleForm.password+'/'+this.ruleForm.new_password)
          axios.post("http://101.34.248.53:8181/Map/forget", this.ruleForm).then(resp => {
            console.log(resp);
            if (resp.data.state == "NOT_password") {
              this.$message.warning("当前密码错误！")
            }
            if (resp.data.state == "OK") {
              this.$message.success("修改成功！")
            }
          })
        }
      })

    },
    addRoutes() {
      this.$router.push("/index");
    }
  }
}
</script>

<style scoped>
.login_page {
  width: 100%;
  height: 100%;
  background: url('../../assets/tea.png') ;
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
.form {
  margin-left: 60px;
  margin-top: 8px;
}

.btn1 {
  margin-left: 85px;
  margin-top: 5px;
}

.box-card {
  border-radius: 40px;
  margin: auto;
  /*margin-left: 700px;*/
  margin-top: 210px;
  /*left: 100%;*/
  /*top:100%;*/
  width: 550px;
  height: 435px;
}
.clearfix:before,
.clearfix:after {
  display: table;
  content: "";
}
</style>
