<template>
    <div id="all">
        <div id="box-1">
            <div class="set">山东省分数线</div>
            <!--                 下拉菜单                       -->
            <el-select v-model="rank_value" placeholder="请选择年份">
                <el-option
                    v-for="item in options"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value">
                </el-option>
            </el-select>
            <!--                 表格                       -->
            <div>
                <el-table :data="table_rank" style="width: 100%" stripe>
                    <el-table-column prop="year" label="年份"></el-table-column>
                    <el-table-column prop="cc" label="录取批次"></el-table-column>
                    <el-table-column prop="school_min_score" label="最低分" :formatter="formatSchool"></el-table-column>
                    <el-table-column prop="school_min_rank" label="最低位次" :formatter="formatSchool"></el-table-column>
                </el-table>
            </div>
        </div>

        <div id="box-2">
            <div class="set">招生计划</div>
            <!--                 下拉菜单                       -->
            <el-select v-model="sel_value" placeholder="请选择年份">
                <el-option
                    v-for="item in options"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value">
                </el-option>
            </el-select>
            <!--                 表格                       -->
            <div id="plan">
                <el-table :data="table_major.slice((curPage-1)*pageSize,curPage*pageSize)" style="width: 100%"
                          stripe>
                    <el-table-column prop="major" label="专业名称" width="250"></el-table-column>
                    <el-table-column prop="menlei" label="学科门类"></el-table-column>
                    <el-table-column prop="plan" label="计划招生"></el-table-column>
                    <el-table-column prop="xuezhi" label="学制"></el-table-column>
                    <el-table-column prop="xvanke" label="选科要求"></el-table-column>
                    <el-table-column prop="lowest_score" label="最低录取分数线"></el-table-column>
                    <el-table-column prop="lowest_ranking" label="最低位次"></el-table-column>
                </el-table>
                <!--                 分页                       -->
                <el-pagination
                    :page-size.sync='pageSize'
                    :current-page.sync='curPage'
                    @size-change="handleSizeChange"
                    @current-change="handleCurrentChange"
                    layout="prev, pager, next"
                    :total="tab_length">
                </el-pagination>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "schoolTable",
    data() {
        return {
            // 公用列表数据 ------------------------------
            // 分数线选择
            rank_value: '',
            // 专业选择
            sel_value: '',

            options: [
                {
                    value: '2021',
                    label: '2021',
                },
                {
                    value: '2022',
                    label: '2022',
                }
            ],

            // 分页 ------------------------------------
            pageSize: 10,
            curPage: 1,
            tab_length: 0,

            // ----------------------------------------
            // 分数线总数组
            text_arr:[],
            // 专业总数组
            major_arr:[],

            table_rank:[],
            table_major:[],
        }
    },
    created() {
        this.getAllData().then(()=>{
            let date = new Date();
            let year = date.getFullYear();
            this.sel_value = year;
            this.rank_value = year;
        })
    },
    methods: {
        // 获取全部数据
        async getAllData(){
            let cid = this.$route.query.id;

            // 专业数据
            await this.axios({
                method:'get',
                url:`http://101.34.248.53:8181/Map/list/Major_score/Byid/${cid}`
            }).then(({data}) => {

                // console.log(data,'专业数据');

                // 这里将年份全部更改
                for (const item of data) {
                    if(item.year === 2020) {
                        item.year = 2021;
                    } else {
                        item.year = 2022;
                    }
                }

                // 进行赋值
                this.major_arr = data;
                this.tab_length = data.length;
            })

            // 分数线数据
            await this.axios({
                method:'get',
                url:`http://101.34.248.53:8181/Map/list/school_score_rank/Byid/${cid}`
            }).then(({data})=>{

                // console.log(data,'分数线');

                for (const item of data) {
                    if(item.year == 2020) {
                        item.year = 2021;
                    } else {
                        item.year = 2022;
                    }
                }

                this.text_arr = data;
            })
        },

        handleSizeChange(val) {
            this.pageSize = val;
        },

        handleCurrentChange(val) {
            this.curPage = val;
        },

        // 根据年份选择专业数据
        yearChooseMajor(year) {
            let arr = [];
            let major = this.major_arr;

            for (const item of major) {
                if(item.year == year) {
                    arr.push(item);
                }
            }

            this.table_major = arr;
        },

        // 根据年份选择分数线
        yearChooseRank(year) {
            let arr = [];
            let rank = this.text_arr;

            for (const item of rank) {
                if(item.year == year) {
                    arr.push(item);
                }
            }

            this.table_rank = arr;
        },

        // ---------------------------------------------
        formatSchool(row, column) {
            let num = row[column.property];
            if (num < 0) {
                return '暂无数据';
            } else {
                return num;
            }
        },
    },
    watch:{
        'rank_value':function () {
            // console.log('已经变动',this.rank_value);
            this.yearChooseRank(this.rank_value);
        },

        'sel_value':function () {
            // console.log('已经变动',this.sel_value);
            this.yearChooseMajor(this.sel_value);
        }
    }
}
</script>

<style scoped>
#all {
    box-sizing: border-box;
    margin: 0;
    position: relative;
    max-height: 1500px;
}

.set {
    margin: 5px 0;
    padding: 5px;
    border-style: solid;
    border-width: 0 0 0 3px;
    border-color: brown;
}

#box-1, #box-2 {
    margin: 0;
    padding: 5px;
    box-shadow: 0px 6px 12px 3px rgba(0, 0, 0, 0.1);
    border-radius: 10px;
    position: relative;
}

#box-2 {
    margin-top: 50px;
    box-shadow: 0px 6px 12px 3px rgba(0, 0, 0, 0.1);
    border-radius: 10px;
}

.el-select {
    position: absolute;
    top: 0;
    right: 20px;
}
</style>
