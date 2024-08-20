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
            <p>
                8月7日上午，山东省教育厅举行2021年普通高校招生工作第三次新闻发布会，通报招生录取基本情况。
            </p>
            <br>
            <p>
                2021年，我省报名参加高考考生共79.5万人，其中春季高考报名16.5万人，夏季高考报名63万人。
            </p>
            <br>
            <p class="big">
                2021年在我省招生的普通高校共1791 所，共录取考生688509人，其中，本科录取294373人（包括春季高考 17000人，夏季高考271406 人，提前保送、单招等 5967人；专科录取394136人（包括春季高考 28442人，夏季高考 222028人，各类单招和专科综合评价招生143666人）。
            </p>
            <br>
            <p class="big">
                集中录取阶段，夏季高考本科录取271406人，其中，普通类225954人，艺术类40921人，体育类4531人;专科录取222028人，其中，普通类206896人，艺术类13867人，体育类1265人。
            </p>
        </div>
        <el-divider></el-divider>
    </div>
</template>

<script>
export default {
    name: "Web-1"
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

p{
    margin: 0;
    padding: 0;
    font-size: 16px;
    text-indent: 2em;
    line-height: 2;
}

.big{
    color: cadetblue;
    font-weight: 700;
}
</style>