<template>
    <div>
        <button
            :class="num"
            title="收藏"
            @click="changeCss(num)"></button>
        <div>次数的数据为：</div>
    </div>
</template>

<script>
export default {
    name: "favorite",
    data(){
        return{
            num:'favor_no',
        }
    },
    methods:{
        changeCss(val){
            if(val == 'favor_no'){
                this.num = 'favor_yes'
                // axios(sdglxy)
            }
            else{
                this.num = 'favor_no'

            }

        }
    }
}
</script>

<style scoped>
.favor_no{
    width: 50px;
    height: 50px;
    outline: 0;
    background-color: transparent;
    border: 0 solid transparent;
    background-image: url("../assets/favorite.png");
}
.favor_no:active{
    outline: 0;
    background-image: url("../assets/favorite.png");
    background-position: 50px 0;
}

.favor_yes{
    width: 50px;
    height: 50px;
    outline: 0;
    background-color: transparent;
    border: 0 solid transparent;
    background-image: url("../assets/favorite.png");
    background-position: 50px 0;
}
</style>