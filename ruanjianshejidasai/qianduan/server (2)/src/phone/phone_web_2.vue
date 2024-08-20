<template>
    <div id="box">
        <div id="bread-box">
            <el-breadcrumb separator="/">
                <el-breadcrumb-item :to="{ path: '/phone_home' }">首页</el-breadcrumb-item>
                <el-breadcrumb-item>内容详情</el-breadcrumb-item>
            </el-breadcrumb>
        </div>
        <h1>山东：艺术类本科批、春季高考本科批第2次志愿填报注意事项</h1>
        <span id="txt-from">稿件来源：中国教育在线</span>
        <el-divider></el-divider>
        <div id="txt-body">
            <p>
                一、考生填报本次高校志愿前，须认真查看我院网站公布的艺术类本科批第2次志愿、春季高考本科批第2次志愿缺额计划和拟填报高校的招生章程（简章），了解高校有关报考要求及录取原则。尤其是艺术类有关高校及专业报考条件及录取原则有所不同，部分高校及专业有单科成绩限制，填报前更要阅读相关高校招生章程（简章），结合自身条件确定是否报考。
            </p>
            <br>
            <p>
                二、达到或超过相应类型录取控制分数线且尚未被录取的合格考生可根据自身情况决定是否填报本次志愿。
            </p>
            <br>
            <p>
                三、填报志愿时间为7月22日9:00-18:00。填报志愿结束后，不再受理考生补报志愿申请，也不允许考生修改、放弃已填报的志愿，考生被录取后，不能改录、换录。请考生慎重填报志愿。
            </p>
            <br>
            <p>
                四、艺术类专业投档时关联专业合格成绩，只有专业合格的考生才有资格填报。
            </p>
            <br>
            <p>
                承认其他校考成绩的专业，考生所取得的合格证专业名称须与所报考的专业名称完全一致。含招考方向的专业，是否要求招考方向也完全一致，由高校在招生章程（简章）中做出详细说明。
            </p>
            <br>
            <p>
                五、填报春季高考志愿时，考生填报的专业类别须与考试时的专业类别一致。
            </p>
            <br>
            <p>
                六、考生填报艺术类本科批第2次志愿时，只能在统考、联考、校考选择一类，不能同时填报。
            </p>
            <br>
            <p>
                七、艺术类本科批第2次志愿、春季高考本科批第2次志愿录取结果查询时间为7月25日12:00后，我院将以短信方式向已录取考生推送录取结果，请考生登录山东省2021年普通高考录取查询平台（http://cx.sdzk.cn/）、"爱山东"APP、国家政务服务平台、"山东省教育招生考试院"百度小程序查询本人录取结果。已被录取的考生将不再参与后续志愿填报、录取。
            </p>
            <br>
            <p class="end">
                山东省教育招生考试院
            </p>
            <p class="end">
                2021年7月21日
            </p>
        </div>
        <el-divider></el-divider>
    </div>
</template>

<script>
export default {
    name: "phone_web_2"
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