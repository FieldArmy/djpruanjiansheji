<template>
    <div id="box">
        <div id="bread-box">
            <el-breadcrumb separator="/">
                <el-breadcrumb-item :to="{ path: '/phone_home' }">首页</el-breadcrumb-item>
                <el-breadcrumb-item>内容详情</el-breadcrumb-item>
            </el-breadcrumb>
        </div>
        <h1>山东：2021高考录取情况公告</h1>
        <span id="txt-from">稿件来源：中国教育在线</span>
        <el-divider></el-divider>
        <div id="txt-body">
            <span>
                <a href="http://www.sdzk.cn/Floadup/file/20210720/6376239645845237111590931.xls">山东2021年普通类常规批第1次志愿投档情况表(点击下载投档情况表)</a>
            </span>
        </div>
        <el-divider></el-divider>
    </div>
</template>

<script>
export default {
    name: "phone_web_6"
}
</script>

<style scoped>
#box{
    width: 100vw;
}

#bread-box{
    padding-top: 10px;
    padding-left: 5px;
}

h1{
    font-size: 20px;
    font-weight: 700;
    text-align: center;
}

#txt-from{
    font-size: 14px;
}

#txt-body{
    width: 100vw;
    margin: 0;
    padding: 0;
    /*border: 1px solid red;*/
}
</style>