<template>
  <div>
    <el-card class="el-card">
      <el-table :data="info.slice((currentPage-1)*pageSize,currentPage*pageSize)" stripe class="table_h">
        <el-table-column align="center" label="用户信息">
          <el-table-column prop="account" align="center" label="用户名" width="230"></el-table-column>
          <el-table-column prop="mail" align="center" label="注册邮箱"></el-table-column>
          <el-table-column prop="level" align="center" label="权限">
            <template>
              <span>用户</span>
            </template>
          </el-table-column>

          <el-table-column align="center" label="操作">
            <template slot-scope="scope">
              <el-button type="danger " @click="deleted(scope.row.account)">删除</el-button>
            </template>
          </el-table-column>

        </el-table-column>
      </el-table>
      <!--添加信息-->
      <div>
        <el-pagination
            :page-size.sync="pageSize"
            :page-sizes="pageSizes"
            :current-page.sync="currentPage"
            :pager-count="pageCount"
            background
            style="margin-top: 6px"
            layout="sizes,prev, pager, next,jumper,->,total"
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
      ruleForm: {
        username: '',
        password: '',
        email: '',
        time: "",
        checkPass: "",
        level: "",
      },
      total: 0,
      pageSize: 10,  //一页显示多少条
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
    // 添加用户
    onSubmit() {
      // console.log(this.ruleForm)
      const _this = this;
      this.$refs['add_form'].validate((valid) => {
        if (valid) {
          axios.post('http://101.34.248.53:8181/Map/add', this.ruleForm).then(resp => {
            // console.log(this.ruleForm);
            // console.log(resp.data)

            if (resp.data == "Success") {
              _this.$message.success("添加成功！");
              this.get1();                //刷新
              this.dialogVisible = false  //关闭
            }
            if (resp.data == "Repeat") {
              _this.$message.error("该用户名已存在！");
            }
            if (resp.data == "Repeat_Email") {
              _this.$message("该邮箱已存在！");
            }
            if (resp.data == "Error") {
              _this.$message("错误！");
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
        url:'api/manager/getuser ',
        data:{
          action:'get_user',
          account:window.sessionStorage.getItem('user'),
          set_mag:'manager'
        }
      }).then((resp)=>{
        console.log(resp.data.data)
        this.info = resp.data.data;
        this.total = resp.data.length;
      })
    },

    // 删除用户账号
    deleted(id) {
      this.$confirm('此操作将永久删除该信息, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning',
        center: true
      }).then(() => {
        axios({
          method:'DELETE',
          url:'api/manager/deluser',
          data:{
            action:'del_user',
            account:window.sessionStorage.getItem('user'),
            set_mag:'manager',
            account_user:id
          }
        }).then((resp)=>{
          if(resp.data.ret===0){
            this.$message.success("删除成功！")
            this.get1();  //刷新
          }
        })
      }).catch(()=>{this.$message('取消成功')})
    },

    resetForm(formName) {
      this.$refs[formName].resetFields();
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

.font {
  font-size: 16px;
  font-style: italic;
  color: #fa9696;
  margin-left: 20px;
}

.el-card {
  margin-left: 20px;
  margin-top: 30px;
  /*width:1300px;*/
  /*height:800px;*/
}

.table_h {
  width: 100%;
  margin-top: 10px;
  font-size: 16px
}
</style>
