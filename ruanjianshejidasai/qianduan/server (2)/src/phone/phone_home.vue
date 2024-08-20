<template>
    <div>
        <div id="Main-box">
            <div id="block">
                <el-carousel
                    height="25vh"
                    :interval="3500">
                    <el-carousel-item v-for="item in images" :key="item.name">
                        <img :src="item.url">
                    </el-carousel-item>
                </el-carousel>
            </div>

            <div id="text-box">
                <div class="text-title">
                    今日头条
                </div>
                <div class="inner-box">
                    <div class="text">
                        <router-link to="/web_4">
                            山东：普通类和体育类常规批、艺术类专科批和春季高考专科批志愿填报注意事项
                        </router-link>
                    </div>
                    <div class="text">
                        <router-link to="/web_5">
                            山东：2021年艺术统考批第1次志愿投档情况表
                        </router-link>
                    </div>
                    <div class="text">
                        <router-link to="/web_6">
                            山东：2021年普通类常规批第1次志愿投档情况表
                        </router-link>
                    </div>
                </div>
                <br>
                <div class="text-title">
                    猜你喜欢
                </div>
                <div class="inner-box">
                    <div class="text">
                        <router-link to="/web_1">
                            山东：2021高考录取情况公告
                        </router-link>
                    </div>
                    <div class="text">
                        <router-link to="/web_2">
                            山东：艺术类本科批、春季高考本科批第2次志愿填报注意事项
                        </router-link>
                    </div>
                    <div class="text">
                        <router-link to="/web_3">
                            山东：2021年普通高校招生录取结果查询时间
                        </router-link>
                    </div>
                </div>
                <br>
                <div class="text-title">
                    专业热度
                </div>
                <div id="chart"></div>
            </div>

        </div>

    </div>
</template>

<script>
export default {
    name: "Home",
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
    },
    methods:{
        draw_chart(){
            let myChart = this.$echarts.init(document.getElementById('chart'));
            myChart.setOption({
                tooltip: {
                    trigger: 'item'
                },
                legend: {
                    orient: 'horizontal',
                    left: 'center'
                },
                series: [
                    {
                        name: '专业',
                        type: 'pie',
                        radius: '70%',
                        minAngel: 30,
                        data: [
                          { value: 1012, name: '财经' },
                          { value: 625, name: '工商' },
                          { value: 530, name: '计算机科学与技术' },
                          { value: 484, name: '土木工程' },
                          { value: 360, name: '医学' },
                          { value: 230, name: '机械制造' },
                          { value: 210, name: '文学' },
                          { value: 180, name: '建筑' },
                          { value: 130, name: '土木工程' },
                        ],
                        label:{
                            show:false,
                        },
                        emphasis: {
                            itemStyle: {
                                shadowBlur: 10,
                                shadowOffsetX: 0,
                                shadowColor: 'rgba(0, 0, 0, 0.5)'
                            }
                        }
                    }
                ]
            })
        }
    },
    mounted() {
        this.draw_chart();
    },
}
</script>

<style scoped>
#Main-box {
  overflow: hidden; /* 防止第二个滚动条*/
  margin: auto;
  padding: 0;
  width: 100vw;
  height: 130vh;
}

#block {
  width: 95vw;
  height: 25vh;
  margin: 0 auto;
}

#block >>> .el-carousel{
  border-radius: 15px;
}

img {
    width: 100vw;
    height: 25vh;
}

#text-box{
    margin-top: 15px;
    /*border: 1px solid blue;*/
}

.text-title{
    width: 60px;
    text-align: center;
    font-size: 12px;
    font-weight: 700;
    background-color: red;
    border-radius: 10px;
    color: white;
    margin-left: 10px;
}

.inner-box{
    display: block;
    margin-top: 15px;
    margin-left: 2vw;
    width: 96vw;
    height: 105px;
    /*border: 1px solid blue;*/
    border-radius: 10px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04);
}

.text{
    display: inline-block;
    width: 95%;
    height: 30%;
    text-align: left;
    line-height: 30px;
    padding-left: 10px;
    font-size: 14px;
    font-weight: 400;

    text-overflow: ellipsis;
    overflow: hidden;
    white-space: nowrap;
}

#chart{
  display: flex;
  justify-content: center;
  margin-top: 15px;
  margin-left: 2vw;
  width: 96vw;
  height: 50vh;
  /*border: 1px solid blue;*/
  border-radius: 10px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04);
}

a {
    color: blue;
    text-decoration: none;
}
</style>
