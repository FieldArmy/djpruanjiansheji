
<template>
  <div class="bgc">
    <el-input style="width: 30%; margin-left: 25%"
              placeholder="请输入内容"
              v-model="input"
              clearable
    >
    </el-input>
    <el-button type="primary" style="margin-left: 5px" @click="search">搜索</el-button> <br>
      <p style="width: 50%;padding: 30px;margin-left: 200px;display: inline-block" v-show="flag">{{answer}}</p>
    <img src="../assets/robot1.png"/>
  </div>
</template>

<script>
import  axios from 'axios'
export default {
  name: "AI",
  data(){
    return{
      input:'',
      username:'',
      answer:'',
     flag:false
    }

  },
  methods: {
    search() {
      this.flag=false;
        axios({
          method:"POST",
          url:'api/myai',
          data:{
            account:this.username,
            action:'ai_action',
            question:this.input
          }
        }).then((resp)=>{
          this.answer=resp.data.result.result
          this.flag=true;
        })

    },

  },
  mounted(){
    this.username=this.$cookies.get('user_name');
  }




}
</script>

<style scoped>
img{
  position: absolute;
  width: 500px;
  right: -7%;
  bottom: -11%;
}

p{
  text-indent: 2em;
}
</style>