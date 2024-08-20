<template>
  <div>
    <el-card id="card_bg">
      <el-radio-group v-model="button_checked" size="small" style="margin-bottom: 10px"  @change="getData">
        <el-radio-button style="margin-left: 11px" v-model="button_checked" label="ben">本科志愿单</el-radio-button>
        <el-radio-button v-model="button_checked" label="zhuan">专科志愿单</el-radio-button>
        <el-button type="warning" id="clear" @click="Clear_All">重置志愿表</el-button>
      </el-radio-group>
      <el-button type="warning" id="id" @click="exportToExcel">导出志愿表</el-button>
      <div class="table_box">
        <el-table
            :data="Major_data"
            style="width: 100%"
            stripe
            border
        id="table_excel">
          <el-table-column label="志愿序号" width="150">
            <template slot-scope="scope">
              志愿{{ scope.$index+1 }}
            </template>
          </el-table-column>
          <el-table-column label="专业">
            <el-table-column prop="major_name" label="专业名称"></el-table-column>
            <el-table-column prop="major_id" label="专业代码"></el-table-column>
          </el-table-column>

          <el-table-column label="院校">
            <el-table-column prop="college_name" label="院校名称"></el-table-column>
            <el-table-column prop="college_id" label="院校代码"></el-table-column>
          </el-table-column>

          <el-table-column label="操作" width="200">

            <template slot-scope="scope">
              <el-button type="danger" style="color:#F56C6C;" @click="delData(scope.$index+1)">删除</el-button>
            </template>
            <br>
          </el-table-column>
        </el-table>
      </div>
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
    </el-card>
  </div>
</template>

<script>
import axios from 'axios'
import ExcelJS from 'exceljs';
export default {
  name: "Major_form",
  data(){
    return{
      button_checked:'ben',
      Major_data:[],
      mark:'',
      // 行数据
      row:'',
      user_name:'',
      whatMajor:'',
    }
  },
  methods:{
    // 初始化函数
    getData(){
      const loading = this.$loading({
        lock:true,
        text:'',
        spinner:'',
        background:'rgba(0, 0, 0, 0.7)',
      });
      axios({
        method:'GET',
        url:'api/students/gkorder',
        params:{
          action:'list_order',
          // account:'12345678',
          account:this.$cookies.get('user_name'),
          pagesize:10000,
          pagenum:1,
          major_set:this.button_checked==='ben'?'本科':'专科'
        }
      }).then((resp)=>{
        this.Major_data = resp.data.retlist;
        console.log(resp.data)
      })
      loading.close();
    },


    // 删除数据
    delData(id){
      this.$confirm(null,{
        title:'警告',
        type:'warning',
        message:"确定要删除吗？",
        confirmButtonText:'确定',
        cancelButtonText:'取消',
      }).then(()=>{
        axios({
          method:'DELETE',
          url:'api/students/gkorder',
          data:{
            action:'del_order',
            order_id:id,
            // account:'12345678',
            account:this.$cookies.get('user_name'),
            major_set:this.button_checked==='ben'?'本科':'专科'
          }
        }).then((resp)=>{
          if(resp.data.ret===0){
            this.$message.success('删除成功！');
            this.getData()
          }
        })

      }).catch((error)=>{
        console.log(error);
      })
    },

    Clear_All(){
      this.$confirm(null,{
        type:"warning",
        title:'警告',
        message:'是否要清空所有志愿？',
        confirmButtonText:'确定',
        cancelButtonText:'取消',
      }).then(()=>{
        axios({
          method:'DELETE',
          url:'api/students/gkorder',
          data:{
            action:'del_order_all',
            // account:'12345678',
            account:this.$cookies.get('user_name'),
            major_set:this.button_checked==='ben'?'本科':'专科'
          }
        }).then((resp)=>{
          if(resp.data.ret===0){
            this.$message.success('删除成功！');
            this.getData()
          }
        })
      })
    },
    exportToExcel() {
      // 创建一个新的Excel工作簿
      const workbook = new ExcelJS.Workbook();
      const worksheet = workbook.addWorksheet('志愿表');

      // 设置表头
      worksheet.columns = [
        { header: '志愿序号', key: 'index', width: 15 },
        { header: '专业名称', key: 'major_name', width: 30 },
        { header: '专业代码', key: 'major_id', width: 15 },
        { header: '院校名称', key: 'college_name', width: 30 },
        { header: '院校代码', key: 'college_id', width: 15 },
      ];

      // 添加数据行
      this.Major_data.forEach((item, index) => {
        const rowData = {
          index: index + 1,
          major_name: item.major_name,
          major_id: item.major_id,
          college_name: item.college_name,
          college_id: item.college_id,
        };
        worksheet.addRow(rowData);
      });

      // 创建一个Blob对象，将工作簿数据写入其中
      workbook.xlsx.writeBuffer().then((buffer) => {
        const blob = new Blob([buffer], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
        const url = window.URL.createObjectURL(blob);

        // 创建一个下载链接并触发点击事件
        const a = document.createElement('a');
        a.href = url;
        a.download = '志愿表.xlsx';
        a.click();

        // 释放URL对象
        window.URL.revokeObjectURL(url);
      });
    },

  },
  created() {
    this.getData();
  },
}
</script>

<style scoped>
.el-main{
  margin: 0;
  padding: 0;
}
.el-button{
  width: 80px;
  background-color: transparent;
  border-radius: 20px;
}

.el-button:focus,.el-button:hover{
  background-color: transparent;
  box-shadow: 0 2px 5px 0 rgba(0, 0, 0, 0.1);
}

#clear,#id{
  background-color: #f14343;
  border-radius: 5px;
  vertical-align: middle;
  position: absolute;
  right: 60px;
  width: 125px;
  text-align: center;
}
#id{
  margin-right: 180px;
}

#card_bg{
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.5);
}

.table_box{
  width: 80vw;
  margin: 0 auto;
}

.el-table >>> .cell{
  text-align: center!important;
}
</style>