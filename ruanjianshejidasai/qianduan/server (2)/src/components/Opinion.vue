<template>
  <div>
    <el-card>
      <span class="span">您的每次份反馈都是我们前进的动力！</span>
      <br>
      <div>
        <el-input
            type="textarea"
            :rows="8"
            placeholder="请输入内容"
            v-model="text"
            maxlength="300"
            style="width: 340px"
            class="form"
            show-word-limit
        >
        </el-input>
        <el-button id="weizhi1" type="success" plain @click="get_data()">提交反馈</el-button>
      </div>

      <div
          style='width:2px;border:0.2px solid #D8DADC;float:left;height:2500px;margin-left: 500px;margin-top: -800px'></div>
      <div
          style='width:2px;border:0.2px solid #D8DADC;float:left;height:2500px;margin-left: 445px;margin-top: -800px'></div>

<!--      <ul type="1" id="weizhi2">-->
<!--        <span style="margin-left: -16px">常见反馈</span>-->
<!--        <li class="li_top">考虑下页面切换时数据的更替</li>-->
<!--        <li class="li_top">不错的系统，数据和显示层都挺好</li>-->
<!--        <li class="li_top">模拟报志愿模块美工方面，希望做的更好</li>-->
<!--        <li class="li_top">继续加油，希望看到更棒的系统！</li>-->
<!--        <li class="li_top">咨询老师页面可以更加完善一点</li>-->
<!--        <li class="li_top">很好，继续加油！</li>-->
<!--        <li class="li_top">你们的系统太好了！！！</li>-->
<!--      </ul>-->
      <ul type="1" id="weizhi2">
        <span style="margin-left: -16px">说明</span>
        <li class="li_top">感谢您提出的宝贵意见</li>
        <li class="li_top">系统将会通过后台查看您反馈的信息</li>
        <li class="li_top">您的每次份反馈都是我们前进的动力！</li>
        <li class="li_top">也欢迎您通过邮箱反馈</li>
        <li class="li_top">我们的邮箱:1574259441@qq.com</li>
      </ul>
    </el-card>
    <el-card v-if="cardzdm == true" style="height: 200px;margin-top: 30px">
      <h2 class="span3">刚刚反馈的信息</h2>
      <!--      <el-input v-model="text2" style="width: 100%;margin-top: 10px" class="span2" disabled></el-input>-->
      <span>{{ this.text2 }}</span>
    </el-card>

  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Opinion",
  data() {
    return {
      text: '',
      username: "",
      cardzdm: false,
      text2: "",
    }
  },
  methods: {
    get_data() {
      this.username = this.$cookies.get('user_name');
      // console.log(this.username);
      if (this.text == '') {
        this.$message.warning("意见反馈不能为空！")
      } else {
        axios({
          method:'POST',
          url:'api/students/giveissue',
          data:{
            action:'give_issue',
            // account:'12345678',
            account:this.$cookies.get('user_name'),
            // account:this.username,
            issue:this.text
          }
        }).then((resp)=>{
          console.log(resp.data)
          this.cardzdm = true;
          this.text2 = this.text;
          this.text = ""
        }).catch((err)=>{
          console.log(err)
          console.log(this.text)
        })

      }
    },

  },
}
</script>

<style scoped>
.span {
  font-size: 22px;
  color: #0077ff;
  font-family: Monospace;
  font-weight: bold;
}

.span3 {
  font-size: 22px;
  color: #000000;
  font-family: Monospace;
  font-weight: bold;
}

.span2 {
  font-size: 18px;
}

.form {
  width: 400px;
  margin-top: 20px;
}

.el-card {
  width: 1400px;
  height: 550px;
  margin-top: 20px;
  margin-left: 10px;
}

#question {
  position: absolute;
  top: 100px;
  right: 400px;
}

#weizhi1 {
  position: absolute;
  top: 320px;
  left: 640px;
}

#weizhi2 {
  position: absolute;
  top: 170px;
  left: 820px;
}

#weizhi3 {
  position: absolute;
  top: 170px;
  left: 1255px;
}

.li_top {
  margin-top: 8px;
}

</style>
