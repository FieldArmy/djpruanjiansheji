<template>
    <div v-if="info">
        <el-card class="box-card">
            <div slot="header" class="clearfix" style="height: 30px">
                <span class="size_t1">智能填报(春季)</span>
                <br>
                <el-button type="text" @click="dialogVisible = true"> 【注意事项】</el-button>
            </div>
            <el-dialog title="注意事项" :visible.sync="dialogVisible" width="300px">
                <h3 style="margin-top: -20px">本系统根据2021和2022两年录取数据，进行推荐志愿服务.</h3>
                <h3>本系统推荐的院校名单，仅供参考，报考风险由考生本身承担！</h3>
                <h3>高考分数、高考位次、专业类别为必填项！</h3>
            </el-dialog>
            <br>
            <div id="form-box">
                <el-form :inline="true" :model="GKfenshu" class="demo-form-inline">
                    <el-form-item label="高考分数">
                        <el-input v-model="GKfenshu" placeholder="分数"></el-input>
                    </el-form-item>
                </el-form>
                <el-form :inline="true" :model="GKweici" class="demo-form-inline">
                    <el-form-item label="高考位次">
                        <el-input v-model="GKweici" placeholder="位次"></el-input>
                    </el-form-item>
                </el-form>

                <div id="tool-box">
                    <el-tooltip content="若同时输入分数和位次,则以位次优先">
                        <i class="el-icon-question"/>
                    </el-tooltip>
                </div>
            </div>

            <!-- 城市级联选择器-->
            <div class="block">
                <div>
                    <el-button type="text" style="margin-top: -15px"><h3>填报批次</h3></el-button>
                    <el-radio-group v-model="button_checked" size="small">
                        <el-radio-button style="margin-left: 5px" v-model="button_checked" label="ben">本科</el-radio-button>
                        <el-radio-button v-model="button_checked" label="zhuan">专科</el-radio-button>
                    </el-radio-group>
                    <br>
                    <!-- 本科专业-->
                    <el-button type="text" style="margin-top: 5px;"><h3>专业类别</h3></el-button>
                    <el-cascader
                        class="width_form"
                        placeholder="不限"
                        :options="options2"
                        filterable
                        v-model="list2"
                        clearable
                        collapse-tags
                        :props="{expandTrigger: 'hover' }"
                        v-show="panduan == true"
                    >
                    </el-cascader>

                    <el-cascader
                        class="width_form"
                        placeholder="不限"
                        :options="options2"
                        v-model="list2"
                        clearable
                        collapse-tags
                        :props="{expandTrigger: 'hover' }"
                        v-show="panduan == false"
                    >

                    </el-cascader>
                    <!-- 专业类别-->
                    <el-button type="text" style="margin-top: 5px;"><h3>教育层次</h3></el-button>
                    <el-cascader
                        class="width_form"
                        placeholder="不限"
                        :options="options4"
                        filterable
                        v-model="list3"
                        clearable
                        collapse-tags
                        :props="{expandTrigger: 'hover' }"
                    >
                    </el-cascader>

                    <!--校企合作选项-->
                    <el-button type="text" style="margin-top: 5px;"><h3>校企合作</h3></el-button>
                    <el-switch
                        v-model="value"
                        active-color="#13ce66"
                        style="margin-left: 10px">
                    </el-switch>
                    <el-button
                        type="cuccess"
                        v-if="choose_major(button_checked) == 1"
                        style="margin-left: 15px"
                        icon="el-icon-search"
                        @click="get1()">
                        提交
                    </el-button>
                </div>

            </div>


        </el-card>
        <!--显示的表格-->
        <el-card class="box-card2">
            <el-table :data="info.slice((currentPage-1)*pageSize,currentPage*pageSize)" border
                      style="margin-top: 0;" :row-style="{height:'70px'}" stripe>
                <el-table-column align="center" label="2021招生计划">
                    <el-table-column prop="major" align="center" label="专业" width="180" class="tableBox">
                        <template slot-scope="scope">
                            <span class="a">{{ scope.row.major }}</span>
                        </template>
                    </el-table-column>
                    <el-table-column prop="university" align="center" label="学校名称">
                        <template slot-scope="scope">
                            <router-link :to="'int'+'?id='+scope.row.school_id" class="a">
                                <span class="b">{{ scope.row.university }}</span>
                            </router-link>
                        </template>
                    </el-table-column>
                    <el-table-column prop="plan" align="center" label="计划数">
                        <template slot-scope="scope">
                            <span class="a">{{ scope.row.plan }}</span>
                        </template>
                    </el-table-column>
                </el-table-column>
                <el-table-column prop="cc" align="center" label="层次" class="a" style="width: 100px">
                    <template slot-scope="scope">
                        <span class="a" v-if="scope.row.cc==1">本科</span>
                        <span class="a" v-if="scope.row.cc==0">专科</span>
                    </template>
                </el-table-column>
                <el-table-column prop="rank_min" align="center" label="最低位次">
                    <template slot-scope="scope">
                        <span class="a">{{ scope.row.rank_min }}</span>
                    </template>
                </el-table-column>
                <el-table-column align="center" label="详细信息">
                    <el-table-column prop="school_type_cc" align="center" label="属性">
                        <template slot-scope="scope">
                            <span class="a">{{ scope.row.school_type_cc }}</span>
                        </template>
                    </el-table-column>
                    <el-table-column prop="school_address" align="center" label="学校地址">
                        <template slot-scope="scope">
                            <span class="a">{{ scope.row.school_address }}</span>
                        </template>
                    </el-table-column>
                </el-table-column>
            </el-table>
            <el-pagination
                :page-size.sync="pageSize"
                :page-sizes="pageSizes"
                :current-page.sync="currentPage"
                :pager-count="pageCount"
                background
                style="margin-top: 6px"
                layout="prev, pager, next,jumper"
                :total=total
            >
            </el-pagination>
        </el-card>
    </div>
</template>

<script>
export default {
    name: "phone_MajorSpring",
    data(){
        return {
            button_checked: 'ben',
            dialogVisible: false,
            value: "true",//校企合作
            value1: "true",//校企合作
            panduan: true, //判断本科/专科
            add: "",
            GKfenshu: "", //分数
            GKweici: "", //次位
            GKfenshu1: "500", //分数
            GKweici1: "20", //次位
            //三个下拉列表
            list2: "",
            list3: "*",
            list22: "信息技术",
            list33: "公办",
            info: [],
            total: 0,
            pageSize: 10,  //一页显示多少条
            pageSizes: [5, 10, 15, 20, 50],//每页显示多少条
            currentPage: 1,  //当前位于哪页
            pageCount: 7,   //多少分页按钮
            //所有专业
            options2: [
                {value: '农林果蔬', label: '农林果蔬',},
                {value: '畜牧养殖', label: '畜牧养殖',},
                {value: '土建', label: '土建',},
                {value: '机械', label: '机械',},
                {value: '机电一体化', label: '机电一体化',},
                {value: '电工电子', label: '电工电子',},
                {value: '化工', label: '化工',},
                {value: '服装', label: '服装',},
                {value: '汽车', label: '汽车',},
                {value: '信息技术', label: '信息技术',},
                {value: '医药', label: '医药',},
                {value: '护理', label: '护理',},
                {value: '财经', label: '财经',},
                {value: '商贸', label: '商贸',},
                {value: '烹饪', label: '烹饪',},
                {value: '旅游服务', label: '旅游服务',},
                {value: '文秘服务', label: '文秘服务',},
                {value: '学前教育', label: '学前教育',},
            ],
            //专业类别
            options4: [
                {value: '公办', label: '公办'},
                {value: '民办', label: '民办'},
            ],
        }
    },
    methods:{
        get1() {
            // console.log(+ '本科' +this.GKfenshu + '/' + this.GKweici + '/' + this.list2 + '/' + this.list3 + '/' + this.value)
            // if (this.choose_major() == 1) {
            if (this.GKfenshu == '') {
                this.$message.warning("请填入高考分数！")
            } else if (this.GKweici == '') {
                this.$message.warning("请填入高考位次！")
            } else if (this.list2 == '') {
                this.$message.warning("请填入专业类别！")
            } else {
                if (this.list3 == '') this.list3 = '*';
                console.log('本科' + this.GKfenshu + '/' + this.GKweici + '/' + this.list2 + '/' + this.list3 + '/' + this.value)
                this.axios.get("http://101.34.248.53:8181/Map/spring_list/zyzhcx/" + '本科' + '/' + this.GKfenshu + '/' + this.GKweici + '/' + this.list2 + '/' + this.list3 + '/' + this.value)
                    .then(resp => {
                        console.log(resp);
                        this.total = resp.data.length;
                        this.info = resp.data;
                    })
            }
            // }
        },
        get3(){
            //专科
            // if (this.choose_major() == 2) {
            if (this.GKfenshu == '') {
                this.$message.warning("请填入高考分数！")
            } else if (this.GKweici == '') {
                this.$message.warning("请填入高考位次！")
            } else if (this.list2 == '') {
                this.$message.warning("请填入专业类别！")
            } else {
                console.log('专科' + '/' + this.GKfenshu + '/' + this.GKweici + '/' + this.list2 + '/' + this.list3 + '/' + this.value)
                this.axios.get("http://101.34.248.53:8181/Map/spring_list/zyzhcx/" + "专科" + '/' + this.GKfenshu + '/' + this.GKweici + '/' + this.list2 + '/' + this.list3 + '/' + this.value)
                    .then(resp => {
                        console.log(resp);
                        this.total = resp.data.length;
                        this.info = resp.data;
                    })
            }
            // }
        },
        //初始化
        get2() {
            this.axios.get("http://101.34.248.53:8181/Map/spring_list/zyzhcx/" + '本科' + '/' + this.GKfenshu1 + '/' + this.GKweici1 + '/' + this.list22 + '/' + this.list33 + '/' + this.value1).then(resp => {
                console.log(resp);
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
        panduan1() {
            this.panduan = true;
            this.add = "普通一段";
            console.log(this.panduan)
            this.$message.success("已选择本科")
        },
        panduan2() {
            this.panduan = false;
            this.add = "普通二段";
            this.$message.success("已选择专科")
        },
    },
    created() {
        this.get2();
        // console.log(this.num_dialog);
    },
}
</script>

<style scoped>
.el-main{
    margin: 0;
    padding: 0;
}

.box-card {
    width: 100vw;
    margin: 0 auto;
    background-color: transparent;
    border: 0 solid transparent;
}

.box-card >>> .el-card__header{
    border: 0 solid transparent;
}

.box-card >>> .el-card__body{
    margin: 0!important;
    padding: 0!important;
    border: 0 solid transparent;
}

.box-card2 {
    width: 100vw;
    margin-top: 10px;
}

.width_form {
    margin-left: 10px;
    width: 300px;
}

.a {
    text-decoration: none;
    font-size: 18px;
    color: #5e402f;
}
.b {
    text-decoration: none;
    font-size: 19px;
    color: #5e402f;
}
.b:hover{
    text-decoration: none;
    font-size: 19px;
    color: #ff5b00;
}

.Fill_size {
    /*font:bolder 18px "楷体";*/
    font-size: 20px;
}

.size_t1 {
    font-size: 22px;
}

#check-box{
    width: 50vw;
    padding-left: 50px;
    margin: -15px auto 10px auto;
    /*border: 1px solid red;*/
    text-align: left;
}

#form-box{
    display: flex;
    justify-content: center;
    align-items: center;
    /*border: 1px solid blue;*/
    margin-left: 3vw;
    position: relative;
}

#tool-box{
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%,-280%);
}
</style>