<template v-if="info">
    <div>
        <el-container>
            <el-main>
                <el-card class="box-card" >

                    <el-input v-model="data1" placeholder="请输入专业" style="width:250px;"></el-input>
                    <el-button type="primary" @click="get()" style="margin: 5px auto;text-align: center" class="btn1">搜索</el-button>
                    <el-button type="text" @click="dialogVisible = true" style="margin: 0 auto"> 【使用小技巧】</el-button>
                    <br>
                    <br>
                    <div id="radio-all">
                        <div id="aside-box">
                            <div style="margin-left: -20px">
                                <el-button type="text"><h3>专业层次></h3></el-button>
                            </div>
                        </div>

                        <div id="button-box">
                            <!--选择本/专科-->
                            <div>
                                <el-radio-group v-model="button_checked" size="small">
                                    <el-radio-button v-model="button_checked" label="ben">本科</el-radio-button>
                                    <el-radio-button v-model="button_checked" label="zhuan">专科</el-radio-button>
                                </el-radio-group>
                            </div>
                            <!--=本科-->
                            <div style="margin-top: 10px" v-if="choose_major(button_checked) == 1">
                                <el-select v-model="value" placeholder="请选择">
                                    <el-option
                                        v-for="item in major_ben"
                                        :key="item.value"
                                        :label="item.label"
                                        :value="item.value">
                                    </el-option>
                                </el-select>
                                <el-button type="primary" class="btn1" @click="find_data">搜索</el-button>
                            </div>
                            <!--=专科-->
                            <div style="margin-top: 10px" v-if="choose_major(button_checked) == 2">
                                <el-select v-model="value" placeholder="请选择">
                                    <el-option
                                        v-for="item in major_zhuan"
                                        :key="item.value"
                                        :label="item.label"
                                        :value="item.value">
                                    </el-option>
                                </el-select>
                                <el-button type="primary" class="btn1" @click="find_data">搜索</el-button>
                            </div>
                        </div>

                        <el-dialog title="使用手册" :visible.sync="dialogVisible" width="300px" style="text-align: left">
                            <h3 style="margin-top: -20px">☆ 输入正确的专业名称，可精准搜索该专业</h3>
                            <h3>☆ 点击专业信息可跳转到专业详情页</h3>
                            <h3>☆ 选择对应的条件可搜索相应的专业</h3>
                            <h3>☆ 两大搜索模块独立运行</h3>
                            <h3>☆ 专业层次和专业门类都为必选项</h3>
                        </el-dialog>
                    </div>

                </el-card>
                <!--接受并且展示数据的表格-->
                <el-table
                    :data="info.slice((currentPage-1)*pageSize,currentPage*pageSize)"
                    stripe
                >
                    <el-table-column align="center" label="专业信息">
                        <el-table-column prop="name" align="center" label="专业名称" class="a" style="width: 100px">
                            <template slot-scope="scope">
                                <router-link :to="'bi'+'?id='+scope.row.id" class="a">
                                    <span>{{ scope.row.name }}</span>
                                </router-link>
                            </template>
                        </el-table-column>
                        <el-table-column prop="cc" align="center" label="层次" class="a" style="width: 100px">
                            <template slot-scope="scope">
                                <router-link :to="'bi'+'?id='+scope.row.id" class="a">
                                    <span v-if="scope.row.cc==1">本科</span>
                                    <span v-if="scope.row.cc==2">专科</span>
                                </router-link>
                            </template>
                        </el-table-column>
                        <el-table-column prop="major_code" align="center" label="专业代码" class="a">
                            <template slot-scope="scope">
                                <router-link :to="'bi'+'?id='+scope.row.id" class="a">
                                    <span>{{ scope.row.major_code }}</span>
                                </router-link>
                            </template>
                        </el-table-column>
                        <el-table-column prop="lv2_name" align="center" label="专业门类" class="a">
                            <template slot-scope="scope">
                                <router-link :to="'bi'+'?id='+scope.row.id" class="a">
                                    <span>{{ scope.row.lv2_name }}</span>
                                </router-link>
                            </template>
                        </el-table-column>
                    </el-table-column>
                    <el-table-column prop="major_year" align="center" label="修业年限" class="a">
                        <template slot-scope="scope">
                            <router-link :to="'bi'+'?id='+scope.row.id" class="a">
                                <span>{{ scope.row.major_year }}</span>
                            </router-link>
                        </template>
                    </el-table-column>

                    <el-table-column prop="degree" align="center" v-if="xuewei == true" label="授予学位" class="a">
                        <template slot-scope="scope">
                            <router-link :to="'bi'+'?id='+scope.row.id" class="a">
                                <span>{{ scope.row.degree }}</span>
                            </router-link>
                        </template>
                    </el-table-column>
                    <el-table-column prop="lv1_name" align="center" label="学位" class="a">
                        <template slot-scope="scope">
                            <router-link :to="'bi'+'?id='+scope.row.id" class="a">
                                <span>{{ scope.row.lv1_name }}</span>
                            </router-link>
                        </template>
                    </el-table-column>
                    <el-table-column prop="kaoyan" align="center" label="考研方向" class="a">
                        <template slot-scope="scope">
                            <router-link :to="'bi'+'?id='+scope.row.id" class="a">
                                <span>{{ scope.row.kaoyan }}</span>
                            </router-link>
                        </template>
                    </el-table-column>


                </el-table>
                <div>
                    <el-pagination
                        :page-size.sync="pageSize"
                        :page-sizes="pageSizes"
                        :current-page.sync="currentPage"
                        :pager-count="pageCount"
                        style="margin-top: 6px"
                        background
                        layout="prev, pager, next,jumper"
                        :total=total
                    >
                    </el-pagination>
                </div>
            </el-main>
        </el-container>

    </div>
</template>

<script>
export default {
    name: "phone_checkMajor",
    data() {
        return {
            num:'favor_no',
            button_checked: 'ben',
            xuewei:true,
            dialogVisible:false,

            // 专业数据
            major_ben:[
                {value:'哲学',label:'哲学'},
                {value:'经济学',label:'经济学'},
                {value:'法学',label:'法学'},
                {value:'教育学',label:'教育学'},
                {value:'文学',label:'文学'},
                {value:'历史学',label:'历史学'},
                {value:'理学',label:'理学'},
                {value:'工学',label:'农学'},
                {value:'管理学',label:'管理学'},
                {value:'艺术学',label:'艺术学'},
            ],
            major_zhuan:[
                {value:'农林牧渔大类',label:'农林牧渔'},
                {value:'资源环境与安全大类',label:'资源环境与安全'},
                {value:'能源动力与材料大类',label:'能源动力与材料'},
                {value:'土木建筑大类',label:'土木建筑'},
                {value:'水利大类',label:'水利'},
                {value:'装备制造大类',label:'装备制造'},
                {value:'生物与化工大类',label:'生物与化工'},
                {value:'食品药品与粮食大类',label:'食品药品与粮食'},
                {value:'轻工纺织大类',label:'轻工纺织'},
                {value:'交通运输大类',label:'交通运输'},
                {value:'电子信息大类',label:'电子信息'},
                {value:'医药卫生大类',label:'医药卫生'},
                {value:'旅游大类',label:'旅游'},
                {value:'文化艺术大类',label:'文化艺术'},
                {value:'新闻传播大类',label:'新闻传播'},
                {value:'教育与体育大类',label:'教育与体育'},
                {value:'公安与司法大类',label:'公安与司法'},
            ],
            value:'',

            data1: "",
            data2: "哲学",
            info: [],

            total: 0,
            pageSize: 10,  //一页显示多少条
            pageSizes: [5, 10, 15, 20, 50],//每页显示多少条
            currentPage: 1,  //当前位于哪页
            pageCount: 7,   //多少分页按钮
        }
    },
    methods: {
        //表单查询
        get() {
            if(this.data1 == ''){this.$message.error("请输入专业名称！")}
            else{
                this.axios.get("http://101.34.248.53:8181/Map/major/byname", {params: {major_name: this.data1}})//
                    .then(resp => {
                        // console.log(resp)
                        this.total = resp.data.length;
                        this.info = resp.data;
                        this.$message.success("查找成功！")
                    })
            }
        },

        //单选框查询
        find_data() {
            if(this.value == ''){
                this.$message.error("请选择专业门类！")
            }else{
                if (this.button_checked == 'ben'){
                    this.axios.get("http://101.34.248.53:8181/Map/major/bycx/" + '本科'+ '%7C' + this.value)
                        .then(resp => {
                            this.$message.success("查找成功！")
                            this.total = resp.data.length;
                            this.info = resp.data;
                            this.value='';
                        }).catch((error)=>{
                        console.log(error);
                    })
                }
                else if(this.button_checked == 'zhuan'){
                    this.axios.get("http://101.34.248.53:8181/Map/major/bycx/" + '专科' + '%7C' + this.value)
                        .then(resp => {
                            this.$message.success("查找成功！")
                            this.total = resp.data.length;
                            this.info = resp.data;
                            this.xuewei = false;
                            this.value='';
                        }).catch((error)=>{
                            console.log(error);
                    })
                }

            }
        },

        //初始化列表调用此接口
        get3() {
            this.axios.get("http://101.34.248.53:8181/Map/major/byname", {params: {major_name: this.data2}})//
                .then(resp => {
                    // console.log(resp)
                    this.total = resp.data.length;
                    this.info = resp.data;
                })
        },

        choose_major(val) {
            if (val == 'ben')
                return 1;
            else {
                return 2;
            }
        },

        enterSearchMember() {
            this.get();
        }
    },
    created() {
        this.get3();
    }
}
</script>

<style scoped>
.el-main{
    margin: 0;
    padding: 0;
}

#radio-all{
    margin-top: -10px;
    position: relative;
}

#aside-box {
    width: 80px;
}

#button-box {
    margin: 0;
    padding: 0;
    width: 100%;
    text-align: center;
    position: absolute;
    top: 20px;
    left: 0;
}

.a {
    text-decoration: none;
    font-size: 19px;
    color: #5e402f;
}
.a:hover{
    text-decoration: none;
    font-size: 19px;
    color: #ff5b00;
}

.box-card {
    margin: 0;
    padding: 0;
    width: 100vw;
    height: 260px;
    background-color: transparent;
    border: 0 solid transparent;
}

.el-table {
    width: 100vw;
    margin: 15px auto 0 auto;
}

.btn11{
    background-color: #0077ff;
}
</style>