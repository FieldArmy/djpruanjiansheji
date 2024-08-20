<template>
  <div>
    <div id="box" ref="wid">
<!--      <el-breadcrumb separator-class="el-icon-arrow-right">-->
<!--        <el-breadcrumb-item :to="{ path: '/checkmajor' }">查专业</el-breadcrumb-item>-->
<!--        <el-breadcrumb-item>{{ nodes.lv1_name }}</el-breadcrumb-item>-->
<!--        <el-breadcrumb-item>{{ nodes.lv2_name }}</el-breadcrumb-item>-->
<!--      </el-breadcrumb>-->
      <el-button id="go_1" type="text" @click="go_1">>上一页</el-button>
      <div class="top">
        <span id="tit" >{{ nodes.name }}</span>
        <el-divider></el-divider>
        <el-descriptions :column="2">
          <el-descriptions-item label="学校类型">
            <!--            <el-tag size="small" v-text="choose(nodes.cc)?'本科':'专科'"></el-tag>-->
            <el-descriptions style="margin-top: -10px;margin-left: 1px"
                             v-text="choose(nodes.cc)?'本科':'专科'"></el-descriptions>
          </el-descriptions-item>
          <el-descriptions-item label="专业代码"> {{ nodes.major_code }}</el-descriptions-item>
          <el-descriptions-item label="修业年限"> {{ nodes.major_year }}</el-descriptions-item>
          <el-descriptions-item label="授予学位"> {{ nodes.degree }}</el-descriptions-item>
        </el-descriptions>
      </div>
      <span id="major-title" class="box"><strong>专业简介</strong></span>
      <div id="major">
        <el-collapse v-model="activeNames">
          <el-collapse-item name="1">
            <template slot="title"><span class="box">是什么</span></template>
            <div class="major-text" style="text-indent:1.5em">  {{ nodes.is_what }}</div>
          </el-collapse-item>
          <el-collapse-item name="2">
            <template slot="title" ><span class="box">学什么</span></template>
            <div class="major-text" style="text-indent:1.5em">{{ nodes.is_learn }}</div>
          </el-collapse-item>
          <el-collapse-item name="3">
            <template slot="title"><span class="box">干什么</span></template>
            <div class="major-text" style="text-indent:1.5em">{{ nodes.is_do }}</div>
          </el-collapse-item>
        </el-collapse>
      </div>
      <div id="xk-box" class="shadow">
        <span id="xktit" class="box">选考学科建议：</span><br>
        <span><strong style="margin-left: 5px">3+3省份</strong></span>
        <div style="margin-left: 5px">{{ nodes.xvanke }}</div>
      </div>

      <div id="box-all">
        <div id="sex" class="shadow">
          <div class="box">男女比例：</div>
          <div>
            <div id="main"></div>
          </div>
        </div>
        <div id="object" class="shadow">
          <span class="box">考研方向</span>
          <p style="text-indent:1.5em">{{ nodes.kaoyan }}</p>
          <span class="box">开设课程</span>
          <p style="text-indent:1.5em">{{ nodes.kecheng }}</p>
          <span class="box">社会名人</span>
          <p style="text-indent:1.5em">{{ nodes.mingren }}</p>
        </div>
      </div>
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
  </div>
</template>

<script>

export default {
  name: "Main",
  data() {
    return {
      activeNames: '1',
      nodes: '',
      number: null,
      child_num: null
    }
  },

  created() {
    this.get_data();
  },

  methods: {
    // 获取手机型号
    isMobile(){
      let flag = navigator.userAgent.match(/(phone|pad|pod|iPhone|iPod|ios|iPad|Android|Mobile|BlackBerry|IEMobile|MQQBrowser|JUC|Fennec|wOSBrowser|BrowserNG|WebOS|Symbian|Windows Phone)/i);
      return flag;
    },

    addCss(){
      if(this.isMobile()){
        this.$refs.wid.style.width = '90vw';
      }else {
        this.$refs.wid.style.width = '800px';
      }
    },

    get_data() {
      this.number = this.$route.query.id
          this.axios.get('http://101.34.248.53:8181/Map/major/id/' + this.number)
              .then(resp => {
                this.nodes = resp.data;
                this.child_num = resp.data.boy;
                this.drawData(this.child_num);

                this.addCss();
              }).catch(error => {
            console.log(error)
          });
    },

    choose: function (item) {
      if (item == 1) {
        return true;
      } else {
        return false;
      }
    },
    go_1(){
      this.$router.go(-1)
    },
    drawData(num) {
      let myChart = this.$echarts.init(document.getElementById('main'));
      myChart.setOption({
        tooltip: {
          trigger: 'item'
        },
        legend: {
          left: 'center',
        },
        series: [
          {
            type: 'pie',
            radius: '50%',
            data: [
              {value: num, name: '男生'},
              {value: 100 - num, name: '女生'},
            ],
            label: {
              position: 'inside',
            },
            emphasis: {
              itemStyle: {
                shadowBlur: 5,
                shadowOffsetX: 0,
                shadowColor: 'rgba(0, 0, 0, 0.5)'
              }
            }
          }
        ]
      })
    }
  }
}
</script>

<style scoped>
#box {
  /*  width: 90vw;*/
  /*width: 800px;*/
  height: 1500px;
  margin: 0 auto;
  padding: 0;
}

.el-breadcrumb {
  margin: 10px;
}

.top {
  text-align: center;
  box-shadow: 0 3px 12px 0 rgba(0, 0, 0, 0.2);
  background-color: white;
}

.el-descriptions {
  margin: 10px;
  padding: 10px 0;
}

img {
  width: 35px;
  height: 35px;
}

p {
  margin: 0;
  padding: 0;
}

#major-title {
  font-size: 20px;
}

#tit {
  text-align: left;
  font-size: 30px;
}

#major {
  box-shadow: 0 3px 12px 0 rgba(0, 0, 0, 0.1);
  border-radius: 2px;
}

.major-text {
  font-size: 16px;
  padding: 10px 0 0 5px;
}

#xk-box {
  background-color: white;
  height: 200px;
  margin-top: 10px;
}

#xktit {
  font-size: 20px;
  font-weight: 700;
  line-height: 70px;
}

#box-all {
  position: relative;
}

.box {
  /*font-weight:bolder;*/
  font:  20px "华文中宋";
  /*font-size: 16px;*/
  height: 30px;
  border-width: 0 0 0 4px;
  border-style: solid;
  border-color: red;
  padding: 0 5px;
  line-height: 35px;
  text-align: left;
}
#go_1{
  width: 200px;
  /*border: 1px solid red;*/
  margin: 0 5px;
  color: black;
  font-size: 15px;
  text-align: left;
}
.shadow {
  border: 0 solid transparent;
  box-shadow: 0 3px 12px 0 rgba(0, 0, 0, 0.2);
}

.shadow:hover {
  /*box-shadow: 0 3px 12px 0 rgba(0, 0, 0, 0.1);*/
}

#sex {
  background-color: white;
  margin-top: 10px;
  height: 250px;
  /*border: 1px solid red;*/
  text-align: center;
}

#boy, #girl {
  display: inline-block;
  margin: 0;
  padding: 0;
  width: 170px;
  position: relative;
  top: -10px;
}

#main {
  width: 250px;
  height: 250px;
  margin: 0 auto;
}

#baifen-boy {
  position: absolute;
  left: 120px;
  top: -10px;
}

#baifen-girl {
  position: absolute;
  left: 15px;
  top: -10px;

}

#object {
  background-color: white;
  height: 100%;
  line-height: 30px;
  margin-top: 10px;
}
</style>
