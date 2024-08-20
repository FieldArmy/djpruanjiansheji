<template>
    <div id="box">
        <div id="bread-box">
            <el-breadcrumb separator="/">
                <el-breadcrumb-item :to="{ path: '/phone_home' }">首页</el-breadcrumb-item>
                <el-breadcrumb-item>内容详情</el-breadcrumb-item>
            </el-breadcrumb>
        </div>
        <h1>山东：普通类和体育类常规批、艺术类专科批和春季高考专科批志愿填报注意事项</h1>
        <span id="txt-from">稿件来源：中国教育在线</span>
        <el-divider></el-divider>
        <div id="txt-body">
            <p class="big">
                一、普通类常规批第3次志愿
            </p>
            <p>
                （一）普通类二段线上考生（含未被录取的一段线上考生）均可参加第3次志愿填报，具体本、专科缺额计划详见山东省教育招生考试院网站。<br>
                （二）志愿均实行以“专业（专业类）+学校”为单位的平行志愿模式，1个“专业（专业类）+学校”为1个志愿。考生每次填报志愿的数量最多不超过96个（本科和专科志愿都包含在内）。<br>
                公费专科医学生包含在96个志愿之内，考生可在常规批第3次志愿填报时填报。<br>
                （三）非西藏生源定向西藏就业计划（山东大学）限572分（含）以上考生填报志愿。边防军人子女预科班限364分（含）以上考生填报志愿。<br>
                （四）部分高校部分专业对性别、面试、体检等有要求，请考生填报之前一定要仔细阅读高校招生章程（简章）。<br>
            </p>
            <br>
            <p class="big">
                二、艺术类专科批第2次志愿
            </p>
            <p>
                （一）须达到艺术类专科文化控制线（150分）方可填报，缺额计划详见山东省教育招生考试院网站。<br>
                （二）艺术类专科专业分类别实行平行志愿，按“专业（专业类）+学校”志愿模式填报，考生每次志愿填报数量不超过60个。考生取得合格证的专业类别须与志愿高校的专业类别一致。<br>
            </p>
            <br>
            <p class="big">
                三、体育类常规批第3次志愿
            </p>
            <p>
                体育类二段线上考生（含未被录取的一段线上考生）均可参加第3次志愿填报，具体缺额计划详见山东省教育招生考试院网站。<br>
            </p>
            <br>
            <p class="big">
                四、春季高考专科批第2次志愿
            </p>
            <p>
                （一）填报春季高考各专业类别的考生成绩不低于150（含）分，缺额计划详见山东省教育招生考试院网站。<br>
                （二）填报春季高考志愿时，考生填报的专业类别须与考试时的专业类别一致。<br>
            </p>
            <br>
            <p class="big">
                五、其他提示
            </p>
            <p>
                （一）部分专业对考生高考体检结论有要求，例如不录取色盲、色弱考生，请考生仔细查阅《普通高等学校招生体检工作指导意见》及高校招生章程（简章），合理填报。<br>
                （二）本次志愿填报时间为8月2日-3日（每天9:00—18:00），在填报志愿时限结束之后，不再受理考生补报志愿申请，也不允许考生修改、放弃已填报的志愿，请考生一定要及时上网填报志愿。建议考生尽量早于志愿填报结束前2小时提交，避免因意外造成志愿填报无法完成。
                普通类、体育类常规批第3次志愿、艺术类专科批第2次志愿，三者不能兼报。<br>
                （三）8月7日至8日（每天9：00-18：00）夏季高考和春季高考双录取学生选择确认。<br>
                （四）本次录取结果查询时间为8月6日12:00后，我院将以短信方式向已录取考生推送录取结果，考生也可以登录山东省2021年普通高考录取查询平台（http://cx.sdzk.cn/）、“爱山东”APP、国家政务服务平台、“山东省教育招生考试院”百度小程序查询本人录取结果。<br>
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
    name: "phone_web_4"
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