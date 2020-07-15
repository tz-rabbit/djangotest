import Vue from 'vue'
import Router from 'vue-router'
import login from '@/views/login'
import home from '@/views/home'
import home2 from '@/views/home2'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/login',
      name: 'login',
      component: login
    },

    {
      path: '/',
      redirect: '/home',
      component: home,

    },
    {
      path: '/home',
      name: 'home',
      component: home,
      
    },
    {
      path: '/home2',
      name: 'home2',
      component: home2
    }
  ]
})
