<template>
  <div>
    <el-card>
      <el-button type="primary" @click="get_opinion">刷新</el-button>
      <el-table :data="info.slice((currentPage-1)*pageSize,currentPage*pageSize)" stripe class="table_h">
        <el-table-column label="用户反馈" align="center">
        <el-table-column prop="students_account" align="center" label="用户姓名" width="330px"></el-table-column>
        <el-table-column prop="issue" align="center" label="反馈内容"></el-table-column>
        <el-table-column prop="time" align="center" label="反馈时间" width="330px"></el-table-column>
        </el-table-column>
      </el-table>
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
    </el-card>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "useropinion",
  data() {
    return {
      total: 0,
      pageSize: 10,  //一页显示多少条
      pageSizes: [5, 10, 15, 20, 50],//每页显示多少条
      currentPage: 1,  //当前位于哪页
      pageCount: 7,   //多少分页按钮
      info: {},
    }
  },
  methods: {
    get_opinion() {
      axios({
        method:'POST',
        url:'api/manager/getissue',
        data:{
          account:window.sessionStorage.getItem('user'),
          action:'get_issue'
        }
      }).then((resp)=>{
        console.log(resp.data)
        this.info = resp.data.data;
        this.total = resp.data.length;
      })
    }
  },
  created() {
    this.get_opinion();
  }
}
</script>

<style scoped>
.el-card {
  margin-left: 20px;
  margin-top: 30px;
  /*width:1300px;*/
  /*height:800px;*/
}
.table_h{
  width: 100%;
  margin-top: 10px;
  font-size: 16px
}
</style>
