<template>
    <div>
        <el-card>
            <span id="title">您的每次份反馈都是我们前进的动力！</span>
            <br>
            <div>
                <el-input
                    type="textarea"
                    :rows="8"
                    placeholder="请输入内容"
                    v-model="text"
                    maxlength="300"
                    style="width: 80vw"
                    class="form"
                    show-word-limit
                >
                </el-input>
                <el-button type="success" plain @click="get_data()" id="button">提交反馈</el-button>
            </div>
        </el-card>
        <el-card id="end-card">
            <h2>刚刚反馈的信息</h2>
            <span>{{this.text2}}</span>
        </el-card>

    </div>
</template>

<script>
export default {
    name: "phone_opinion",
    data() {
        return {
            text: '',
            username: "",
            text2:"您暂未反馈消息",
        }
    },
    methods: {
        get_data() {
            this.username = this.$cookies.get('user_name');
            if (this.text == '') {
                this.$message.warning("意见反馈不能为空！")
            } else {
                this.axios.get("http://101.34.248.53:8181/Map/Comments/" + this.text + '/' + this.username).then(resp => {
                    console.log(resp.data)
                    this.$message.success("反馈成功!");
                    this.text2 = this.text;
                    this.text = ""
                })
            }
        },

    },
    created() {
        this.get1();
    }
}
</script>

<style scoped>
#title{
    display: block;
    width: 90vw;
    height: 50px;
    text-align: center;
    line-height: 50px;
}

.el-card{
    width: 100vw;
    height: 60vh;
    margin: 0;
    padding: 0;
    background-color: transparent;
    border: 0;
    box-shadow: 0 0 0 0 transparent;
}

#button{
    margin-top: 15px;
}

#end-card{
    height: 40vh;
    background-color: transparent;
    border: 0;
    box-shadow: 0 0 0 0 transparent;
}
</style>