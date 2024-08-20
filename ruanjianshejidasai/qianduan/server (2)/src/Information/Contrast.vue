<template>
    <div>
        <div class="big_title">
            院校对比
        </div>
        <div class="input-box">
            <el-autocomplete
                class="inline-input"
                v-model="search_data"
                :fetch-suggestions="searchData"
                placeholder="输入院校直接添加"
                @select="handleSelect">
            </el-autocomplete>

            <el-button type="warning" @click="clearAllData">重置</el-button>
        </div>
        <div class="test-box">
            <div class="box-item" v-for="(item,index) in contrast_data" :key="index">
                <div class="logo-tit-box" @click="goToSchool(item.sid)">
                    <div class="class_logo">
                        <img v-if="item.logo_img" :src="item.logo_img" >
                        <span v-else>学校logo</span>
                    </div>
                    <div class="cls-tit" >{{ item.school_name }}</div>
                </div>
                <div class="other_msg">

                    <div class="cls-type">
                        <span class="item-type" v-for="(name,index) in item['type_arr']" :key="index">{{ name }}</span>
                    </div>

                    <el-divider></el-divider>

                    <div class="cls-ade">
                        <div>
                            <span>
                                <i class="el-icon-timer"></i>
                                成立时间
                            </span>
                            <span>{{ item.time }}</span>
                        </div>

                        <div>
                            <span>
                                <i class="el-icon-office-building"></i>
                                隶属于
                            </span>
                            <span>{{ item.member }}</span>
                        </div>

                        <div>
                            <span>
                                <i class="el-icon-location-information"></i>
                                地区
                            </span>
                            <span>{{ item.address }}</span>
                        </div>

                        <div>
                            <span>
                                <i class="el-icon-place"></i>
                                占地面积
                            </span>
                            <span>{{ item.zhandi }}</span>
                        </div>

                        <div>
                            <span>
                                <i class="el-icon-data-line"></i>
                                考研升学率
                            </span>
                            <span v-if="Boolean(item.shengxue)" style="color: #67C23A">{{ item.shengxue }}%</span>
                        </div>

                        <div>
                            <span>
                                <i class="el-icon-s-custom"></i>
                                硕士点
                            </span>
                            <span v-if="item.shuoshi" class="yes">有硕士点</span>
                            <span v-else class="no">无硕士点</span>
                        </div>

                        <div>
                            <span>
                                <i class="el-icon-s-custom"></i>
                                博士点
                            </span>
                            <span v-if="item.boshi" class="yes">有博士点</span>
                            <span v-else class="no">无博士点</span>
                        </div>
                    </div>

                    <el-divider></el-divider>

                    <div class="sex">
                        <div>
                            <div class="sex-img">
                                <img src="../assets/nan.png" alt="">
                            </div>
                            <div class="sex-pro">
                                <span v-if="!Boolean(item.nan)">暂无数据</span>
                                <el-progress :percentage="item.nan" v-else></el-progress>
                            </div>
                        </div>
                        <div>
                            <div class="sex-img">
                                <img src="../assets/nv.png" alt="">
                            </div>
                            <div class="sex-pro">
                                <span v-if="!Boolean(item.nv)">暂无数据</span>
                                <el-progress :percentage="item.nv" color="#e6a23c" v-else></el-progress>
                            </div>
                        </div>
                    </div>

                    <el-divider></el-divider>

                    <div class="cls-table">
                        <el-table
                            :data="item.all_scores"
                            style="width: 100%">
                            <el-table-column prop="type" label="类型"></el-table-column>
                            <el-table-column prop="scores" label="最低分"></el-table-column>
                            <el-table-column prop="rank" label="最低位次"></el-table-column>
                        </el-table>
                    </div>
                </div>

                <el-popconfirm title="是否删除该条记录？" @confirm="deleteOneSchool(item,index)">
                    <div class="delete_but" slot="reference">
                        ╳
                    </div>
                </el-popconfirm>
            </div>
        </div>


    </div>
</template>

<script>
export default {
    name: "Contrast",
    data(){
        return{
            baseurl:'',

            search_data:'',

            // 获得对比数据（默认全为空）
            contrast_data:[{}, {}, {}, {}],

            // 设置等待时间
            timeOut:''
        }
    },
    methods:{
        // 获取所有院校数据
        async getAllSchool() {
            let arr = []

            await this.axios({
                method:'get',
                url:`${this.baseUrl}/Get_All_School`
            }).then(({data}) => {
                arr = data;
            })

            return arr;
        },

        // ----------------------------------------

        // 获取当前用户的院校对比数据
        getData(){
            let username = this.$cookies.get('user_name');
            this.axios({
                method:'get',
                url:`${this.baseUrl}/Get_School_Contrast/${username}`
            }).then(({data}) => {
                console.log('对比数据',data);

                // 总数组
                let all_arr = [];

                for (const item of data) {
                    if(item === null) {
                        all_arr.push({});
                        continue;
                    }

                    // 处理对比数据 --------------------------------

                    // 处理性质
                    let type_arr = item['school_type_cc'].split(' ');

                    // 硕博点
                    let shuoshi = item['school_shuoshi'] == 1 ? true:false;
                    let boshi = item['school_boshi'] == 1 ? true:false;

                    // 处理本科专科分数线
                    let obj1 = {
                        type:'本科',
                        scores: item['school_min_scores_bk_2021'],
                        rank: item['school_min_rank_bk_2021']
                    }
                    let obj2 = {
                        type:'专科',
                        scores: item['school_min_scores_zk_2021'] == -1 ? "暂无数据" : item['school_min_scores_zk_2021'],
                        rank: item['school_min_rank_zk_2021'] == -1 ? "暂无数据" : item['school_min_rank_zk_2021']
                    }

                    // 合并总数据
                    const one_item = {
                        sid: item['id'],
                        logo_img: `${this.baseUrl}/list/school_logo/${item['school_name']}`,
                        school_name: item['school_name'],
                        type_arr,

                        time: item['school_time'],
                        member: item['school_bumen'],
                        address: item['school_chengshi'],
                        zhandi: item['school_zhandi'],
                        shuoshi,
                        boshi,
                        shengxue: item['school_up'],

                        nan: isNaN(parseInt(item['school_nan'])) ? 0 : parseInt(item['school_nan']),
                        nv: isNaN(parseInt(item['school_nv'])) ? 0 : parseInt(item['school_nv']),

                        all_scores:[
                            obj1,
                            obj2
                        ]
                    }

                    all_arr.push(one_item);
                }

                this.contrast_data = all_arr;
            }).catch((err) => {
                console.log(err.message);
                this.$message.warning('获取院校数据失败，请刷新后重试');
            })
        },

        // 远程搜索数据
        searchData(queryString, cb) {
            this.getAllSchool().then((school_arr) => {
                // 这里通过后端获取所有院校
                let school = school_arr;

                // 进行判断操作（生成数组）
                let result = queryString ? school.filter(this.creatFilter(queryString)) : school.slice(0,50);

                clearTimeout(this.timeOut);
                this.timeOut = setTimeout(() => {
                    cb(result);
                }, 3000 * Math.random());
            })
        },

        // 创建复制浅数组的函数（用于判断输入内容是否存在于数组中）
        creatFilter(str) {
            return (item) => {
                return (item.value.indexOf(str) === 0)
            }
        },

        // 选择某个数据后再向后端请求
        handleSelect(item) {
            let username = this.$cookies.get('user_name');
            let school_id = item['id'];

            this.axios({
                method:'get',
                url:`${this.baseUrl}/Add_School_Contrast/${username}/${school_id}`
            }).then(({data}) => {
                this.$nextTick(() => {
                    if(data.code === '1') {
                        this.$message.success('添加成功');
                        this.getData();
                    } else {
                        this.$message.warning(data.msg);
                    }
                })
            })
        },

        // ----------------------------------------

        // 删除院校
        deleteOneSchool(item,index) {
            // 向后端请求删除某一数据
            if(item.sid === '') {
                this.$message.warning('操作有误')
            } else {
                this.contrast_data.splice(index,1,{});
                this.delToEnd(item.sid);
            }
        },

        // 后端请求（删除）
        delToEnd(sid) {
            let username = this.$cookies.get('user_name');
            this.axios({
                method:'get',
                url:`${this.baseUrl}/Del_School_Contrast/${username}/${sid}`
            }).then(({data})=> {

                if(data.code === '1') {
                    this.$message.success('删除成功');
                } else {
                    this.$message.warning(data.msg);
                }
            })
        },

        // ----------------------------------------

        // 重置数据
        clearAllData() {
            let username = this.$cookies.get('user_name');

            this.$confirm('是否重置所有的数据？', '警告', {
                confirmButtonText:'确定',
                cancelButtonText:'取消',
                type:'warning'
            }).then(() => {
                this.axios({
                    method:'get',
                    url:`${this.baseUrl}/Clear_School_Contrast/${username}`
                }).then(({data}) => {
                    if(data.code === '1') {
                        this.$message.success('重置成功');
                        this.contrast_data = [{}, {}, {}, {}];
                    } else {
                        this.$message.warning(data.msg);
                    }
                })
            })
        },

        // ----------------------------------------

        // 跳转
        goToSchool(id) {
            if(id === '') {
                this.$message.warning('请选择院校');
            } else {
                this.$router.push({
                    path:'/int',
                    query:{
                        id:id
                    }
                })
            }
        }

    },
    created() {
        this.getAllSchool();
        this.getData();
    }
}
</script>

<style scoped>
.big_title {
    font-size: 30px;
    font-weight: 700;
    text-align: center;
}

.input-box {
    margin: 0 auto;
    width: 1300px;
    height: 60px;

    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
}

.input-box >>> .el-input {
    width: 300px;
}

.input-box >>> .el-button {
    margin-left: 10px;
}

.test-box {
    margin: 20px auto 0 auto;
    width: 1300px;
    /*border: 1px solid black;*/

    display: flex;
    justify-content: space-between;
    align-items: flex-start;
}

.box-item {
    box-sizing: border-box;
    padding: 12px;

    width: 24%;
    max-width: 300px;
    min-height: 700px;
    /*background-color: transparent;*/
    background-color: white;
    border-radius: 5px;

    display: flex;
    flex-direction: column;
    align-items: center;

    position: relative;
    transition: box-shadow 300ms linear;
}

.box-item:hover {
    box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
}

/* ------------------------------------------- */
.logo-tit-box:hover .cls-tit{
    cursor: pointer;
    color: #ff5b00;
}

.class_logo {
    width: 150px;
    height: 150px;
    border: 1px dotted #ccc;
    border-radius: 50%;

    color: #ccc;
    display: flex;
    justify-content: center;
    align-items: center;
}

.class_logo img {
    max-width: 100%;
    max-height: 100%;
    object-fit: contain;
}

.class_logo img:hover {
    cursor: pointer;
}

/* ------------------------------------------- */
.other_msg {
    width: 100%;
}

.cls-tit {
    margin-top: 15px;
    width: 100%;
    font-size: 18px;
    font-weight: 700;
    text-align: center;

    transition: color 100ms linear;
}

.cls-type {
    box-sizing: border-box;
    margin-top: 10px;
    padding: 5px;

    min-height: 70px;

    display: flex;
    flex-wrap: wrap;
    flex-direction: row;
    justify-content: space-around;
}

.item-type {
    margin-top: 5px;
    display: inline-block;
    box-sizing: border-box;
    padding: 2px 8px;

    max-height: 21px;

    font-size: 13px;
    color: #409eff;

    background-color: #d9ecff;
    border-radius: 20px;
}

.cls-ade {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

.cls-ade > div {
    height: 40px;
    display: flex;
    align-items: center;
}

.cls-ade span:nth-of-type(1) {
    display: inline-block;
    width: 45%;
    text-align: left;
    letter-spacing: 1px;
}

.cls-ade span:nth-of-type(2) {
    display: inline-block;
    width: calc(100% - 35%);
    text-align: center;
    color: #9f9fce;
    font-size: 12px;
}

.yes {
    color: #409eff!important;
}

.no {
    color: #dc4545 !important;
}

/* ------------------------------------------- */
.sex {
    box-sizing: border-box;
    padding: 10px 0;
}

.sex > div {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
}

.sex > div:last-child {
    margin-top: 15px;
}

.sex-img {
    width: 10%;
    height: 40px;

    display: flex;
    justify-content: center;
    align-items: center;
}

.sex-img img {
    max-height: 100%;
    object-fit: contain;
}

.sex-pro {
    width: 80%;
}

/* ------------------------------------------- */
.cls-table {
    margin-top: 10px;
}

/* ------------------------------------------- */
.delete_but {
    display: inline-block;
    padding: 10px;

    position: absolute;
    right: 0;
    top: 0;

    text-align: center;
    color: #a8a8a8;
    cursor: pointer;
    transition: background-color 300ms linear;
}

.delete_but:hover {
    background-color: rgba(0,0,0,0.04);
}

/* ------------------------------------------- */
.dis_show:after {
    content: '';
    display: block;
    width: 100%;
    height: 100%;

    background-color: rgba(0,0,0,0.5);

    position: absolute;
    top: 0;
    left: 0;


    user-select: none;
    cursor: default;
    z-index: 999;
}
</style>