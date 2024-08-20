<template>
  <div id="day">
    <div id="tuchu">
    </div>
    <div id="top-box">
      <div class="block">
        <el-date-picker
            v-model="value_day"
            type="month"
            placeholder="选择日期"
            value-format="yyyy-M"
            @change="op_day(value_day)"
            default-value=value_day>
        </el-date-picker>
      </div>
    </div>
    <div id="numer_tit">
      数量 / 人
    </div>

    <div id="time_tit">
      日期
    </div>
    <div id="user"></div>
  </div>
</template>

<script>
export default {
  name: "tableinfo",
  data() {
    return {
      arr: null,
      value_day: '2021-9',
      now_year: 2021,
      now_month: 9,
      // arr:require('@/data/com.json')
    }
  },
  created() {
      let date = new Date();
      this.now_year = date.getFullYear();
      this.now_month = date.getMonth() + 1;
      this.value_day = `${this.now_year}-${this.now_month}`;
    this.get_data();
  },
  methods: {
    op_day(val) {
      var date = new Date()
      const Regex_1 = /^[0-9]{1,4}/gm;
      const Regex_2 = /[0-9]{1,2}$/gm;
      this.now_year = Regex_1.exec(val);
      this.now_month = Regex_2.exec(val);

      this.get_data();
    },

    get_data() {
      this.axios.get('http://101.34.248.53:8181/Map/PV_record/' + this.now_year + '/' + this.now_month)
          .then(resp => {
            this.arr = resp.data;
            if(this.arr.length == 1){
              return alert("该月暂无数据!!!");
            }

            this.run(this.arr);
          }).catch(error => {
        console.log(error)
      })
    },

    run(_rawData) {
      let myChart = this.$echarts.init(document.getElementById('user'));
      // 选择国家名
      var countries = ['用户访问量', '用户注册总量', '咨询师注册总量'];
      // 用于设置存储的数据
      var datasetWithFilters = [];
      // 用于设置存储的方法
      var seriesList = [];
      // 动画函数
      this.$echarts.util.each(countries, function (country) {
        // 设置id
        var datasetId = 'dataset_' + country;
        datasetWithFilters.push({
          id: datasetId,
          // 日期来源id
          fromDatasetId: 'dataset_raw',
          // 动态图表
          transform: {
            // 设置参考线
            type: 'filter',
            config: {
              // 设置维度
              and: [
                // 指定日期开始时间
                {dimension: 'Time', gte: 1},
                {dimension: 'Name', '=': country}
              ]
            }
          }
        });

        // 节点依次添加
        seriesList.push({
          type: 'line',
          datasetId: datasetId,
          // true为显示每一个节点
          showSymbol: false,
          name: country,
          // 在折线末尾显示数据
          endLabel: {
            show: true,
            formatter: function (params) {
              return params.value[2] + ': ' + params.value[0];
            }
          },
          // 防止标签过多导致重叠
          labelLayout: {
            moveOverlap: 'shiftY'
          },
          // 数据聚焦高亮
          emphasis: {
            focus: 'series'
          },
          // 设置坐标轴上节点如何显示
          encode: {
            x: 'Time',
            y: 'Sum',
            // 折线的显示数据（图形上的文本标签）
            label: ['Name', 'Sum'],
            // 用来分类数据
            itemName: 'Time',
            // 表示维度会在tooltip中显示
            tooltip: ['Sum'],
          }
        });
      });

      myChart.setOption({
        animationDuration: 10000,
        dataset: [{
          id: 'dataset_raw',
          source: _rawData
        }].concat(datasetWithFilters),
        // 设置标题
        // title: {
        //     text: '用户PV访问',
        //     textStyle:{
        //         fontSize:14,
        //         color:'#FFF',
        //     }
        // },
        // 设置悬浮提示框
        tooltip: {
          order: 'valueDesc',
          trigger: 'axis',
        },
        xAxis: {
          type: 'category',
          nameLocation: 'middle'
        },
        yAxis: {
          name: 'Sum'
        },
        // 表格位移
        grid: {
          top: 100,
          right: 140
        },

        // 数据调用
        series: seriesList
      })
    },
  },
}
</script>

<style scoped>
/*设置全局框架*/
#day {
  background-color: #ffffff;
  width: 1000px;
  margin: 0 auto;
  /*border:1px solid red;*/
  border-radius: 25px;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
  text-align: center;
  position: relative;
}

#top-box {
  width: 600px;
  margin: 0 auto;
}

/*加红字体*/
#tuchu {
  font-style: italic;
  height: 50px;
  font-size: 16px;
  color: #fa9696;
  line-height: 50px;
}

#numer_tit{
  width: 60px;
  height: 25px;
  color: black;
  font-size: 14px;
  background-color: white;
  position: absolute;
  top: 150px;
  left: 55px;
  z-index: 9999;
}

#time_tit{
  width: 60px;
  height: 25px;
  color: black;
  font-size: 14px;
  background-color: white;
  position: absolute;
  bottom: 45px;
  right: 70px;
  z-index: 9999;
}
/*设置图表*/
#user {
  width: 1000px;
  height: 700px;
}
</style>
