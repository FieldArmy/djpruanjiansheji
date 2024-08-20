<template>
  <div class="bg">

    <el-container v-if="info">
      <el-button id="go_1" type="text" @click="go_1">>上一页</el-button>
      <el-header height="auto">
        <div id="box">

          <!-- logo区域 -->
          <div id="logo-box">
            <img :src="'http://101.34.248.53:8181/Map/list/school_logo/' + info.school_name" id="logo">
          </div>

          <!-- 主体区域 -->
          <div id="msg">
            <div id="msg-title" style="color: white">{{ info.school_name }}</div>

            <!-- 学校详细信息 -->
            <div id="ifm">
              <div>
                <i class="el-icon-location-outline" style="color: white"></i>
                <span style="color: white">{{ info.school_chengshi }}</span>
              </div>
              <div id="address">
                <i class="el-icon-eleme" style="color: white"></i> <span style="color: white">官方网址</span> &nbsp;
                <span style="color: white">{{ info.school_url }}</span>
              </div>
              <div id="call">
                <i class="el-icon-phone" style="color: white"></i>
                <span style="color: white"> 官方电话</span> &nbsp;
                <span style="color: white"> {{ info.school_dianhua }} </span>
              </div>
              <div id="emi">
                <i class="el-icon-message" style="color: white"></i>
                <span style="color: white"> 电子邮箱</span> &nbsp;
                <span style="color: white"> {{ info.school_email }} </span>
              </div>
            </div>
          </div>

          <!-- 标签 -->
          <div id="tag-pos">
            <span v-for="item in arr" :key="item" class="tag">{{ item }}</span>
          </div>

        </div>
      </el-header>

      <!-- 用于切换页面操作 -->
      <el-main style="padding:5px 20px">
        <el-tabs v-model="activeName" type="border-card">
          <el-tab-pane
              v-for="(num,index) in items"
              :key="index"
              :label="num.name"
              :name="num.id">
            <router-view :name="num.ctm"></router-view>
          </el-tab-pane>
        </el-tabs>
      </el-main>

    </el-container>
  </div>
</template>

<script>

export default {
  name: "Main",
  data() {
    return {
      activeName: '1',
      info: null,
      arr: [],
      number: null,
      items: [
        {
          id: '1',
          name: '学校概况',
          ctm: 'ino'
        },
        {
          id: '2',
          name: '历年分数',
          ctm: 'scl'
        }
      ]
    };
  },
  methods:{
    go_1(){
      this.$router.go(-1)
    }
  },
  created() {
    this.number = this.$route.query.id;

    this.axios.get('http://101.34.248.53:8181/Map/list/byid_one/' + this.number)
        .then(resp => {
          this.info = resp.data;
          this.arr = resp.data.school_type_cc;
          this.arr = this.arr.split(' ');
        });
  }
}
</script>

<style scoped>
.el-container {
  width: 1200px;
  margin: auto;
}

.el-header {
  width: 1200px;
}

/*整体的大盒子*/
#box {
  display: flex;
  justify-self: center;
  align-items: center;
  height: 200px;
  /*background-color: #0093E9;*/
  /*background-image: url('./assets/bg_best.png');*/
  /*background-image: url('../Views/assets/bg_best.png');*/
  background-image: url('./assets/bg_best.png');
  background-repeat: no-repeat;
  font-size: 15px;
  padding: 20px;
  position: relative;
}

/*logo盒子*/
#logo-box {
  width: 150px;
  height: 150px;
  margin-top: 25px;
  background-color: white;
  border-radius: 10px;
  display: flex;
  justify-content: center;
  align-items: center;
}

/*logo设置*/
#logo {

  width: 120px;
  height: 120px;
}

/*主体盒子，不包含标签*/
#msg {
  padding: 15px;
  /*width: 700px;*/
  height: 200px;
  font-size: 14px;
  line-height: 2.0;
}

/*学校大标题*/
#msg-title {
  font-size: 30px;
  font-weight: 700;
  text-align: center;
}

/*标签的盒子*/
#tag-pos {
  width: 500px;
  position: absolute;
  right: -60px;
}

/*学校标签*/
.tag {
  margin: 5px;
  padding: 5px;
  display: inline-block;
  width: 30%;
  height: 20px;
  font-size: 14px;
  color: white;
  border: 1px solid white;
  border-radius: 30px;
  text-align: center;
  line-height: 20px;
}

/*标签的触碰动作*/
.tag:hover {
  border-color: yellow;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1)
}

/*主体部分*/
.el-main {
  margin: 0;
  width: 1200px;
}

/*.bg {*/
/*  background-color: #defcfc;*/
/*}*/
/*.go_1{*/
/*  position: absolute;*/
/*  !*top: 0px;*!*/
/*  right: 1590px;*/
/*}*/
#go_1{
  width: 200px;
  /*border: 1px solid red;*/
  margin: 0 20px;
  color: black;
  font-size: 15px;
  text-align: left;
}
.go_1{
  margin-left: 200px;
  color: black;
  font-size: 15px;
}
.go_1:hover{
  margin-left: 200px;
  /*margin: 0;*/
  color: black;
  font-size: 15px;
}
</style>
