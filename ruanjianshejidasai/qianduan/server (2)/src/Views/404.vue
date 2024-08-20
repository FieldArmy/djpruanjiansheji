<!--<template>-->
<!--<div class="bg">-->
<!--&lt;!&ndash;  <el-empty description="您的页面走丢了"  :image-size="500">&ndash;&gt;-->
<!--&lt;!&ndash;&lt;!&ndash;    <h2>您的页面走丢了</h2>&ndash;&gt;&ndash;&gt;-->

<!--&lt;!&ndash;      <el-button  v-on:click="back" round icon="el-icon-refresh-right">点我返回</el-button>&ndash;&gt;-->

<!--&lt;!&ndash;  </el-empty>&ndash;&gt;-->
<!--<div style="color: #494949">.</div>-->
<!--  <span></span>-->
<!--  <div class="head404" style="margin-top: 50px"></div>-->

<!--  <div class="txtbg404">-->

<!--    <div class="txtbox" style="margin-top: 20px">-->

<!--      <p class="pp">对不起，您请求的页面不存在、或已被删除、或暂时不可用</p>-->

<!--      <p class="paddingbox">请点击以下链接继续浏览网页</p>-->
<!--      <div>-->
<!--&lt;!&ndash;      <el-button type="text" @click="get" class="color_1">> 返回网站首页</el-button>&ndash;&gt;-->
<!--      </div>-->
<!--      <el-button type="text" @click="back"  class="color_1">> 返回上一页面</el-button>-->
<!--    </div>-->

<!--  </div>-->
<!--</div>-->
<!--&lt;!&ndash;  <div>&ndash;&gt;-->
<!--&lt;!&ndash;    <el-button type="info" @click="get">返回网站首页</el-button>&ndash;&gt;-->
<!--&lt;!&ndash;  </div>&ndash;&gt;-->
<!--</template>-->

<!--<script>-->
<!--export default {-->
<!--  name: "404",-->
<!--  methods:{-->
<!--    back(){-->
<!--      this.$router.go(-1);//返回上一层-->
<!--    },-->
<!--    get(){-->
<!--      this.$router.push("/index")-->
<!--    }-->
<!--  },-->
<!--  // created() {-->
<!--  //   console.log(1111)-->
<!--  //   this.push()-->
<!--  // }-->
<!--}-->
<!--</script>-->

<!--<style scoped>-->
<!--.head404 {-->
<!--  width: 580px;-->
<!--  height: 234px;-->
<!--  /*margin: 50px auto 0 auto;*/-->
<!--  margin: auto;-->
<!--  background: url(https://www.daixiaorui.com/Public/images/head404.png) no-repeat;-->
<!--}-->
<!--.txtbg404 {-->
<!--  width: 499px;-->
<!--  height: 169px;-->
<!--  margin: 10px auto 0 auto;-->
<!--  background: url(https://www.daixiaorui.com/Public/images/txtbg404.png) no-repeat;-->
<!--}-->

<!--.txtbg404 .txtbox {-->
<!--  width: 390px;-->
<!--  position: relative;-->
<!--  top: 30px;-->
<!--  left: 60px;-->
<!--  color: #eee;-->
<!--  font-size: 13px;-->
<!--}-->

<!--.txtbg404 .txtbox p {-->
<!--  margin: 5px 0;-->
<!--  line-height: 18px;-->
<!--}-->

<!--.txtbg404 .txtbox .paddingbox {-->
<!--  padding-top: 10px;-->
<!--  font-size: 14px;-->
<!--}-->

<!--.txtbg404 .txtbox p a {-->
<!--  color: #eee;-->
<!--  text-decoration: none;-->
<!--}-->

<!--.txtbg404 .txtbox p a:hover {-->
<!--  color: #FC9D1D;-->
<!--  text-decoration: underline;-->
<!--}-->
<!--.bg{-->
<!--  margin: auto;-->
<!-- /*width:1800px;*/-->
<!-- /* height: 1000px;*/-->
<!--  height: 100vh;-->
<!--  background-color: #494949;-->
<!--}-->
<!--.color_1{-->
<!--  color: white;-->
<!--}-->
<!--.color_1:hover{-->
<!--  color: #ffd04b;-->
<!--}-->
<!--.pp{-->
<!--  font-size: 14px;-->
<!--}-->
<!--</style>-->
