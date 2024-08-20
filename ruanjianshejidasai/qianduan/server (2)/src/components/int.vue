<template>
    <div id="int-box">
        <div id="school_box">
            <div id="msg" v-if="atem" style="background-color: white">
                <div class="tuchu"> 基本信息</div>
                <div id="msg-all">
                    <div><i class="el-icon-time"></i> 创建时间:
                        <span>{{ atem.school_time }}</span>
                    </div>
                    <div><i class="el-icon-office-building"></i> 占地面积(亩):
                        <span>{{ atem.school_zhandi }}</span>
                    </div>
                    <div><i class="el-icon-s-check"></i> 隶属于:
                        <span>{{ atem.school_bumen }}</span>
                    </div>
                    <div>
                        <i class="el-icon-map-location"></i> 学校地址:
                        <span id="school_locat">{{ atem.school_address }}</span>
                    </div>
                </div>
            </div>

            <div id="sex-box" v-if="atem" style="background-color: white">
                <div class="tuchu"> 男女比例</div>
                <div id="sex">
                    <div id="man">
                        <img src="../assets/nan.png">
                        <div>男</div>
                    </div>
                    <el-progress :percentage="numberFloat(atem.school_nan)"></el-progress>
                    <br>
                    <div id="girl">
                        <img src="../assets/nv.png">
                        <div>女</div>
                    </div>
                    <el-progress :percentage="numberFloat(atem.school_nv)" color="red"></el-progress>
                </div>
            </div>
        </div>

        <div id="tubiao-box" style="background-color: white">
            <div id="tubiao"></div>
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

        <div id="scl-box" v-if="jies" style="background-color: white">
            <el-collapse v-model="intro">
                <div class="tuchu"> 学校简介</div>
                <div id="jieshao" style="margin-top: 15px;text-indent:1.6em">
                    {{ jies }}
                </div>
            </el-collapse>
        </div>

    </div>
</template>

<script>
export default {
    name: "introduce",
    data() {
        return {
            number: null,
            atem: null,
            jies: null,
            intro: '1',
            bl_up: null,
            bl_job: null,
            bl_abroad: null
        }
    },
    created() {
        this.get_data();
    },

    methods: {
        get_data() {
            this.number = this.$route.query.id;
            this.axios.get('http://101.34.248.53:8181/Map/list/byid_one/' + this.number)
                .then(resp => {
                    this.atem = resp.data;
                    this.bl_up = this.atem.school_up;
                    this.bl_job = this.atem.school_job;
                    this.bl_abroad = this.atem.school_abroad;
                    // console.log(this.bl_up);
                    // console.log(this.bl_job);
                    // console.log(this.bl_abroad);
                    this.draw_charts(this.bl_up, this.bl_job, this.bl_abroad);
                }).catch(error => {
                console.log(error);
            });

            this.axios.get('http://101.34.248.53:8181/Map/list/school_jieshao/' + this.number)
                .then(resp => {
                    this.jies = resp.data;
                }).catch(error => {
                console.log(error);
            })
        },

        numberFloat(shuju) {
            var nt = parseFloat(shuju);
            if (isNaN(nt) == true)
                return 0;
            else
                return nt;
        },

        draw_charts(val_1, val_2, val_3) {
            let myChart = this.$echarts.init(document.getElementById('tubiao'));
            myChart.setOption({
                title: {
                    text: '毕业去向',
                    left: 'left'
                },
                tooltip: {
                    trigger: 'item'
                },
                legend: {
                    orient: 'horizontal',
                    left: 'center',
                },
                series: [
                    {
                        type: 'pie',
                        radius: '50%',
                        data: [
                            {value: val_1, name: '考研率'},
                            {value: val_2, name: '就业率'},
                            {value: val_3, name: '出国率'},
                        ],
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

}
</script>

<style scoped>
#int-box {
    height: 100%;
    /*background-color: pink;*/
    padding: 5px;
    position: relative;
}

#school_box {
    /*background-color: white;*/
    width: auto;
}

.tuchu {
    height: 32px;
    line-height: 32px;
    border-width: 0 0 0 3px;
    border-style: solid;
    border-color: brown;
    padding: 0 3px;
    font-size: 16px;
}

#msg {
    margin: 0;
    padding: 0;
    width: 550px;
    height: 300px;
    box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
    border-radius: 10px;
}

/*#msg:hover{*/
/*  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);*/
/*  border-radius: 10px;*/
/*}*/

#msg-all {
    padding: 5px 0 5px 13px;
    font-size: 14px;
    line-height: 55px;
    /*text-indent: 1em;*/
    font-weight: 700;
}

#msg-all span {
    padding: 10px;
    font-weight: 400;
}

#school_locat {
    font-size: 12px;
    font-weight: 400;
}

#sex-box {
    margin: 0;
    padding: 0;
    width: 550px;
    height: 300px;
    position: absolute;
    top: 5px;
    right: 5px;
    box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
    border-radius: 10px;
}

/*#sex-box:hover{*/
/*  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);*/
/*  border-radius: 10px;*/
/*}*/

#sex {
    padding: 10px;
}

#tubiao-box {
    margin-top: 25px;
    width: auto;
    height: 250px;
    /*border: 1px solid red;*/
    box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
    border-radius: 10px;
}

/*#tubiao-box:hover{*/
/*  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);*/
/*  border-radius: 10px;*/
/*}*/

#tubiao {
    margin: 0 auto;
    /*width: 800px;*/
    height: 300px;
}

#scl-box {
    margin: 10px 0;
    box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
    border-radius: 10px;
}

/*#scl-box:hover{*/
/*  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);*/
/*  border-radius: 10px;*/
/*}*/

#jieshao {
    box-sizing: border-box;
    padding: 5px;
    font-family: "Helvetica Neue", Helvetica, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "微软雅黑", Arial, sans-serif;
    line-height: 1.5;
}
</style>
