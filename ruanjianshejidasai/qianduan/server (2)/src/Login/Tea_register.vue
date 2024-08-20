<template>
  <div class="login_page">
    <el-card class="box-card">
      <div slot="header" class="clearfix">
        <h2 class="login-title">咨询师注册</h2>
      </div>

      <div>
        <div class="user_logon_develop_ym">
          <el-form :model="ruleForm" status-icon :rules="rules" ref="ruleForm" label-width="100px">

            <el-form-item label=" 姓 名 : " prop="name">
              <el-input type="text" v-model="ruleForm.name" placeholder="请输入姓名" autocomplete="off"></el-input>
            </el-form-item>
            <el-form-item label=" 账 号 : " prop="name">
              <el-input type="text" v-model="ruleForm.username" placeholder="请输入账号" autocomplete="off"></el-input>
            </el-form-item>

            <el-form-item label=" 密 码 : " prop="name">
              <el-input type="text" v-model="ruleForm.password" placeholder="请输入密码" autocomplete="off"></el-input>
            </el-form-item>

            <el-form-item label=" 邮 箱 : " prop="email">
              <el-input type="text" v-model="ruleForm.email" placeholder="请输入邮箱"></el-input>
            </el-form-item>

            <el-form-item label=" 年龄 : " prop="age">
              <el-input type="text" v-model="ruleForm.age" placeholder="请输入年龄" autocomplete="off"></el-input>
            </el-form-item>

            <el-form-item label=" 联系电话 : " prop="tel">
              <el-input type="text" v-model="ruleForm.tel" placeholder="请输入电话" autocomplete="off"></el-input>
            </el-form-item>
            <div>
              <el-button type="text" style="margin-top: -10px;margin-left: 54px" class="text">性别：</el-button>
              <el-radio-group v-model="ruleForm.sex" size="medium">
                <el-radio-button label="男"></el-radio-button>
                <el-radio-button label="女"></el-radio-button>
              </el-radio-group>
            </div>
            <el-button type="text" style="margin-top: 15px;margin-left: 26px" class="text">擅长专业：</el-button>
            <el-cascader
                style="margin-left: 0px"
                placeholder="选择您擅长的专业"
                :options="options1"
                v-model="ruleForm.major"
                clearable
                collapse-tags
                :props="{ checkStrictly: true ,expandTrigger: 'hover' }"
            >
            </el-cascader>
            <div>
              <el-button type="text" style="margin-top: 15px;margin-left: 26px" class="text">个人简介：</el-button>
              <el-input
                  type="textarea"
                  :rows="4"
                  placeholder="请输入内容"
                  v-model="ruleForm.info"
                  maxlength="100"
                  class="form"
                  show-word-limit>
              </el-input>
            </div>
            <el-form-item>
              <el-button type="primary" style="margin-left: 20px;margin-top: 30px" @click="addform()">注册</el-button>
<!--              <el-button style="margin-left: 30px" @click="resetForm('ruleForm')">重置</el-button>-->
              <el-button style="margin-left: 30px" @click="cost_log()">重置</el-button>
              <el-button style="margin-left: 30px" @click="addtest()">返回</el-button>
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

    const name = (rule, value, callback) => {
      if (!value) {
        return callback(new Error('用户名不能为空!'));
      }
    };
    const age = (rule, value, callback) => {
      if (!value) {
        return callback(new Error('年龄不能为空!'));
      }
    };
    // const tel = (rule, value, callback) => {
    //   if (!value) {
    //     return callback(new Error('电话不能为空!'));
    //   }
    // };
    const tel = (rule, value, callback) => {
      if (!value) {
        return callback(new Error('电话不能为空!'));
      } else if (value && (!(/^[1][345789]\d{9}$/).test(value) || !(/^[1-9]\d*$/).test(value) || value.length !== 11)) {
        callback(new Error('手机号码不符合规范'))
      } else {
        callback()
      }
    }
    const email = (rule, value, callback) => {
      const mailReg = /^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+(.[a-zA-Z0-9_-])+/
      if (!value) {
        return callback(new Error('邮箱不能为空'))
      }
      setTimeout(() => {
        if (mailReg.test(value)) {
          callback()
        } else {
          callback(new Error('请输入正确的邮箱格式'))
        }
      }, 100)
    };
    const validatePass = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请输入密码'));
      } else {
        if (this.ruleForm.password !== '') {
          this.$refs.ruleForm.validateField('password');
        }
        callback();
      }
    };
    const validatePass2 = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请再次输入密码'));
      } else if (value !== this.ruleForm.password) {
        callback(new Error('两次输入密码不一致!'));
      } else {
        callback();
      }
    };
    return {
      ruleForm: {
        info: "",
        name: '',
        email: '',
        age: '',
        major: "",
        tel: '',
        key: "",
        sex: "",
        username:"",
        password: "",
        checkPass: "",
      },
      rules: {
        name: [
          {validator: name, trigger: 'blur'}
        ],
        age: [
          {validator: age, trigger: 'blur'}
        ],
        tel: [
          {validator: tel, trigger: 'blur'}
        ],
        email: [
          {validator: email, trigger: 'blur'}
        ],
        password: [
          {validator: validatePass, trigger: 'blur'}
        ],
        checkPass: [
          {validator: validatePass2, trigger: 'blur'}
        ],
      },
      options1: [
        {
          value: '本科', label: '本科',
          children: [
            {value: '哲学', label: '哲学',},
            {value: '经济学', label: '经济学',},
            {value: '法学', label: '法学',},
            {value: '教育学', label: '教育学',},
            {value: '文学', label: '文学',},
            {value: '历史学', label: '历史学',},
            {value: '理学', label: '理学',},
            {value: '工学', label: '工学',},
            {value: '农学', label: '农学',},
            {value: '管理学', label: '管理学',},
            {value: '艺术学', label: '艺术学',},
          ]
        },
        {
          value: '专科', label: '专科',
          children: [
            {value: '农林牧渔', label: '农林牧渔大类',},
            {value: '资源环境与安全', label: '资源环境与安全大类',},
            {value: '能源动力与材料', label: '能源动力与材料大类',},
            {value: '土木建筑', label: '土木建筑大类',},
            {value: '水利大类', label: '水利大类大类',},
            {value: '装备制造', label: '装备制造大类',},
            {value: '生物与化工', label: '生物与化工大类',},
            {value: '食品药品与粮食', label: '食品药品与粮食大类',},
            {value: '轻工纺织', label: '轻工纺织大类',},
            {value: '交通运输', label: '交通运输大类',},
          ]
        }

      ],
    };
  },
  methods: {
    addform() {
      if (this.ruleForm.name != '' && this.ruleForm.email != '' && this.ruleForm.info != '' && this.ruleForm.age != ''
          && this.ruleForm.sex != '' && this.ruleForm.tel != ''&& this.ruleForm.password != '' && this.ruleForm.major != '') {
        console.log(this.ruleForm);
        axios.get('http://101.34.248.53:8181//Map/teacher/add/' + this.ruleForm.name + '/' + this.ruleForm.username+ '/' + this.ruleForm.password+ '/' + this.ruleForm.sex + '/'
            + this.ruleForm.age + '/' + this.ruleForm.tel + '/' + this.ruleForm.major + '/' + this.ruleForm.email + '/' + this.ruleForm.info).then(resp => {
          // axios.post('http://101.34.248.53:8181//Map/teacher/add',this.ruleForm).then(resp=>{
          console.log(resp.data);
          if (resp.data == "OK") {this.$message.success("注册成功！");}
          if (resp.data == "Repeat_Username") {this.$message.error("用户名重复！");}
          if (resp.data == "Repeat_Email") {this.$message.error("邮箱重复！");}

        })
      } else {
        this.$message.error("请完成输入！")
      }
    },
    addtest() {
      this.$router.push('/')
    },

    resetForm(formName) {
      this.$refs[formName].resetFields();
    },
    cost_log(){
      this.ruleForm.name = ""
      this.ruleForm.email = ""
      this.ruleForm.info = ""
      this.ruleForm.age = ""
      this.ruleForm.sex = ""
      this.ruleForm.tel = ""
      this.ruleForm.major =""
    },
    get22() {
      this.ruleForm.major = "";
    }
  }
}
</script>
<style scoped>
.login_page {
  width: 100%;
  height:100%;
  background: url(https://pic.imgdb.cn/item/613a140244eaada73973b202.jpg) ;
  background-size: cover;
  background-attachment: fixed!important;
  position: fixed;
  overflow-y: scroll;
}

.user_logon_develop_ym {
  width: 500px;
  margin: auto;
}

.box-card {
  border-radius: 40px;
  margin: auto;
  /*margin-left: 580px;*/
  margin-top: 100px;
  width: 950px;
  height: 800px;
}

.text {
  color: #000000;
}
.text:hover{
  color: #000000;
}

.login-title {
  text-align: center;
  margin: 0 auto 10px auto;
  margin-top: 10px;
  color: #303133;
}

.form {
  width: 400px;
  margin-top: 20px;
}
.clearfix:before,
.clearfix:after {
  display: table;
  content: "";
}
</style>

