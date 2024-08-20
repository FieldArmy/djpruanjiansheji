<template>
  <div>
    <el-card>
      <el-button type="primary" @click="dialogVisible = true">添加咨询师信息</el-button>
      <el-table :data="info.slice((currentPage-1)*pageSize,currentPage*pageSize)" stripe class="table_h">
        <el-table-column label="咨询师信息" align="center">
          <el-table-column prop="name" align="center" label="咨询师姓名" width="220" >
          </el-table-column>
          <el-table-column prop="sex" align="center" label="性别" width="220" ></el-table-column>
          <el-table-column prop="age" align="center" label="年龄" width="220" ></el-table-column>
          <el-table-column prop="phonenumber" align="center" label="联系电话" width="220"
                           autocomplete="off"></el-table-column>
          <el-table-column prop="major" align="center" label="擅长专业" width="220"
                           autocomplete="off"></el-table-column>
          <el-table-column prop="mail" align="center" label="注册邮箱" ></el-table-column>
          <el-table-column align="center" label="操作" class="table-h">
            <template slot-scope="scope">
              <el-button type="danger " @click="deleted(scope.row.account)">删除</el-button>
            </template>
          </el-table-column>
        </el-table-column>
      </el-table>
      <el-dialog title="添加咨询师信息" :visible.sync="dialogVisible" width="28%">
        <el-form ref="add_form" :model="ruleForm" :rules="rules" label-width="100px">
          <el-form-item label="用户名" prop="username">
            <el-input class="form" v-model="ruleForm.username" placeholder="请输入用户名"></el-input>
          </el-form-item>
          <el-form-item label="密码" prop="password">
            <el-input type="password" class="form" v-model="ruleForm.password" placeholder="请输入密码"
                      show-password></el-input>
          </el-form-item>
          <el-form-item label="确认密码" prop="checkPass">
            <el-input v-model="ruleForm.checkPass" class="form" placeholder="请再次输入密码" show-password></el-input>
          </el-form-item>
          <el-form-item label="姓名" prop="name">
            <el-input v-model="ruleForm.name" class="form" placeholder="请输入姓名" ></el-input>
          </el-form-item>
          <el-form-item label="性别" prop="sex">
            <el-input v-model="ruleForm.sex" class="form" placeholder="请输入性别" ></el-input>
          </el-form-item>
          <el-form-item label="电话号码" prop="phonenumber">
            <el-input v-model="ruleForm.phonenumber" class="form" placeholder="请输入电话号码"></el-input>
          </el-form-item>
          <el-form-item label="年龄" prop="age">
            <el-input v-model="ruleForm.age" class="form" placeholder="请输入年龄" ></el-input>
          </el-form-item>
          <el-form-item label="专业" prop="major">
            <el-input v-model="ruleForm.major" class="form" placeholder="请输入专业"></el-input>
          </el-form-item>

          <el-form-item label="个人简介" prop="text">
            <el-input v-model="ruleForm.text" class="form" placeholder="请输入个人简介" ></el-input>
          </el-form-item>
          <el-form-item label="个人邮箱" prop="email">
            <el-input v-model="ruleForm.email" class="form" placeholder="请输入个人邮箱"></el-input>
          </el-form-item>
          <el-form-item>
            <el-button type="success" style="margin-left: 1px;margin-top: 10px" @click="onSubmit('add_form')">添加
            </el-button>
            <el-button type="info" style="margin-left: 50px" @click="resetForm('add_form')">重置</el-button>
            <el-button type="info" style="margin-left: 50px" @click="dialogVisible = false">取消</el-button>
          </el-form-item>
        </el-form>
      </el-dialog>

      <div>
        <el-pagination
            :page-size.sync="pageSize"
            :page-sizes="pageSizes"
            :current-page.sync="currentPage"
            :pager-count="pageCount"
            background
            layout="sizes,prev, pager, next,jumper,->,total"
            style="margin-top: 6px"
            :total=total
        >
        </el-pagination>
      </div>
    </el-card>
  </div>
</template>

<script>
import axios from "axios"

export default {
  name: "Admain",
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
      dialogVisible: false,
      info: [],
      total: 0,
      ruleForm: {
        username: '',
        password: '',
        email: '',
        checkPass: "",
        name:'',
        sex:'',
        phonenumber:'',
        age:'',
        major:'',
        text:''
      },
      pageSize: 15,  //一页显示多少条
      pageSizes: [5, 10, 15, 20, 50],//每页显示多少条
      currentPage: 1,  //当前位于哪页
      pageCount: 7,   //多少分页按钮
      rules: {
        username: [
          {required: true, message: "账号不可为空", trigger: "blur"}
        ],
        password: [
          {required: true, message: "密码不可为空", trigger: "blur"}
        ],
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

      },
    }

  },
  methods: {
    resetForm(formName) {
      this.$refs[formName].resetFields();
    },
    onSubmit() {
      // console.log(this.ruleForm)
      const _this = this;
      this.$refs['add_form'].validate((valid) => {
        if (valid) {
            axios({
              method:'POST',
              url:'api/manager/addteacher',
              data:{
                action:'add_teacher',
                account:window.sessionStorage.getItem('user'),
                set_mag:'manager',
                tch_account:this.ruleForm.username,
                tch_password:this.ruleForm.password,
                name:this.ruleForm.name,
                sex:this.ruleForm.sex,
                mail:this.ruleForm.email,
                phonenumber: this.ruleForm.phonenumber,
                age:this.ruleForm.age,
                major: this.ruleForm.major,
                major_set:'本科',
                text:this.ruleForm.text
              }
            }).then((resp)=>{
              console.log(resp.data)
              if (resp.data.ret ===0) {
                _this.$message.success("添加成功！");
                this.get1();                //刷新
                this.dialogVisible = false  //关闭
              }else{
                _this.$message.error(resp.data.msg)
              }
            })

        } else {
          _this.$message.error("校验失败！")
        }
      })
    },
    get1() {
      axios({
        method:'POST',
        url:'api/manager/getteacher',
        data:{
          action:'get_teacher',
          account:window.sessionStorage.getItem('user'),
          set_mag:'manager',
        }
      }).then((resp)=>{
        // console.log(resp.data)
        this.total = resp.data.length;
        this.info = resp.data.data;
        console.log(this.info)
      })
    },
    deleted(id) {
      this.$confirm('此操作将永久删除该信息, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning',
        center: true
      }).then(() => {
        axios({
          method:'DELETE',
          url:'api/manager/delteacher',
          data:{
            action:'del_teacher',
            account:window.sessionStorage.getItem('user'),
            set_mag:'manager',
            account_teacher:id
          }
        }).then((resp)=>{
          if (resp.data.ret ===0) {
            console.log(resp.data)
            this.$message.success("删除成功！")
            this.get1();  //刷新
          }
        })
      }).catch(() => {
        this.$message.success('已取消删除');
      });
    },
  },
  created() {
    this.get1();
  }

}
</script>

<style scoped>
.form {
  /*width: 350px;*/
  width: 88%;
}
.el-card {
  margin-left: 20px;
  margin-top: 30px;
  /*width:1400px;*/
  /*height:800px;*/
}
.table_h{
  width: 100%;
  margin-top: 10px;
  font-size: 16px
}
</style>
