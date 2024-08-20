<template>
  <el-container>
    <el-header style="height:20vh; padding: 0;">
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
                    <el-radio-button label="all">全部</el-radio-button>
                    <el-radio-button label="ben">本科</el-radio-button>
                    <el-radio-button label="zhuan">专科</el-radio-button>
                </el-radio-group>
              </div>

                <!--全部-->
                <div style="margin-top: 22px" v-if="choose_major(button_checked) == 0">
                    <el-select placeholder="请选择">
                        <el-option></el-option>
                    </el-select>
                </div>
              <!--本科-->
              <div style="margin-top: 22px" v-if="choose_major(button_checked) == 1">
                  <el-select v-model="value" placeholder="请选择">
                      <el-option
                          v-for="item in major_ben"
                          :key="item.value"
                          :label="item.label"
                          :value="item.value">
                      </el-option>
                  </el-select>
              </div>
              <!--=专科-->
              <div style="margin-top: 22px" v-if="choose_major(button_checked) == 2">
                  <el-select v-model="value" placeholder="请选择">
                      <el-option
                          v-for="item in major_zhuan"
                          :key="item.value"
                          :label="item.label"
                          :value="item.value">
                      </el-option>
                  </el-select>
              </div>
            </div>
          </div>
        </div>
      </el-card>
    </el-header>
    <el-main>
        <!--生成教师信息-->
      <div id="th-box">
        <template v-for="(num,index) in teachers">
          <div
              class="box"
              v-show="choose_teacher(num.major)"
              :key="index">
            <img :src="num.sex == '男'?top_man:top_woman">
            <div class="teacher-intro">
              <p>姓名：{{ num.name }}</p>
              <p id="question">被咨询次数：{{ num.num }}</p>
              <p>年龄：{{ num.age }}</p>
              <p>性别：{{ num.sex }}</p>
              <p>擅长：{{ num.major }}</p>
              <el-button type="primary" plain @click="teacher_introduce(index)">个人简介</el-button>
              <el-button type="success" plain @click="zixun(index)" class="zixun_button">点击咨询</el-button>
            </div>
          </div>
        </template>
      </div>
    </el-main>
  </el-container>
</template>

<script>
export default {
  name: "teacher",
  data() {
    return {
        button_checked: 'all',
        top_man: require("../assets/nan2.png"),
        top_woman: require("../assets/nv2.png"),
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
            {value:'农林牧渔',label:'农林牧渔'},
            {value:'资源环境与安全',label:'资源环境与安全'},
            {value:'能源动力与材料',label:'能源动力与材料'},
            {value:'土木建筑',label:'土木建筑'},
            {value:'水利',label:'水利'},
            {value:'装备制造',label:'装备制造'},
            {value:'生物与化工',label:'生物与化工'},
            {value:'食品药品与粮食',label:'食品药品与粮食'},
            {value:'轻工纺织',label:'轻工纺织'},
            {value:'交通运输',label:'交通运输'},
            {value:'电子信息',label:'电子信息'},
            {value:'医药卫生',label:'医药卫生'},
            {value:'旅游',label:'旅游'},
            {value:'文化艺术',label:'文化艺术'},
            {value:'新闻传播',label:'新闻传播'},
            {value:'教育与体育',label:'教育与体育'},
            {value:'公安与司法',label:'公安与司法'},
        ],
        teachers: [],
        value: '哲学',
    }
  },
  methods: {
    // axios获取数据
    get_data() {
      this.axios.get('http://101.34.248.53:8181/Map/list_teacher')
          .then(resp => {
            this.teachers = resp.data;
          });
    },

    // 判断选择的是本科还是专科，来进行专业的筛选
    choose_major(val) {
      if (val == 'all')
          return 0;
      else if (val == 'ben')
          return 1;
      else
          return 2;
    },

    //根据老师的擅长进行归类
    choose_teacher(major) {
      if (this.button_checked == 'all')
        return true;

      else if (major == this.value) {
        return true;
      }

      else {
        return false;
      }
    },

    // 右侧弹出老师个人介绍的气泡
    teacher_introduce(index) {
      this.$notify({
        title: '老师个人介绍',
        message: this.teachers[index].info,
        duration: 10000,
      })
    },

    //向后台传递数据
    file_post(index) {
      let num = this.teachers[index].id;
      this.axios({
        url: 'http://101.34.248.53:8181/Map/teacher',
        method: 'post',
        params: {
          'id': num
        },
      });

      //实时更新
      this.get_data();
    },

    //咨询函数，判断是否确定咨询
    zixun(index) {
      this.$confirm('是否要咨询此老师？', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
      }).then(() => {
        //实时更新
        this.get_data();

        //换行操作
        let arr = ["老师的电话：" + this.teachers[index].tel, "老师的邮箱：" + this.teachers[index].email];
        arr = arr.join('<br /><br />');
        //弹出message对话框
        this.$message({
          type: 'success',
          message: arr,
          duration: 15000,
          showClose: true,
          dangerouslyUseHTMLString: true
        });

        //向后台传递参数
        this.file_post(index);
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '已取消咨询'
        });
      })
    },
  },
  created() {
    this.get_data();
  }
}
</script>

<style scoped>
.box-card{
    border: 0 solid transparent;
    background-color: transparent;
}

/*头部整体设置*/
#radio_all {
  height: 15vh;
  position: relative;
}

/*侧边栏设置*/
#aside-box {
  width: 70px;
}

.el-card >>> .el-card__body{
    padding-left: 5px!important;
}

/*设置头部按钮框的大小和位置*/
#button-box {
    margin: 0;
    padding: 0;
    text-align: left;
    width: 80vw;
    position: absolute;
    top: 40px;
    left: 90px;
}

/*main的总体布局*/
.el-container >>> .el-main{
    padding: 0!important;
    /*padding: 20px 0!important;*/
}

#th-box {
    width: 100vw;
    overflow: hidden;
}

/*每一个信息框的设置*/
.box {
  background-color: white;
  margin-top: 10px;
  display: inline-block;
  width: 300px;
  height: 270px;
  border: 1px solid #EBEEF5;
  padding: 50px 0;
  text-align: center;
  transition: .3s;
  position: relative;
}

.box:hover {
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.3);
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
</style>
