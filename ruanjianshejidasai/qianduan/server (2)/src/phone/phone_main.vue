<template>
    <div id="phone_app">
        <el-header id="header-box">
            <el-button @click="drawer = true">
                <img src="./assets/aside.png">
            </el-button>
            <div id="logo-box">
                <img src="./assets/logo_3.png" id="logo">
                <span id="tit">山东优志愿系统</span>
            </div>
        </el-header>
<!--        弹出框         -->
        <el-drawer
            title="菜单栏"
            :visible.sync="drawer"
            :direction="direction"
            size="250px"
            :show-close="showCloseButton"
            >
            <div>
                <el-menu
                    default-active="/"
                    class="el-menu-vertical-demo"
                    router
                >
                    <el-menu-item index="/phone_home" >
                        <i class="el-icon-setting"></i>
                        <span slot="title">首页</span>
                    </el-menu-item>

                    <el-menu-item index="/phone_school">
                        <i class="el-icon-s-help"></i>
                        <span slot="title">查学校</span>
                    </el-menu-item>

                    <el-menu-item index="/phone_major">
                        <i class="el-icon-menu"></i>
                        <span slot="title">查专业</span>
                    </el-menu-item>

                    <el-menu-item index="/phone_zhiyuan">
                        <i class="el-icon-s-platform"></i>
                        <span slot="title">智能填报</span>
                    </el-menu-item>

                    <el-menu-item index="/phone_spring">
                        <i class="el-icon-s-promotion"></i>
                        <span slot="title">智能填报(春)</span>
                    </el-menu-item>

                    <el-menu-item index="/phone_teacher">
                        <i class="el-icon-s-custom"></i>
                        <span slot="title">咨询老师</span>
                    </el-menu-item>

                    <el-menu-item index="/phone_opinion">
                        <i class="el-icon-question"></i>
                        <span slot="title">意见反馈</span>
                    </el-menu-item>
                </el-menu>
            </div>
        </el-drawer>
        <el-main id="main-box">
            <router-view></router-view>
        </el-main>
    </div>
</template>

<script>
export default {
    name: "phone_main",
    data(){
        return{
            direction:'ltr',
            drawer:false,
            showCloseButton:false,
        }
    }
}
</script>

<style scoped>
/*添加元素整体居中，这里的居中只负责移动端*/
#phone_app{
    text-align: center!important;
}
/*element ui样式设计*/
/*设置按钮框样式*/
.el-button{
    background-color: transparent!important;
    border: 0 solid transparent!important;
    position: absolute;
    left: 0;
}
.el-button:hover{
    background-color: transparent;
    border: 0 solid transparent!important;
}
.el-button:focus{
    background-color: transparent;
    border: 0 solid transparent!important;
}

/*设置按钮样式*/
.el-button >>> img{
    width: 25px;
    height: 25px;
}

/*需要主体添加*/
/*.el-drawer__header >>> span{*/
/*    text-align: center!important;*/
/*}*/

.el-drawer__body ul{
    margin: 0;
    padding: 0;
}

/*设置每一个选项的大小*/
.el-drawer__body li{
    line-height: 100px!important;
    height: 100px!important;
}

.el-menu{
    border: 0 solid transparent!important;
}

.el-menu-item{
    padding: 0 20px 0 0!important;
}

/*具体细节样式设计*/
#header-box{
    display: flex;
    justify-content: center;
    align-items: center;

    height: 100px!important;
    margin: 0!important;
    padding: 0!important;
    /*border: 1px solid blue;*/
    /*background-color: pink;*/
}

#main-box{
    margin: 0;
    padding: 0;
    /*border: 1px solid red;*/
}

#logo-box{
    display: block;
    width: 100%;
    height: 100%;
    text-align: center;
    vertical-align: middle;
    /*border: 1px solid green;*/
}

#logo{
    width: 120px;
    height: 100px;
    vertical-align: middle;
}

#tit{
    font-size: 24px;
    font-weight: 700;
    vertical-align: middle;
}
</style>