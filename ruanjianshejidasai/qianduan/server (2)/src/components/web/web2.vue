<template>
    <div id="box">
        <div style="margin-top: 10px">
            <el-breadcrumb separator="/">
                <el-breadcrumb-item :to="{ path: '/index' }">首页</el-breadcrumb-item>
                <el-breadcrumb-item>内容详情</el-breadcrumb-item>
            </el-breadcrumb>
        </div>
        <div class="box">
            <h1>山东：2023年体育类常规批（本科）第2次志愿院校专业计划</h1>
            <span id="txt-from">稿件来源：中国教育在线</span>
            <el-divider></el-divider>
            <div id="txt-body">
              <a href="https://www.sdzk.cn/Floadup/file/20230719/6382538152670673255865061.xls">山东省2023年体育类常规批（本科）第2次志愿院校专业计划</a>
            </div>
            <el-divider></el-divider>
        </div>
    </div>
</template>

<script>
export default {
    name: "Web-1"
}
</script>

<style scoped>
#box {
    width: 1200px;
    margin: 0 auto;
    padding: 10px;
}

.box {
    box-sizing: border-box;
    padding: 0 10px;
    background-color: white;
    border-radius: 10px;
}

#txt-from {
    font-size: 14px;
}

h1 {
    font-weight: 400;
    text-align: center;
}

#txt-body {
    width: 1000px;
    margin: auto;
    padding: 0;
    /*border: 1px solid red;*/
}

p {
    margin: 0;
    padding: 0;
    font-size: 16px;
    text-indent: 2em;
    line-height: 2;
}

.end {
    text-align: right;
}
</style>
