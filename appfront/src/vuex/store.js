import Vue from 'vue'
//全局引入vueX
import Vuex from 'vuex'


//全局注册vueX
Vue.use(Vuex)

const state = { //状态
  name: '张三'
}
const mutations = { //更改store中状态的唯一方法
  change1(state) { //不带参数更改
    state.name = "李四"
  },
  change2(state, payload) { //带参数更改
    state.name = payload.name
  },
}
const actions = { //异步更改状态
  change1a(context) {
    let _name = context.state.name //获取state原name
    console.log('_name', _name)
    setTimeout(() => {
      context.commit('change1')
    }, 1000);
  },
  change2a(context, payload) {

    setTimeout(() => {
      context.commit("change2", payload)
    }, 1000);

  }
}

//store中state的派生状态,也可以理解为一种计算属性，因为它像计算属性一样，返回值会根据它的依赖被缓存起来，且依赖对象发生改变的时候它才会被重新计算。
const getters = {
  change1b: state => {
    let add = ""
    if (state.name === "张三") {
      add = "是初始的值"
    }
    return state.name + add
  },
  change2b: (state) =>(val) =>{
    let add = ""
    if (state.name === "张三") {
      add = val
    }
    return state.name + add
  }

}
export default new Vuex.Store({
  state,
  mutations,
  actions,
  getters
})
