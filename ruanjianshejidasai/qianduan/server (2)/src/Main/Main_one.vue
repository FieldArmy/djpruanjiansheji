<template>
    <div class="body">
        <el-backtop>
            <div
                style="{
        height: 100%;
        width: 100%;
        background-color: #f2f5f6;
        box-shadow: 0 0 6px rgba(0,0,0, .12);
        text-align: center;
        line-height: 40px;
        color: #1989fa;
      }"
            >
                UP
            </div>
        </el-backtop>
        <el-container style="height: 100vh">
            <el-header height="70px">
                <div>
                    <img src="../assets/pic.png" class="first">
                    <h3 class="hh3">志高考</h3>
                    <el-button type="text" class="hello2">Hi,{{ user }}</el-button>

                    <el-dropdown id="question">
                    <span class="el-dropdown-link">
                      <el-avatar class="img"
                                 src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png"></el-avatar>
                    </span>
                        <el-dropdown-menu slot="dropdown" style="width: 80px" align="center">
                            <el-button type="text" @click="jump2()" style="margin-left: 0">退出登录</el-button>

                        </el-dropdown-menu>
                    </el-dropdown>
                </div>
            </el-header>

            <el-container>
                <el-aside width="220px" align="left">
                    <el-menu
                        default-active="2"
                        class="el-menu-vertical-demo"
                        background-color="#545c64"
                        text-color="#fff"
                        active-text-color="#ffd04b"
                        router
                    >

                        <el-menu-item index="/index">
                            <i class="el-icon-setting"></i>
                            <span slot="title" class="cebian">首页</span>
                        </el-menu-item>

                      <el-menu-item index="Fill">
                        <i class="el-icon-s-platform"></i>
                        <span slot="title" class="cebian">模拟报志愿</span>
                      </el-menu-item>

                      <el-menu-item index="AI">
                        <i class="el-icon-cpu"></i>
                        <span slot="title" class="cebian">AI助手</span>
                      </el-menu-item>



                        <el-menu-item index="/checkschool">
                            <i class="el-icon-s-help"></i>
                            <span slot="title" class="cebian">查学校</span>
                        </el-menu-item>

                        <el-menu-item index="/checkmajor">
                            <i class="el-icon-menu"></i>
                            <span slot="title" class="cebian">查专业</span>
                        </el-menu-item>




                        <el-menu-item index="Collection">
                            <i class="el-icon-star-off"></i>
                            <span slot="title" class="cebian">我的收藏</span>
                        </el-menu-item>


                        <el-menu-item index="teacher">
                            <i class="el-icon-s-custom"></i>
                            <span slot="title" class="cebian">咨询老师</span>
                        </el-menu-item>

                        <el-menu-item index="opinion">
                            <i class="el-icon-question"></i>
                            <span slot="title" class="cebian">意见反馈</span>
                        </el-menu-item>
                    </el-menu>
                </el-aside>

                <el-main>
                    <router-view></router-view>
                </el-main>

            </el-container>
        </el-container>
    </div>
</template>

<script>
export default {
    name: "main_one",

    data() {
        return {
            isCollapsed: true,
          user: "",
          hello:[
              '请您首先在模拟填报志愿模块填写您的考生信息',
            '(此消息30s后消失)'],
          newDatas:[],
        }
    },
    methods: {
      open_notify() {
        const h = this.$createElement;
        for (let i in this.hello) {
          this.newDatas.push(h('p', null, this.hello[i]));
        }

        this.$notify({
          title: '尊敬的各位老师',
          message: h('div', null, this.newDatas),
          duration: 30000,
        });
      },
        getForm() {
            this.dialogVisible = true;
        },
        jump2() {
            window.sessionStorage.clear();//清楚session
            this.$router.push('/')
            this.$message.success("退出成功！")
        },
    },
    created() {
        this.user = this.$cookies.get('user_name');
      this.open_notify();
    }
}
</script>

<style scoped>
.body {
    margin: auto;
}



.el-menu {
    border: 0px solid transparent;
}

#soall {
    width: 100px;
    height: 100px;
}

.el-header {
    font-size: 30px;
    justify-content: space-between;
}

.el-header img {
    margin-top: 4px;
    margin-left: -20px;
    height: 70px;
  border-radius: 50px;
}

.el-menu-item {
    height: 85px;
    line-height: 85px;
}

.el-header {
  position: relative;
    height: 50px;
}

.el-aside {
    background-color: #545c64;
}

.el-main {
    /*width: 100vh;*/
    background-color: #defcfc;
}

.img {
    width: 50px;
    height: 50px;
}

#question {
    position: absolute;
    top: 19px;
    right: 45px;
}

.size_hello {
    color: black;
}

.hello1 {
    font-family: "Lithos Pro Regular";
    color: dodgerblue;
    font-size: 19px;
    position: absolute;
    top: 37px;
    right: 174px;
}

.hello2 {
    font-size: 18px;
    position: absolute;
    top: 35px;
    right: 110px;
}



.hh3 {
    font: bolder 30px "Adobe 黑体 Std R";
    margin-left: 80px;
    margin-top: -72px;
    line-height: 1.5em;
    font-family: "Times New Roman", Times, serif;
    font-size: 40px;
    color: gray;
  text-shadow:-6px -3px 2px darkgray;
}

.cebian {
    font-size: 16px;
}

.cebian:hover {
    font-size: 16px;
    color: #ffd04b;
}
</style>
