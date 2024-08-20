<template>
    <div>
      <el-card style="height: 500px;width: 1200px;margin: auto">
        <div id="box">
            <h3 id="tit">个人信息</h3>
            <el-descriptions
                direction="vertical"
                :column="3"
                border
                :labelStyle=des_style
                :contentStyle=des_style
            >

                <el-descriptions-item label="用户名">
                    <span>
                        {{ teacher.name }}
                    </span>
                </el-descriptions-item>

                <el-descriptions-item label="性别">
                    <span>
                        {{ teacher.sex }}
                    </span>
                </el-descriptions-item>

                <el-descriptions-item label="年龄">
                    <span>
                        {{ teacher.age }}
                    </span>
                </el-descriptions-item>

                <el-descriptions-item label="电话">
                    <span>
                        {{ teacher.tel }}
                    </span>
                </el-descriptions-item>

                <el-descriptions-item label="电子邮箱">
                    <span>
                        {{ teacher.email }}
                    </span>
                </el-descriptions-item>

                <el-descriptions-item label="专业">
                    <el-tag size="small">{{ teacher.major }}</el-tag>
                </el-descriptions-item>
            </el-descriptions>
            <el-button type="primary" id="button"  @click="showBox">修改信息</el-button>
        </div>
      </el-card>
        <div id="change-box" v-if="flag">
            <div id="mask">
                <div id="title">
                    信息修改
                </div>
                <div id="contant">
                    <span class="con-tit">用户名：</span><input type="text"  v-model="model_name">
                    <span class="con-tit">性别：</span><input type="text" v-model="model_sex">
                    <span class="con-tit">年龄：</span><input type="text" v-model="model_age">
                    <span class="con-tit">电话：</span><input type="text" v-model="model_tel">
                    <span class="con-tit">电子邮箱：</span><input type="text"  v-model="model_email">
                    <span class="con-tit">专业：</span><input type="text"  v-model="model_major">
                    <span class="con-tit">介绍：</span><el-input class="textarea" type="textarea" :rows="5" v-model="model_info"></el-input>
                </div>
                <div id="button-box">
                    <el-button type="primary" style="margin-right: 60px" @click="TrueBox">保存修改</el-button>
                    <el-button type="warning" @click="closeBox">取消修改</el-button>
                </div>
            </div>
        </div>

    </div>
</template>

<script>
export default {
    name: "teacher_inform",
    data(){
        return{
            //是否显示信息修改框
            flag: false,
            teacher:[],
            username:'',
            // 添加居中的css样式
            des_style:{
                'text-align':'center',
                'height':'70px',
            },
            model_name:null,
            model_sex:null,
            model_age:null,
            model_tel:null,
            model_email:null,
            model_major:null,
            model_info:null,
          teacher_name:''
        }
    },
    methods:{
      //显示老师个人信息
      get_message(){
        this.username = this.$cookies.get('user');
        this.axios.get("http://101.34.248.53:8181/Map/teacher/info/"+this.username).then(resp=>{
          this.teacher = resp.data
          console.log(resp.data)
          console.log(11111)
        })
      },
        showBox(){
            this.flag = true;
            this.model_name = this.teacher.name;
            this.model_sex = this.teacher.sex;
            this.model_tel = this.teacher.tel;
            this.model_age = this.teacher.age;
            this.model_email = this.teacher.email;
            this.model_major = this.teacher.major
            this.model_info = this.teacher.info

        },

        closeBox(){
            this.flag = false;
        },
       //修改信息
        TrueBox(){
          this.closeBox();
          this.teacher_name = this.$cookies.get('user');
          this.axios.get("http://101.34.248.53:8181/Map/teacher/relist/"+this.teacher_name+'/'+this.model_name+'/'+this.model_sex+'/'
              +this.model_age+'/'+this.model_tel+'/'+this.model_major+'/'+this.model_email+'/'+this.model_info).then(resp=>{
            this.teacher = resp.data
            this.get_message()
          })

        //    axios返回后台数值
        },

    },
  created() {
      this.get_message()
  }

}
</script>

<style scoped>
#box{
    width: 900px;
    height: 800px;
    margin: 0 auto;
}

#tit{
    text-align: center;
}

.el-tag--small{
    margin: 5px;
}

#button{
    margin-top: 20px;
     /*margin-left: 405px;*/
}

#change-box{
    display: block;
    width: 100%;
    height: 100%;
    background-color: rgba(0,0,0,0.4);
    position: fixed;
    top: 0;
    left: 0;
    z-index: 999;
}

#mask{
    width: 550px;
    height: 640px;

    background-color: white;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%,-50%);

    border-radius: 25px;
    box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
}

#title{
    height: 60px;
    font-size: 20px;
    font-weight: 700;
    text-align: center;
    line-height: 60px;
    margin-top: 15px;
}

#contant{
    /*border: 1px solid red;*/
}

#contant input{
    display: block;
    width: 230px;
    height: 40px;
    margin: 5px auto 15px 200px;
    border-radius: 5px;
    box-shadow: none;
    border: 1px solid red;
    outline: none;
    padding-left: 15px;
}

#contant input:hover{
    border: 1px solid blue;
}
.con-tit{
    font-size: 14px;
    font-weight: 700;
    position: absolute;
    margin-left: 100px;
    margin-top: 11px;
}
.textarea{
  border: 1px solid red;
  border-radius: 4px;
  width: 247px;
  height: 114px;
  margin: 5px auto 15px 200px;
}
.textarea:hover{
  border: 1px solid blue;
  border-radius: 4px;

}

#button-box{
    display: flex;
    justify-content: center;
    align-items: center;
}
</style>