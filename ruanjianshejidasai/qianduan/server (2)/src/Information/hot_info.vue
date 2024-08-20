<template>
<div id="image-box">
  <el-card class="hot">
  <iframe style="width: 1000px;height: 800px" src="https://maplab.amap.com/share/mapv/4bd5162b5ab6a80d8b38798297801011"></iframe>
  </el-card>
</div>
</template>

<script>
export default {
  name: "hot_info"
}
</script>

<style scoped>
#image-box {
  align-content: center;
  /*margin: 0 auto;*/
  /*margin-top: 30px;*/
  padding: 20px 0;
}
.hot{
  margin: auto;
  width: 1050px;
  height: 850px;
}
</style>