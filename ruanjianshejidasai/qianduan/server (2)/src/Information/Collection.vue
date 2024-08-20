<template>
    <div>
        <br>
        <el-tabs v-model="activeName" style="background-color: white"   type="card">

            <el-tab-pane label="学校收藏" name="first">
                <el-table border :data="info2" style="width: 100%"
                          stripe>
                    <el-table-column align="center" label="校徽" prop="school_name" class="table-h">
                        <template slot-scope="scope">
                                <img style="width: 50%" :src="petImage(scope.row.name)"/>
                        </template>
                    </el-table-column>

                    <el-table-column prop="name" align="center" label="名称" width="180" class="table-h">
                        <template slot-scope="scope">
                                <span>{{ scope.row.name }}</span>
                        </template>
                    </el-table-column>
                  <el-table-column prop="college_id" align="center" label="院校代码" width="180" class="table-h">
                    <template slot-scope="scope">
                      <span>{{ scope.row.college_id }}</span>
                    </template>
                  </el-table-column>
                    <el-table-column prop="Type_college" align="center" label="学校类型" class="table-h">
                        <template slot-scope="scope">
                                <span>{{ scope.row.Type_college}}</span>
                        </template>
                    </el-table-column>

                    <el-table-column prop="address" align="center" label="地址" class="table-h">
                        <template slot-scope="scope">
                                <span>{{ scope.row.address }}</span>
                        </template>
                    </el-table-column>

                    <el-table-column prop="shoucang" align="center" label="操作" class="a">
                        <template slot-scope="scope">
                            <el-button
                                @click="deleted2(scope.row.college_id)">
                                取消收藏
                            </el-button>
                        </template>
                    </el-table-column>
                </el-table>
                <el-pagination
                    :page-size.sync="pageSize2"
                    :page-sizes="pageSizes2"
                    :current-page.sync="currentPage2"
                    :pager-count="pageCount2"
                    background
                    style="margin-top: 6px"
                    layout="sizes,prev, pager, next,jumper,->,total"
                    :total=total2
                >
                </el-pagination>
            </el-tab-pane>

          <el-radio-group v-model="button_checked" size="small" @change="get_major" style="margin-left: 5px;margin-bottom: 5px;">
            <el-radio-button v-model="button_checked" label="ben">本科</el-radio-button>
            <el-radio-button v-model="button_checked" label="zhuan">专科</el-radio-button>
          </el-radio-group>
            <el-tab-pane label="专业收藏" name="second">
                <el-table
                    border
                    :data="info1"
                    stripe
                    style="width: 100%;"
                    :row-style="{height:'100px'}"
                >

                    <el-table-column prop="major_name" align="center" label="专业名称" class="a" style="width: 100px">
                        <template slot-scope="scope">
                                <span>{{ scope.row.major_name }}</span>
                        </template>
                    </el-table-column>
                    <el-table-column prop="cc" align="center" label="层次" class="a" style="width: 100px">
                        <template slot-scope="scope">
                                <span v-if="scope.row.major_year==='三年'">专科</span>
                          <span v-else >本科</span>
                        </template>
                    </el-table-column>
                    <el-table-column prop="major_code" align="center" label="专业代码" class="a">
                        <template slot-scope="scope">
                                <span>{{ scope.row.major_code }}</span>
                        </template>
                    </el-table-column>
                    <el-table-column prop="small_type" align="center" label="专业类" class="a">
                      <template slot-scope="scope">
                                <span>{{ scope.row.small_type ||'无'}}</span>
                        </template>
                    </el-table-column>
                  <el-table-column prop="big_type" align="center" label="门类" class="a">
                    <template slot-scope="scope">
                      <span>{{ scope.row.big_type }}</span>
                    </template>
                  </el-table-column>
                    <el-table-column prop="major_year" align="center" label="修业年限" class="a">
                      <template slot-scope="scope">
                                <span>{{ scope.row.major_year }}</span>
                        </template>
                    </el-table-column>
                    <el-table-column prop="academic" align="center" label="学位" class="a">
                        <template slot-scope="scope">
                                <span>{{ scope.row.academic ||'无'}}</span>
                        </template>
                    </el-table-column>
                    <el-table-column prop="shoucang" align="center" label="取消收藏" class="a">
                        <template slot-scope="scope">
                            <el-button
                                @click="deleted(scope.row.major_code)">
                                取消收藏
                            </el-button>
                        </template>
                    </el-table-column>
                </el-table>
                <el-pagination
                    :page-size.sync="pageSize1"
                    :page-sizes="pageSizes1"
                    :current-page.sync="currentPage1"
                    :pager-count="pageCount1"
                    style="margin-top: 6px"
                    background
                    layout="sizes,prev, pager, next,jumper,->,total"
                    :total=total1
                >
                </el-pagination>
            </el-tab-pane>

        </el-tabs>
    </div>
</template>

<script>
import axios from "axios";

export default {
    name: "Collection",
    data() {
        return {
          button_checked:'ben',
            username: null,
            activeName: 'first',
            info1: [],  //专业信息
            info2: [],  //学校信息
            total1: 0,
            total2: 0,
            total3: 0,
            pageSize1: 5,  //一页显示多少条
            pageSize2: 5,  //一页显示多少条
            pageSize3: 5,  //一页显示多少条
            pageSizes1: [5, 10, 15, 20, 25],//每页显示多少条
            pageSizes2: [5, 10, 15, 20, 25],//每页显示多少条
            pageSizes3: [5, 10, 15, 20, 25],//每页显示多少条
            currentPage1: 1,  //当前位于哪页
            currentPage2: 1,  //当前位于哪页
            currentPage3: 1,  //当前位于哪页
            pageCount1: 7,   //多少分页按钮
            pageCount2: 7,   //多少分页按钮
            pageCount3: 7,   //多少分页按钮
        }
    },
    methods: {

        // 获取收藏的专业
        get_major() {
          axios({
            method:'GET',
            url:'api/students/listcollection',
            params:{
              // this.$cookies.get('user_name');
              action:'list_major',
              // account:'12345678',
              account:this.$cookies.get('user_name'),
              pagesize:10000,
              pagenum:1,
              major_set:this.button_checked==='ben'?'本科':'专科'
            }
          }).then((resp)=>{
            this.info1 = resp.data.data
            // console.log(this.info1.length)
            this.total1 = resp.data.length
          })
        },
        //获取收藏的学校
        get_school() {
          axios({
            method:'GET',
            url:'api/students/listcollection',
            params:{
              // this.$cookies.get('user_name');
              action:'list_college',
              // account:'12345678',
              account:this.$cookies.get('user_name'),
              pagesize:10000,
              pagenum:1,
              major_set:''
            }
          }).then((resp)=>{
            this.info2 = resp.data.data
          })
        },
        //校徽
      petImage(name) {
        return 'api/students/jpeg/' + name
      },
        //删除收藏
        deleted(id) {
          axios({
            method:'POST',
            url:'api/students/delcollection',
            data:{
              action:'del_major',
              major_id:id,
              major_set:this.button_checked==='ben'?'本科':'专科',
              // account:'12345678'
              account:this.$cookies.get('user_name'),
            }
          }).then((resp)=>{
            if(resp.data.ret === 0){this.$message.info("取消成功！"); this.get_major();}
          })
        },
        deleted2(id) {
          axios({
            method:'POST',
            url:'api/students/delcollection',
            data:{
              action:'del_college',
              college_id:id,
              // account:'12345678'
              account:this.$cookies.get('user_name'),
            }
          }).then((resp)=>{
            if(resp.data.ret === 0){this.$message.info("取消成功！"); this.get_school()}
          })
        },

    },
    created() {
        this.get_major()
        this.get_school()
    },
}
</script>

<style scoped>
.table-h {
    text-decoration: none;
    font-size: 18px;
    color: #5e402f;
}
.a {
    text-decoration: none;
    font-size: 19px;
    color: #5e402f;
}
.aa2{
    text-decoration: none;
    font-size: 19px;
    color: #5e402f;
}

.a:hover {
    text-decoration: none;
    font-size: 19px;
    color: #ff5b00;
}
</style>
