<template>
    <div id="school_box">
        <el-container>
            <el-main>
                <el-card class="box-card" >
                    <el-input v-model="schoolName" style="width:250px;" placeholder="请输入学校名称"></el-input>
                    <el-button type="primary" @click="get()" @keyup.enter="enterSearchMember">搜索</el-button>
                    <el-button type="text" @click="dialogVisible = true" style="margin: 5px auto"> 【使用小技巧】</el-button>
                    <div>
                        <el-container>
                            <el-aside width="80px">
                                <el-button type="text" style="margin-left: 0"><h3>院校所属></h3></el-button>
                                <el-button type="text" style="margin-left: 0;margin-top: -15px"><h3>院校类型></h3></el-button>
                                <el-button type="text" style="margin-left: 0;margin-top: -15px"><h3>办学类型></h3></el-button>
                                <el-button type="text" style="margin-left: 0;margin-top: -15px"><h3>院校特色></h3></el-button>
                            </el-aside>
                            <el-main>
                                <div id="check_box">
                                    <!--所属城市-->
                                    <div>
                                        <el-select v-model="value_1" placeholder="院校所属">
                                            <el-option
                                                v-for="item in China_address"
                                                :key="item.value"
                                                :label="item.label"
                                                :value="item.value">
                                            </el-option>
                                        </el-select>
                                    </div>
                                    <!--院校类型-->
                                    <div style="margin-top: 20px">
                                        <el-select v-model="value_2" placeholder="院校类型">
                                            <el-option
                                                v-for="item in School_type"
                                                :key="item.value"
                                                :label="item.label"
                                                :value="item.value">
                                            </el-option>
                                        </el-select>
                                    </div>
                                    <!--办学类型-->
                                    <div style="margin-top: 20px">
                                        <el-select v-model="value_3" placeholder="办学类型">
                                            <el-option
                                                v-for="item in Class_type"
                                                :key="item.value"
                                                :label="item.label"
                                                :value="item.value">
                                            </el-option>
                                        </el-select>
                                    </div>
                                    <!--院校特色-->
                                    <div style="margin-top: 20px">
                                        <el-select v-model="value_4" placeholder="院校特色">
                                            <el-option
                                                v-for="item in School_fun"
                                                :key="item.value"
                                                :label="item.label"
                                                :value="item.value">
                                            </el-option>
                                        </el-select>
                                    </div>
                                </div>
                                <el-button type="primary" @click="get2()" style="margin:5px auto;" class="btn1">搜索</el-button>
                            </el-main>
                        </el-container>
                    </div>

                    <el-dialog title="使用手册" :visible.sync="dialogVisible" width="300px">
                        <h3 style="margin-top: -20px">☆ 输入正确的学校名称，可精准搜索该学校</h3>
                        <h3>☆ 点击表格内的学校信息可跳转到学校详情页</h3>
                        <h3>☆ 选择对应条件可搜索相应的学校</h3>
                        <h3>☆ 两大搜索模块独立运行</h3>
                        <h3>☆ 院校所属、院校类型、办学类型、院校特色都为必选项</h3>
                    </el-dialog>
                </el-card>
                <br>
                <br>
                <!-- 表格数据 -->
                <el-table border :data="info.slice((currentPage-1)*pageSize,currentPage*pageSize)" stripe>
                    <el-table-column align="center" label="学校">
                        <el-table-column align="center" label="校徽" prop="school_name" class="table-h">
                            <template slot-scope="scope">
                                <router-link :to="'int'+'?id='+scope.row.id" >
                                    <img style="width: 50%" :src="petImage(scope.$index,scope.row)"/>
                                </router-link>
                            </template>
                        </el-table-column>

                        <el-table-column prop="school_name" align="center" label="名称" width="180" class="table-h">
                            <template slot-scope="scope">
                                <router-link :to="'int'+'?id='+scope.row.id" class="a">
                                    <span>{{ scope.row.school_name }}</span>
                                </router-link>
                            </template>
                        </el-table-column>
                    </el-table-column>
                    <el-table-column label="详细信息" align="center">
                        <el-table-column prop="school_type_cc" align="center" label="学校性质" class="table-h">
                            <template slot-scope="scope">
                                <router-link :to="'int'+'?id='+scope.row.id" class="a">
                                    <span>{{ scope.row.school_type_cc }}</span>
                                </router-link>
                            </template>
                        </el-table-column>

                        <el-table-column prop="school_bumen" align="center" label="隶属部门" class="table-h">
                            <template slot-scope="scope">
                                <router-link :to="'int'+'?id='+scope.row.id" class="a">
                                    <span>{{ scope.row.school_bumen }}</span>
                                </router-link>
                            </template>
                        </el-table-column>

                        <el-table-column prop="school_chengshi" align="center" label="地址" class="table-h">
                            <template slot-scope="scope">
                                <router-link :to="'int'+'?id='+scope.row.id" class="a">
                                    <span>{{ scope.row.school_chengshi }}</span>
                                </router-link>
                            </template>
                        </el-table-column>

                        <el-table-column prop="school_email" align="center" label="邮箱" class="table-h">
                            <template slot-scope="scope">
                                <router-link :to="'int'+'?id='+scope.row.id" class="a">
                                    <span>{{ scope.row.school_email }}</span>
                                </router-link>
                            </template>
                        </el-table-column>

                        <el-table-column prop="school_zhandi" align="center" label="占地面积（亩）" class="table-h">
                            <template slot-scope="scope">
                                <router-link :to="'int'+'?id='+scope.row.id" class="a">
                                    <span>{{ scope.row.school_zhandi }}</span>
                                </router-link>
                            </template>
                        </el-table-column>
                    </el-table-column>
                </el-table>
                <div>
                    <el-pagination
                        :page-size.sync="pageSize"
                        :page-sizes="pageSizes"
                        :current-page.sync="currentPage"
                        :pager-count="pageCount"
                        background
                        style="margin: 15px 0 0 0"
                        layout="prev, pager, next"
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
    name: "phone_checkSchool",
    data() {

        return {
            dialogVisible:false,

            schoolName: "",

            data3: "中国",//隐藏的表单默认显示的内容
            info: [],

            China_address:[
                {value:'全部',label:'全部'},
                {value:'北京',label:'北京'},
                {value:'天津',label:'天津'},
                {value:'山东',label:'山东'},
                {value:'河北',label:'河北'},
                {value:'山西',label:'山西'},
                {value:'辽宁',label:'辽宁'},
                {value:'吉林',label:'吉林'},
                {value:'上海',label:'上海'},
                {value:'江苏',label:'江苏'},
                {value:'浙江',label:'浙江'},
                {value:'安徽',label:'安徽'},
                {value:'福建',label:'福建'},
                {value:'江西',label:'江西'},
                {value:'河南',label:'河南'},
                {value:'湖南',label:'湖南'},
                {value:'湖北',label:'湖北'},
                {value:'广东',label:'广东'},
                {value:'广西',label:'广西'},
                {value:'黑龙江',label:'黑龙江'},
                {value:'内蒙古',label:'内蒙古'},
                {value:'海南',label:'海南'},
                {value:'重庆',label:'重庆'},
                {value:'四川',label:'四川'},
                {value:'贵州',label:'贵州'},
                {value:'云南',label:'云南'},
                {value:'西藏',label:'西藏'},
                {value:'陕西',label:'陕西'},
                {value:'甘肃',label:'甘肃'},
                {value:'青海',label:'青海'},
                {value:'宁夏',label:'宁夏'},
                {value:'新疆',label:'新疆'},
            ],
            School_type:[
                {value: '全部',label: '全部'},
                {value: '综合',label: '综合'},
                {value: '理工',label: '理工'},
                {value: '医药',label: '医药'},
                {value: '农林',label: '农林'},
                {value: '师范',label: '师范'},
                {value: '语言',label: '语言'},
                {value: '财经',label: '财经'},
                {value: '政法',label: '政法'},
                {value: '体育',label: '体育'},
                {value: '艺术',label: '艺术'},
                {value: '民族',label: '民族'},
                {value: '军事',label: '军事'},
                {value: '其他',label: '其他'},
            ],
            Class_type:[
                {value: '全部',label: '全部'},
                {value: '普通本科',label: '普通本科'},
                {value: '公办',label: '公办'},
                {value: '民办',label: '民办'},
                {value: '专科(高职)',label: '专科'},
                {value: '中外合作办学',label: '中外合作'},
                {value: '其他',label: '其他'},
            ],
            School_fun:[
                {value: '全部',label: '全部'},
                {value: '985',label: '985'},
                {value: '211',label: '211'},
                {value: '一流大学建设高校A类',label: '一流大学建设高校A类'},
                {value: '一流大学建设高校B类',label: '一流大学建设高校B类'},
                {value: '一流大学建设高校',label: '一流大学建设高校'},
                {value: '中央部门直属',label: '中央部门直属'},
                {value: '强基计划',label: '强基计划'},
                {value: '双高计划',label: '双高计划'},
            ],
            value_1:'全部',
            value_2:'全部',
            value_3:'全部',
            value_4:'全部',

            total: 0,
            pageSize: 10,  //一页显示多少条
            pageSizes: [5, 10, 15, 20, 50],//每页显示多少条
            currentPage: 1,  //当前位于哪页
            pageCount: 7,   //多少分页按钮


        }
    },
    //正式的搜索
    methods: {
        get() {
            if(this.schoolName == ''){this.$message.error("请输入校名！")}
            else{
                this.axios.get("http://101.34.248.53:8181/Map/list/byname", {params: {school_name: this.schoolName}})//
                    .then(resp => {
                        if (this.schoolName == '') {
                            this.$message.error('请输入学校名称');
                        } else {
                            console.log(resp);
                            this.total = resp.data.length;
                            this.info = resp.data;
                            this.$message.success("搜索成功！");
                        }
                    })
            }
        },
        //复选框搜索
        get2() {
            if(this.value_1 == ''){this.$message.error("请选择所属地区！");}
            else if(this.value_2 == ''){this.$message.error("请选择院校类型！");}
            else if(this.value_3 == ''){this.$message.error("请选择办学类型！");}
            else if(this.value_4 == ''){this.$message.error("请选择办学特色！");}
            else{


                // console.log(this.value_1 + '/' + this.value_2 + '/' + this.value_3 + '/' + this.value_4)
                this.axios.get("http://101.34.248.53:8181/Map/list/bycx/" + this.value_1 + '/' + this.value_2 + '/' + this.value_3 + '/' + this.value_4)
                    .then(resp => {
                        this.info = resp.data;
                        this.total = resp.data.length;
                        console.log(resp.data)
                        this.$message.success("搜索成功！");
                    })
            }
            // }
        },
        //初始化的时候调用的
        get3() {
            this.axios.get("http://101.34.248.53:8181/Map/list/byname", {params: {school_name: this.data3}})//
                .then(resp => {
                    console.log(resp);
                    this.total = resp.data.length;
                    this.info = resp.data;
                })
        },
        enterSearchMember() {
            this.get()
        },
        //校徽图片
        petImage(index, row) {
            var url = "http://101.34.248.53:8181/Map/list/school_logo/" + row.school_name
            // console.log(url)
            return url
        },
    },

    //项目初始化时显示的内容
    created() {
        this.get3();
        const _this = this;
        document.onkeydown = function() {
            var key = window.keyCode;
            if (key == 13) {
                _this.enterSearchMember();
            }
        }
    },
}
</script>

<style scoped>
.el-main{
    margin: 0;
    padding: 0;
}

#school_box{
    margin: 0;
    padding: 0;
    width: 100vw;
}

.box-card {
    width: 100vw;
}

.box-card >>> .el-card__body{
    margin: 0!important;
    width: 100vw;
    padding: 0;
    border: 0;
    background-color: transparent;
}

#check_box{
    margin-top: 15px;
    /*border: 1px solid red;*/
}


.text {
    font-size: 14px;
}

.table-h {
    text-decoration: none;
    font-size: 18px;
    color: #5e402f;
}

.box-card{
    border: 0;
    background-color: transparent;
}

.box-card >>> .el-card__header{
    width: 100vw;
    margin: 0;
    padding: 0;
    border: 0;
    background-color: transparent;
}

.el-table {
    margin-top: 15px;
    padding: 0;
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

.el-pagination{
    padding: 2px 0;
}

</style>