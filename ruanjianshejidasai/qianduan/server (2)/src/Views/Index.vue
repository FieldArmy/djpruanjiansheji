<template>
  <div>
    <div id="Main-box">
      <div id="block">
        <el-carousel
            height="460px"
            :interval="3500">
          <el-carousel-item v-for="item in images" :key="item.name">
            <img :src="item.url" alt="志高考">
          </el-carousel-item>
        </el-carousel>
      </div>

      <div id="all-body" style="background-color: #ffffff">
        <div id="inform-box">
          <div id="inform-top">
            <span id="im-tuchu">头条</span>
            <span id="im-title">山东：四六级成绩今天出成绩啦！！</span>
          </div>
          <div id="inform-body">
            <div id="im-body-1">
              <router-link to="/web1" class="im-text">山东：2023年艺术类本科批统考第3次志愿院校专业计划</router-link>
              <router-link to="/web2" class="im-text">山东：山东省2023年体育类常规批（本科）第2次志愿院校专业计划</router-link>
              <router-link to="/web3" class="im-text">山东：2023年普通高校招生录取结果查询时间</router-link>
            </div>
            <div id="im-body-2">
              <router-link to="/web4" class="im-text">山东：山东省2023年春季高考本科批第1次志愿投档情况表</router-link>
              <router-link to="/web5" class="im-text">山东：2023年艺术统考批第1次志愿投档情况表</router-link>
              <router-link to="/web6" class="im-text">山东：2023年普通类常规批第1次志愿投档情况表</router-link>
            </div>
          </div>
        </div>
      </div>
      <div id="image-box">
<!--        <img src="../assets/image_3.png" id="image-time">-->
        <el-button type="text" class="photo">全国高校分布图</el-button>
        <el-card style="height: 800px;width: 1200px">
        <iframe class="fk" src="http://api.map.baidu.com/lbsapi/getpoint/index.html"></iframe>
        </el-card>
      </div>
    </div>

  </div>
</template>

<script>
export default {
  name: "Main",
  data() {
    return {
      images: [
        {
          name: 'first',
          url: require("@/assets/first.png")
        },
        {
          name: 'second',
          url: require("@/assets/second.png")
        },
        {
          name: 'third',
          url: require("@/assets/third.png")
        },
        {
          name: 'four',
          url: require("@/assets/four.png")
        }
      ]
    }
  }
}
</script>

<style scoped>
#Main-box {
  overflow: hidden; /* 防止第二个滚动条*/
  margin: auto;
  padding: 0;
  width: 1200px;
  height: 1800px;
}
#image-box {
  align-content: center;
  /*margin: 0 auto;*/
  margin-top: 30px;
  padding: 20px 0;
}
.fk{
  margin-left: -15px;
  margin-top: -15px;
  width: 1185px;
  height: 790px;
}
.photo{
  font-size: 23px;
  color:black;
  margin-left: 20px;
  font-weight: bold;
}
.photo:hover{
  font-size: 23px;
  color:black;
  margin-left: 20px;
  font-weight: bold;
}
#block {
  width: 1200px;
  height: 370px;
}

img {
  width: 1200px;
  height: 370px;
}

#all-body {
  margin-top: 15px;
  /*width: 800px;*/
}

#inform-box {
  padding: 20px;
  /*border: 1px solid black;*/
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
  position: relative;
}

#im-tuchu {
  display: inline-block;
  width: 65px;
  height: 30px;
  background-color: red;
  color: white;
  font-weight: 700;
  line-height: 30px;
  text-align: center;
}

#im-title {
  font-size: 20px;
  font-weight: 700;
  margin-left: 15px;
}

#im-body-1, #im-body-2 {
  padding: 10px;
  /*width: 350px;*/
  height: 130px;
  /*border: 1px solid red;*/
}

#im-body-2 {
  position: absolute;
  top: 51px;
  right: 20px;
}

a {
  display: block;
  margin: 0;
  padding: 10px;
  text-decoration: none;
  color: #333;

  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  /*border: 1px solid blue;*/
}

a:hover {
  color: red;
}
#image-time {
  height: 1000px;
  margin: auto;
  box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04);
}

#police {
    width: 95%;
    padding: 20px;
    margin: 0 auto;
    /*height: 200px;*/
    background-color: white;
    text-align: center;
    color: #333;
}
</style>
