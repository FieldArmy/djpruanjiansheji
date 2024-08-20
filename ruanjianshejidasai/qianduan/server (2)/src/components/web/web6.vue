<template>
  <div id="box">
    <div style="margin-top: 10px">
      <el-breadcrumb separator="/">
        <el-breadcrumb-item :to="{ path: '/index' }">首页</el-breadcrumb-item>
        <el-breadcrumb-item>内容详情</el-breadcrumb-item>
      </el-breadcrumb>
    </div>
      <div class="box">
          <h1>山东：2023高考录取情况公告</h1>
          <span id="txt-from">稿件来源：中国教育在线</span>
          <el-divider></el-divider>
          <div id="txt-body">
            <span>
                <a href="https://www.sdzk.cn/Floadup/file/20230719/6382538122655052185031609.xls">山东2023年普通类常规批第1次志愿投档情况表(点击下载投档情况表)</a>
            </span>
          </div>
          <el-divider></el-divider>
      </div>
  </div>
</template>

<script>
export default {
  name: "Web-1"
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

#txt-from{
  font-size: 14px;
}

h1{
  font-weight: 400;
  text-align: center;
}

#txt-body{
  width: 1000px;
  margin: auto;
  padding: 0;
  /*border: 1px solid red;*/
  text-align: center;
}
</style>
