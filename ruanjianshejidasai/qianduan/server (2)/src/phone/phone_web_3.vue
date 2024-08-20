<template>
    <div id="box">
        <div id="bread-box">
            <el-breadcrumb separator="/">
                <el-breadcrumb-item :to="{ path: '/phone_home' }">首页</el-breadcrumb-item>
                <el-breadcrumb-item>内容详情</el-breadcrumb-item>
            </el-breadcrumb>
        </div>
        <h1>山东：2021年普通高校招生录取结果查询时间</h1>
        <span id="txt-from">稿件来源：中国教育在线</span>
        <el-divider></el-divider>
        <div id="txt-body">
            <img src="./assets/inter-time.png">
        </div>
        <el-divider></el-divider>
    </div>
</template>

<script>
export default {
    name: "phone_web_3"
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

img{
    width: 95vw;
    height: 95vh;
}
</style>