<template>
    <el-container>
        <el-tabs  v-model="activeName" type="card" class="tob_hand">
            <el-tab-pane label="咨询老师" style="margin: auto" name="first">

                <el-header style="height: 160px">
                    <el-card class="box-card" shadow="hover">
                        <div>
                            <div id="radio_all">
                                <!-- 侧边栏 -->
                                <div id="aside-box">
                                    <div style="margin-top: -15px">
                                        <el-button type="text" style="margin-top: -8px"><h3>专业层次></h3></el-button>
                                        <br>
                                        <el-button type="text" style="margin-top: -22px"><h3>专业门类></h3></el-button>
                                    </div>
                                </div>

                                <div id="button-box">
                                    <!--选择本/专科-->
                                    <div style="margin-top: -27px">
                                        <el-radio-group v-model="button_checked" size="small">
                                            <el-radio-button v-model="button_checked" label="ben">本科</el-radio-button>
                                            <el-radio-button v-model="button_checked" label="zhuan">专科</el-radio-button>
                                        </el-radio-group>
                                    </div>
                                    <!--=本科-->
                                    <div style="margin-top: 22px" v-if="choose_major(button_checked) == 1">
                                        <el-radio-group v-model="radio_major" size="small">
                                            <el-radio-button label="全部"></el-radio-button>
                                            <el-radio-button label="哲学"></el-radio-button>
                                            <el-radio-button label="经济学"></el-radio-button>
                                            <el-radio-button label="法学"></el-radio-button>
                                            <el-radio-button label="教育学"></el-radio-button>
                                            <el-radio-button label="文学"></el-radio-button>
                                            <el-radio-button label="历史学"></el-radio-button>
                                            <el-radio-button label="理学"></el-radio-button>
                                            <el-radio-button label="工学"></el-radio-button>
                                            <el-radio-button label="农学"></el-radio-button>
                                            <el-radio-button label="管理学"></el-radio-button>
                                            <el-radio-button label="艺术学"></el-radio-button>
                                        </el-radio-group>
                                    </div>
                                    <!--=专科-->
                                    <div style="margin-top: 22px" v-if="choose_major(button_checked) == 2">
                                        <el-radio-group v-model="radio_major" size="small">
                                            <el-radio-button label="农林牧渔"></el-radio-button>
                                            <el-radio-button label="资源环境与安全"></el-radio-button>
                                            <el-radio-button label="能源动力与材料"></el-radio-button>
                                            <el-radio-button label="土木建筑"></el-radio-button>
                                            <el-radio-button label="水利"></el-radio-button>
                                            <el-radio-button label="装备制造"></el-radio-button>
                                            <el-radio-button label="生物与化工"></el-radio-button>
                                            <el-radio-button label="食品药品与粮食"></el-radio-button>
                                            <el-radio-button label="轻工纺织"></el-radio-button>
                                            <el-radio-button label="交通运输"></el-radio-button>
                                            <el-radio-button label="电子信息"></el-radio-button>
                                            <el-radio-button label="医药卫生"></el-radio-button>
                                            <el-radio-button label="财经商贸"></el-radio-button>
                                            <div style="margin-top: 3px">
                                                <el-radio-button label="旅游"></el-radio-button>
                                                <el-radio-button label="文化艺术"></el-radio-button>
                                                <el-radio-button label="新闻传播"></el-radio-button>
                                                <el-radio-button label="教育与体育"></el-radio-button>
                                                <el-radio-button label="公安与司法"></el-radio-button>
                                            </div>
                                        </el-radio-group>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </el-card>
                </el-header>
                <el-main>
                    <div id="th-box">
                        <template v-for="(num,index) in teachers">
                            <div
                                class="box"
                                v-show="choose_teacher(num.major)"
                                :key="index">
                                <img :src="num.sex == '男'?top_man:top_woman">
                                <div class="teacher-intro">
                                    <p>姓名：{{ num.name }}</p>
                                    <p id="question">被咨询次数：{{ num.advice_num }}</p>
                                    <p>年龄：{{ num.age }}</p>
                                    <p>性别：{{ num.sex }}</p>
                                    <p>擅长：{{ num.major }}</p>
                                    <el-button type="primary" plain @click="teacher_introduce(index)">个人简介</el-button>
                                    <el-button type="success" plain @click="zixun(index)" class="zixun_button">点击咨询</el-button>
                                </div>
                            </div>
                        </template>
                        <el-dialog title="咨询老师" :visible.sync="dialogVisible" width="28%">
                            <el-form ref="add_form" :model="ruleForm" label-width="100px"> <!--:rules="rules"-->
                                <el-button type="text" class="text">问题描述</el-button>
                                <el-input
                                    type="textarea"
                                    :rows="4"
                                    placeholder="请输入内容"
                                    v-model="text"
                                    maxlength="100"
                                    style="width: 70%;margin-left: 11px;margin-top: 10px"
                                    class="form"
                                    show-word-limit>
                                </el-input>
                                <el-form-item>
                                    <el-button type="success" style="margin-left: 1px;margin-top: 10px" @click="onSubmit()">提交
                                    </el-button>
                                    <el-button type="info" style="margin-left: 50px" @click="new_get()">重置</el-button>
                                    <el-button type="info" style="margin-left: 50px" @click="dialogVisible = false">取消</el-button>
                                </el-form-item>
                            </el-form>
                        </el-dialog>
                    </div>
                </el-main>

            </el-tab-pane>
            <el-tab-pane label="我的咨询" style="width: 1300px" name="second">
                <el-table :data="info" stripe class="table_h">
                    <el-table-column prop="name" align="center" label="咨询师姓名" width="230"></el-table-column>
                    <el-table-column prop="question" align="center" label="问题" width="230" autocomplete="off"></el-table-column>
                    <el-table-column prop="time" align="center" label="咨询时间"></el-table-column>
                    <el-table-column align="center" label="反馈信息">


                        <template slot-scope="scope">
<!--                            <el-button type="success ">{{scope.row.question}}</el-button>-->
                          <el-collapse v-model="activeNames" @change="handleChange">
                            <el-collapse-item title="查看反馈" name="1">
                                    <div>{{scope.row.advice}}</div>
                            </el-collapse-item>
                          </el-collapse>
                        </template>
                    </el-table-column>
                </el-table>
            </el-tab-pane>
        </el-tabs>
        <el-dialog title="查看反馈" :data="message"  :visible.sync="dialogVisible2">
            <h3 v-if="this.panduan == false">暂无反馈</h3>
            <h3>{{message.text}}</h3>
        </el-dialog>
    </el-container>
</template>

<script>
import axios from 'axios'
export default {

    name: "teacher",
    data() {
        return {
            activeName: 'first',
            radio_major: '全部',
            button_checked: 'ben',
            top_man: require("../assets/nan2.png"),
            top_woman: require("../assets/nv2.png"),
            teachers: [],
            dialogVisible: false,
            subjects: [],//选课
            text: "",//问题
            id:'',
            ruleForm: {},
            mained_square: "",//咨询师账户名
            dialogVisible2:false,
            info: [],
            message:[],
            panduan:false
        }
    },
    methods: {
        // axios获取数据
        get_data() {
            axios({
              method:'POST',
              url:'api/students/getteacher',
              data:{
                action: 'get_teacher',
                account: this.$cookies.get('user_name')
              }
            }).then((resp)=>{
              console.log(resp.data.data[0])
              this.teachers=resp.data.data
            })
        },
        // 判断选择的是本科还是专科，来进行专业的筛选
        choose_major(val) {
            if (val == 'ben')
                return 1;
            else {
                return 2;
            }
        },
        //根据老师的擅长进行归类
        choose_teacher(major) {
            if (this.radio_major == '全部') {
                return true;
            } else if (major == this.radio_major) {
                return true;
            } else {
                return false;
            }
        },
        // 右侧弹出老师个人介绍的气泡
        teacher_introduce(index) {
            this.$notify({
                title: '老师个人介绍',
                message: this.teachers[index].text,
                duration: 10000,
            })
        },

        //咨询老师
        onSubmit() {
          this.main_square = this.$cookies.get('user_name');
          if(this.text == ''){this.$message.error("请输入要咨询的问题！")}
            else {
            axios({
              method:'POST',
              url:'api/students/givequestion',
              data:{
                action:'give_question',
                // account:'12345678',
                account:this.$cookies.get('user_name'),
                question:this.text,
                tch_code:this.mained_square
              }
            }).then((resp)=>{
              console.log(resp.data)
              if (resp.data.ret ===0) {
                this.$message.success("咨询成功")
                this.get_data()
                this.dialogVisible = false
                this.new_get()
                this.mywenti()
              }
            })


            }
        },

        //咨询函数，判断是否确定咨询
        zixun(index) {
            this.dialogVisible = true;
            //向后台传递参数
            this.mained_square = this.teachers[index].account;
            // this.file_post(index);
        },
        new_get(){
            this.text = ""
        },
        //显示我的咨询
        mywenti() {
          axios({
            method:'POST',
            url:" api/students/getquestion",
            data:{
              action:'get_question',
              // account:'12345678'
              account:this.$cookies.get('user_name'),
            }
          }).then((resp)=>{
            console.log(resp.data.question)
            this.info=resp.data.question
          })
        }
    },
    created() {
        this.get_data();
        this.mywenti()
    }
}
</script>

<style scoped>
/*头部整体设置*/
#radio_all {
    height: 140px;
    position: relative;
}

/*侧边栏设置*/
#aside-box {
    width: 250px;
}

/*设置头部按钮框的大小和位置*/
#button-box {
    width: 1200px;
    position: relative;
    top: -80px;
    right: -100px;
}

/*main的总体布局*/
#th-box {
    width: 1500px;
    /*margin: 0 auto;*/
    text-align: left;
}

/*每一个信息框的设置*/
.box {
    background-color: #ffffff;
    margin-left: 50px;
    margin-top: 20px;
    display: inline-block;
    width: 300px;
    height: 270px;
    border: 1px solid #EBEEF5;
    padding: 50px 0;
    text-align: center;
    transition: .3s;
    position: relative;
    /*box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.3);*/
}

.box:hover {
    box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.3);
}

.box-card {
    /*height: 230px;*/
    /*width: 1574px;*/
    margin: auto;
    /*margin-top: -15px;*/
}
/*设置头像*/
img {
    width: 100px;
    height: 100px;
    border-radius: 50%;
    border: 1px solid #EBEEF5;
    box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.2);
}

/*老师信息框*/
.teacher-intro {
    margin: 0 auto;
    width: 250px;
    text-align: left;
}

/*被咨询次数 表示框位置*/
#question {
    position: absolute;
    top: 156px;
    right: 20px;
}

/*点击咨询 按钮位置*/
.zixun_button {
    position: relative;
    right: -45px;

}

.text {
    /*margin-top: 15px;*/
    /*margin-left: 26px;*/
    color: #000000;
    margin-left: 31px;
}

.text:hover {
    color: #000000;
}

.xuanke {
    margin-right: 30px;
    margin-top: -30px;
    color: black;
}

.xuanke:hover {
    margin-right: 30px;
    margin-top: -30px;
    color: black;
}

.form {
    /*width: 350px;*/
    width: 86%;
}

.tob_hand {
    background-color: #defcfc;
    /*box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.2);*/
}
</style>
