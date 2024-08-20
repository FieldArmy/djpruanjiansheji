<template>
  <div>

    <el-container>
      <el-main>
        <el-card class="box-card">

          <el-autocomplete
              class="inline-input"
              v-model="states"
              :fetch-suggestions="querySearchAsync"
              placeholder="输入院校直接添加"
              @select="handleSelect">
          </el-autocomplete>
          <el-button type="primary" @click="get()" style="" class="btn1">搜索</el-button>
          <el-button type="text" @click="dialogVisible = true" style="margin-left: 1050px;margin-top: 0px"> 【使用小技巧】
          </el-button>
          <br>
          <br>
          <div>
            <el-container>
              <el-aside>
                <div style="margin-top: -15px">

                  <el-button type="text" style="margin-top: -8px"><h3>专业层次></h3></el-button>
                  <br>
                  <el-button type="text" style="margin-top: -22px"><h3>专业门类></h3></el-button>
                </div>
              </el-aside>

              <el-main style="margin-left: -180px">
                <div>
                  <!--选择本/专科-->
                  <div style="margin-top: -20px">
                    <el-radio-group v-model="button_checked" size="small" >
                      <el-radio-button v-model="button_checked" label="ben" @click.native="change1">本科</el-radio-button>
                      <el-radio-button v-model="button_checked" label="zhuan" @click.native="change2">专科</el-radio-button>
                    </el-radio-group>
                  </div>
                  <!--=本科-->
                  <div style="margin-top: 16px" v-if="choose_major(button_checked) == 1">
                    <el-radio-group v-model="CX.list2" size="small">
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
                    <el-button type="primary" class="btn1" @click="addform111">搜索</el-button>
                  </div>
                  <!--=专科-->
                  <div style="margin-top: 21px" v-if="choose_major(button_checked) == 2">
                    <el-radio-group v-model="CX.list3" size="small">
                      <el-radio-button label="农林牧渔大类"></el-radio-button>
                      <el-radio-button label="资源环境与安全大类"></el-radio-button>
                      <el-radio-button label="能源动力与材料大类"></el-radio-button>
                      <el-radio-button label="土木建筑大类"></el-radio-button>
                      <el-radio-button label="水利大类"></el-radio-button>
                      <el-radio-button label="装备制造大类"></el-radio-button>
                      <el-radio-button label="生物与化工大类"></el-radio-button>
                      <el-radio-button label="食品药品与粮食大类"></el-radio-button>
                      <el-radio-button label="轻工纺织大类"></el-radio-button>
                      <el-radio-button label="交通运输大类"></el-radio-button>
                      <div style="margin-top: 2px">
                        <el-radio-button label="电子与信息大类"></el-radio-button>
                        <el-radio-button label="医药卫生大类"></el-radio-button>
                        <el-radio-button label="财经商贸大类"></el-radio-button>
                        <el-radio-button label="旅游大类"></el-radio-button>
                        <el-radio-button label="文化艺术大类"></el-radio-button>
                        <el-radio-button label="新闻传播大类"></el-radio-button>
                        <el-radio-button label="教育与体育大类"></el-radio-button>
                        <el-radio-button label="公安与司法大类"></el-radio-button>

                      </div>
                      <el-button type="primary" class="btn1" @click="addform222"
                                 style="margin-top: -30px;margin-left: 865px">搜索
                      </el-button>
                    </el-radio-group>
                  </div>

                </div>
              </el-main>
            </el-container>
            <el-dialog title="使用小技巧" :visible.sync="dialogVisible" width="28%">
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
            style="width: 100%"
            :row-style="{height:'100px'}"
        >
          <el-table-column align="center" label="专业信息">
            <el-table-column prop="major_name" align="center" label="专业名称" class="a" style="width: 100px">
              <template slot-scope="scope">
                 <a :href="links+'/s?wd='+scope.row.major_name" target="_blank"> {{ scope.row.major_name }}</a>
              </template>
            </el-table-column>
            <el-table-column prop="cc" align="center" label="层次" class="a" style="width: 100px">
              <template slot-scope="scope">
                <span>{{scope.row.set||button_checked==='ben'?'本科':'专科'}}</span>
              </template>
            </el-table-column>
            <el-table-column prop="major_code" align="center" label="专业代码" class="a">
              <template slot-scope="scope">
                  <span>{{ scope.row.major_code }}</span>
              </template>
            </el-table-column>
            <el-table-column prop="small_type" align="center" label="专业类" class="a">
              <template slot-scope="scope">
                  <span>{{ scope.row.small_type||'无'}}</span>
              </template>
            </el-table-column>
          </el-table-column>
          <el-table-column prop="major_year" align="center" label="修业年限" class="a">
            <template slot-scope="scope">
                <span>{{ scope.row.major_year }}</span>
            </template>
          </el-table-column>

          <el-table-column prop="big_type" align="center" label="门类" class="a">
            <template slot-scope="scope">
                <span>{{ scope.row.big_type }}</span>
            </template>
          </el-table-column>
          <el-table-column prop="academic" align="center" label="学位" class="a">
            <template slot-scope="scope">
                <span>{{ scope.row.academic||'无'}}</span>
            </template>
          </el-table-column>
          <el-table-column  align="center" label="收藏" class="a">
            <template slot-scope="scope">
              <el-button
                  title="收藏"
                  @click="collect(scope.row.major_code)">
                收藏
              </el-button>
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
      // num: 'favor_no',
      states:'',
      button_checked: 'ben',
      dialogVisible: false,
      CX: {
        list2: "",
        list3: "",
      },
      data1: "",
      links:'http://www.baidu.com',
      info: [],
      info2:[],
      info3:[],
      total: 0,
      total1:0,
      total2:0,
      pageSize: 10,  //一页显示多少条
      pageSizes: [5, 10, 15, 20, 50],//每页显示多少条
      currentPage: 1,  //当前位于哪页
      pageCount: 7,   //多少分页按钮
    }
  },
  methods: {
    async getAllMajor() {
      let arr = []
      await this.axios({
        method: 'get',
        url: 'api/students/getdata',
        params: {
          account: this.$cookies.get('user_name'),
          action: 'list_major'
        }
      }).then((resp) => {
        arr = resp.data.major_name;
      })

      return arr;
    },
    querySearchAsync(queryString, cb) {
      this.getAllMajor().then((school_arr)=> {
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
    //表单查询
    get() {
      if (this.states === '') {
        this.$message.error("请输入专业名称！")
      } else {
        axios({
          method:'POST',
          url:'api/students/selectdata',
          data:{
            action:'select_major',
            major_type:[],
            major_name:this.states,
            account:this.$cookies.get('user_name')
          }
        }).then((resp)=>{
          console.log(resp.data.data)
          this.total = resp.data.length;
          this.info = resp.data.data;
          this.$message.success("查找成功！")
        })

      }
    },
   // 单选框查询
    addform111() {
      if (this.CX.list2 == '') {
        this.$message.error("请选择专业门类！")
      } else {
        axios({
          method:'POST',
          url:'api/students/selectdata',
          data:{
            action:'select_major',
            major_set:this.button_checked==='ben'?'本科':'专科',
            major_type:[this.CX.list2],
            major_name:'',
            account:this.$cookies.get('user_name')
          }
        }).then((resp)=>{
          console.log(resp.data.data)
          this.total = resp.data.length;
          this.total1=this.total;
          this.info = resp.data.data;
          this.info2=resp.data.data;
          this.$message.success("查找成功！")
          this.CX.list2=''
        })
      }
    },
    addform222() {
      if (this.CX.list3 == '') {
        this.$message.error("请选择专业门类！")
      } else {
        axios({
          method:'POST',
          url:'api/students/selectdata',
          data:{
            action:'select_major',
            major_set:this.button_checked==='ben'?'本科':'专科',
            major_type:[this.CX.list3],
            major_name:'',
            account:this.$cookies.get('user_name')
          }
        }).then((resp)=>{
          console.log(resp.data.data)
          this.total = resp.data.length;
          this.total2=this.total;
          this.info = resp.data.data;
          this.info3=resp.data.data;
          this.$message.success("查找成功！")
          this.CX.list3=''
        })
      }
    },
    //初始化列表调用此接口
    get3() {
      axios({
        method:'POST',
        url:'api/students/selectdata',
        data:{
          action:'select_major',
          major_set:'本科',
          major_type:['工学'],
          major_name:'',
          account:this.$cookies.get('user_name')
        }
      }).then((resp)=>{
        console.log(resp.data.data)
        this.total = resp.data.length;
        this.info = resp.data.data;
        // this.$message.success("查找成功！")
        this.CX.list3=''
      })
    },
    change1() {
      // this.total=this.total1
      this.info=this.info2
    },
    change2() {
      // this.total=this.total2
      this.info=this.info3
    },
    choose_major(val) {
      if (val === 'ben')
        return 1;
      else {
        return 2;
      }
    },

    // 收藏
    collect(id) {
      axios({
        method:'POST',
        url:'api/students/collectdata',
        data:{
          action:'collect_major',
          major_set:this.button_checked==='ben'?'本科':'专科',
          major_id:id,
          // account:'12345678'
          account:this.$cookies.get('user_name')
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
    enterSearchMember() {
      this.get()
    },
  },
  created() {
    this.get3();
    const _this = this;
    document.onkeydown = function (e) {
      var key = window.event.keyCode;
      if (key == 13) {
        _this.enterSearchMember();
      }
    }
  }
}
</script>
<style scoped>
a{
  text-decoration: none;

}
a:hover{
  color: red;
  font-size: 16px;
  font-weight: 700;
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

.btn1 {
  margin-left: 30px;
  min-width: 85px;
}

.box-card {
  /*height: 230px;*/
  /*width: 1574px;*/
  margin: auto;
  margin-top: -15px;
}

.el-table {
  width: 1574px;
  margin: auto;
  margin-top: 35px;
}

.favor_no {
  width: 50px;
  height: 50px;
  outline: 0;
  background-color: transparent;
  border: 0 solid transparent;
  background-image: url("../assets/favorite.png");
}

.favor_no:active {
  outline: 0;
  background-image: url("../assets/favorite.png");
  background-position: 50px 0;
}

.favor_yes {
  width: 50px;
  height: 50px;
  outline: 0;
  background-color: transparent;
  border: 0 solid transparent;
  background-image: url("../assets/favorite.png");
  background-position: 50px 0;
}

.btn11 {
  background-color: #0077ff;
}
</style>
