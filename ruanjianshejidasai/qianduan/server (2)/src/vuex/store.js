import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const store = new Vue.Store({
    state:{
        count:1
    },
    mutations:{
        increment(state){
            state.count++
        }
    }
})
export default store
