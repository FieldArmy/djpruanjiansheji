<template>
  <div id="box">
    <div style="margin-top: 10px">
      <el-breadcrumb separator="/">
        <el-breadcrumb-item :to="{ path: '/index' }">首页</el-breadcrumb-item>
        <el-breadcrumb-item>内容详情</el-breadcrumb-item>
      </el-breadcrumb>
    </div>
      <div class="box">
          <h1>山东省2023年艺术本科批统考</h1>
          <span id="txt-from">稿件来源：中国教育在线</span>
          <el-divider></el-divider>
          <div id="txt-body">
              <a href="https://www.sdzk.cn/Floadup/file/20230717/6382521311467550833989416.xls">山东省2023年艺术本科批统考美术类第1次志愿投档情况表</a>
          </div>
          <el-divider></el-divider>
      </div>
  </div>
</template>

<script>
export default {
  name: "Web-1",
  data () {
    // return {
    //   imgSrc: logo
    // };
  }
}
</script>

<style scoped>
#box{
    width: 1200px;
    margin: 0 auto;
    padding: 10px;
}

.box {
    box-sizing: border-box;
    padding: 0 10px;
    background-color: white;
    border-radius: 10px;
}

#bread-box{
  padding-top: 10px;
  padding-left: 5px;
}

h1{
  font-size: 20px;
  font-weight: 700;
  text-align: center;
}

#txt-from{
  font-size: 14px;
}

#txt-body{
  width: 100%;
  margin: 0;
  padding: 0;
  /*border: 1px solid red;*/
}

img{
  display: block;
  margin: 0 auto;
}
</style>
