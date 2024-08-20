<template>
    <div class="div11">
        <el-container>
            <el-main>

                <el-card class="box-card">
<!--                    <el-input v-model="data2" placeholder="请输入学校名称" style="width:250px;"></el-input>-->
                      <el-autocomplete
                      class="inline-input"
                      v-model="states"
                      :fetch-suggestions="querySearchAsync"
                      placeholder="输入院校直接添加"
                      @select="handleSelect">
                  </el-autocomplete>

<!--                  <el-select-->
<!--                      key="123"-->
<!--                      v-model="value"-->
<!--                      filterable-->
<!--                      change-->
<!--                      remote-->
<!--                      placeholder="请输入关键词"-->
<!--                      :remote-method="remoteMethod"-->
<!--                      :loading="loading"-->
<!--                  ref="Select">-->
<!--                    <el-option-->
<!--                        v-for="(item,index) in options"-->
<!--                        :key="index"-->
<!--                        :label="item.label"-->
<!--                        :value="item.value">-->
<!--                      {{item.label.slice(6)}}-->
<!--                    </el-option>-->
<!--                  </el-select>-->

                    <el-button type="primary" @click="get()" class="btn1" @keyup.enter="enterSearchMember">搜索</el-button>
                    <el-button type="text" @click="dialogVisible = true" style="margin-left: 1050px;margin-top: -30px"> 【使用小技巧】
                    </el-button>
                    <div>
                        <el-container>
                            <el-aside width="120px">
                                <el-button type="text" style="margin-top: -7px;margin-left: 0px"><h3>院校地区></h3></el-button>
                                <el-button type="text" style="margin-top: 40px;margin-left: 0px"><h3>院校类型></h3></el-button>
                                <el-button type="text" style="margin-top: -20px;margin-left: 0px"><h3>办学类型></h3></el-button>

                            </el-aside>
                            <el-main>
                                <div style="margin-top: -4px">
                                    <div>
                                        <!--所属城市-->
                                        <div style="margin-top: -5px">
                                            <el-radio-group v-model="CX.list1" size="small">
                                                <el-radio-button label="山东"></el-radio-button>
                                                <el-radio-button label="北京"></el-radio-button>
                                                <el-radio-button label="天津"></el-radio-button>
                                                <el-radio-button label="河北"></el-radio-button>
                                                <el-radio-button label="山西"></el-radio-button>
                                                <el-radio-button label="辽宁"></el-radio-button>
                                                <el-radio-button label="吉林"></el-radio-button>
                                                <el-radio-button label="上海"></el-radio-button>
                                                <el-radio-button label="江苏"></el-radio-button>
                                                <el-radio-button label="浙江"></el-radio-button>
                                                <el-radio-button label="安徽"></el-radio-button>
                                                <el-radio-button label="福建"></el-radio-button>
                                                <el-radio-button label="江西"></el-radio-button>
                                                <el-radio-button label="河南"></el-radio-button>
                                                <el-radio-button label="湖南"></el-radio-button>
                                                <el-radio-button label="湖北"></el-radio-button>

                                                <div style="margin-top: 2px">
                                                  <el-radio-button label="广东"></el-radio-button>
                                                  <el-radio-button label="广西"></el-radio-button>
                                                  <el-radio-button label="黑龙江"></el-radio-button>
                                                  <el-radio-button label="内蒙古"></el-radio-button>
                                                  <el-radio-button label="海南"></el-radio-button>
                                                  <el-radio-button label="重庆"></el-radio-button>
                                                    <el-radio-button label="四川"></el-radio-button>
                                                    <el-radio-button label="贵州"></el-radio-button>
                                                    <el-radio-button label="云南"></el-radio-button>
                                                    <el-radio-button label="西藏"></el-radio-button>
                                                    <el-radio-button label="陕西"></el-radio-button>
                                                    <el-radio-button label="甘肃"></el-radio-button>
                                                    <el-radio-button label="青海"></el-radio-button>
                                                    <el-radio-button label="宁夏"></el-radio-button>
                                                    <el-radio-button label="新疆"></el-radio-button>
                                                </div>
                                            </el-radio-group>
                                        </div>
                                        <!--院校类型-->
                                        <div style="margin-top: 20px">
                                            <el-radio-group v-model="CX.list2" size="small">
                                                <el-radio-button label="综合类"></el-radio-button>
                                                <el-radio-button label="理工类"></el-radio-button>
                                                <el-radio-button label="医药类"></el-radio-button>
                                                <el-radio-button label="农林类"></el-radio-button>
                                                <el-radio-button label="师范类"></el-radio-button>
                                                <el-radio-button label="语言类"></el-radio-button>
                                                <el-radio-button label="财经类"></el-radio-button>
                                                <el-radio-button label="政法类"></el-radio-button>
                                                <el-radio-button label="体育类"></el-radio-button>
                                                <el-radio-button label="艺术类"></el-radio-button>
                                                <el-radio-button label="民族类"></el-radio-button>
                                                <el-radio-button label="军事类"></el-radio-button>
                                            </el-radio-group>
                                        </div>
                                        <!--办学类型-->
                                        <div style="margin-top: 20px">
                                            <el-radio-group v-model="CX.list3" size="small">
                                                <el-radio-button label="普通本科"></el-radio-button>
                                                <el-radio-button label="公办"></el-radio-button>
                                                <el-radio-button label="民办"></el-radio-button>
                                                <el-radio-button label="专科（高职）"></el-radio-button>
                                              <el-radio-button :label="985"></el-radio-button>
                                              <el-radio-button :label="211"></el-radio-button>
                                            </el-radio-group>
                                        </div>
                                        <!--院校特色-->
                                            <el-button type="primary" @click="get2()" style="margin-top: 8px;" class="btn1">搜索</el-button>

                                    </div>
                                </div>

                            </el-main>
                        </el-container>
                    </div>

                    <el-dialog title="使用小技巧" :visible.sync="dialogVisible" width="28%">
                        <h3 style="margin-top: -20px">☆ 输入正确的学校名称，可精准搜索该学校</h3>
                        <h3>☆ 选择对应条件可搜索相应的学校</h3>
                        <h3>☆ 两大搜索模块独立运行</h3>
                        <h3>☆ 院校所属、院校类型、办学类型、院校特色都为必选项</h3>
                    </el-dialog>
                </el-card>
                <br>
                <br>

                <!-- 表格数据 -->
                <el-table border :data="info.slice((currentPage-1)*pageSize,currentPage*pageSize)" style="width: 100%;min-width: 1200px" stripe>
                    <el-table-column align="center" label="学校">
                        <el-table-column align="center" label="校徽" prop="school_name" class="table-h">
                            <template slot-scope="scope">
                                    <a :href="links+'/s?wd='+scope.row.name" target="_blank"><img style="width: 50%" :src="petImage(scope.row.name)"/></a>
                            </template>
                        </el-table-column>

                        <el-table-column prop="school_name" align="center" label="学校名称" width="180" class="table-h">
                            <template slot-scope="scope">
                                    <span>{{ scope.row.name }}</span>
                            </template>
                        </el-table-column>
                      <el-table-column prop="school_code" align="center" label="学校代码" width="180" class="table-h">
                        <template slot-scope="scope">
                          <span>{{ scope.row.college_id }}</span>
                        </template>
                      </el-table-column>
                    </el-table-column>
                    <el-table-column label="详细信息" align="center">
                        <el-table-column prop="school_type_cc" align="center" label="学校性质" class="table-h">
                            <template slot-scope="scope">
                                    <span>{{ scope.row.Type_college}}</span>
                            </template>
                        </el-table-column>



                        <el-table-column prop="school_chengshi" align="center" label="地址" class="table-h">
                            <template slot-scope="scope">
                                    <span>{{ scope.row.address }}</span>
                            </template>
                        </el-table-column>

                        <el-table-column  align="center" label="操作" class="a">
                            <template slot-scope="scope">
                                <el-button type="primary" title="收藏" @click="collect(scope.row.college_id)">
                                    收藏
                                </el-button>
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
                        style="margin-top: 6px"
                        layout="sizes,prev, pager, next,jumper,->,total"
                        :total=total
                    >
                    </el-pagination>
                </div>

            </el-main>
        </el-container>
    </div>
</template>

<script>
import axios from "axios";

export default {
    name: "list2",
    data() {

        return {
          links:'http://www.baidu.com',
          states:'',
          loading: false,
            dialogVisible: false,
            state: "",
            data3: "中国",//隐藏的表单默认显示的内容
            info: [],
            CX: {
                list1: "",
                list2: "",
                list3: "",
                list4: "",
            },
            total: 0,
            pageSize: 10,  //一页显示多少条
            pageSizes: [5, 10, 15, 20, 50],//每页显示多少条
            currentPage: 1,  //当前位于哪页
            pageCount: 7,   //多少分页按钮
        }
    },
    //搜索
    methods: {
      async getAllSchool() {
        let arr = []
        await this.axios({
          method: 'get',
          url: 'api/students/getdata',
          params: {
            account: this.$cookies.get('user_name'),
            action: 'list_college'
          }
        }).then((resp) => {
          arr = resp.data.college_name;
        })

        return arr;
      },
      querySearchAsync(queryString, cb) {
        this.getAllSchool().then((school_arr)=> {
          let school = school_arr
          let results = queryString ? school.filter(this.createStateFilter(queryString)) : school.slice(0, 30);
          clearTimeout(this.timeout);
          console.log(results)
          this.timeout = setTimeout(() => {
            // cb(results);
            console.log(cb(results))
          }, 3000 * Math.random());
        })
      },
      createStateFilter(queryString) {
        return (state) => {
          return (state.value.toLowerCase().indexOf(queryString.toLowerCase()) === 0);
        };
      },

      // 选择某个数据后再向后端请求
      handleSelect(item) {
        console.log('@@', item)
      },



        get() {
            if (this.states=== '') {
                this.$message.error("请输入校名！")
            } else {
                axios({
                  method:'POST',
                  url:'api/students/selectdata',
                  data:{
                    action:'select_college',
                    college_address:'',
                    college_name:this.states,
                    college_type:[],
                    account:this.$cookies.get('user_name')
                  }
                }).then((resp)=>{
                  console.log(resp.data)
                  this.info = resp.data.data;
                  this.total = resp.data.length;
                  this.$message.success("搜索成功！");
                })


            }
        },
        //复选框搜索
        get2() {

            if (this.CX.list1 == '') {
                this.$message.error("请选择所属地区！");
            } else if (this.CX.list2 == '') {
                this.$message.error("请选择院校类型！");
            } else if (this.CX.list3 == '') {
                this.$message.error("请选择办学类型！");
            }  else {
              axios({
                method:'POST',
                url:'api/students/selectdata',
                data:{
                  action:'select_college',
                  college_address:this.CX.list1,
                  college_name:'',
                  college_type:[this.CX.list2,this.CX.list3],
                  account:this.$cookies.get('user_name')
                }

              }).then((resp)=>{
                // console.log(resp.data.data)
                this.info = resp.data.data;
                this.total = resp.data.length;
                this.$message.success("搜索成功！");
              }).catch(()=>{
                console.log(this.CX.list1)
                console.log(this.CX.list2)
              })
            }
        },
        //初始化的时候调用的
        get3() {
          axios({
            method:'POST',
            url:'api/students/selectdata',
            data:{
              action:'select_college',
              college_address:'山东',
              college_name:'',
              college_type:[],
              account:this.$cookies.get('user_name')
            }

          }).then((resp)=>{
            this.info = resp.data.data;
            this.total = resp.data.length;
          }).catch(()=>{
            console.log(this.CX.list1)
            console.log(this.CX.list2)
          })
        },
        enterSearchMember() {
            this.get()
        },
        //校徽图片
        petImage(name) {
          return 'api/students/jpeg/' + name
        },
        collect(id) {
          axios({
            method:'POST',
            url:'api/students/collectdata',
            data:{
              action:'collect_college',
              college_id:id,
              account:this.$cookies.get('user_name')
              // account:'12345678'
            }
          }).then((resp)=>{
            console.log(resp.data)
              if(resp.data.ret===0){
                this.$message.success("收藏成功")
              }
              if(resp.data.ret===1){
                this.$message.error("重复收藏！！")
              }
          })
        },
    },

    //项目初始化时显示的内容
    created() {
        this.get3();
        const _this = this;
        document.onkeydown = function (e) {
            var key = window.event.keyCode;
            if (key == 13) {
                _this.enterSearchMember();
            }
        }
    },


}
</script>

<style scoped>
.body {
    margin: auto;
}

.btn1 {
    min-width: 85px;
    margin-left: 30px;
}

.text {
    font-size: 14px;
}

.table-h {
    text-decoration: none;
    font-size: 18px;
    color: #5e402f;
}

.div11 {

}

.box-card {
    /*height: 340px;*/
    /*width: 1574px;*/
    margin: auto;
    margin-top: -15px;
    min-width: 1200px;
}

.el-table {
    width: 1574px;
    margin: auto;
    margin-top: -10px;
}

.a {
    text-decoration: none;
    font-size: 19px;
    color: #5e402f;
}

.a:hover {
    text-decoration: none;
    font-size: 19px;
    color: #ff5b00;
}

.bg_color {
    background-color: #defcfc;
}
</style>
