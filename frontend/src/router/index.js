import Vue from 'vue'
import Router from 'vue-router'
import Hello from '@/components/Hello'
import AuthForm from '@/components/AuthForm'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/login',
      name: 'Login',
      component: AuthForm
    },
    {
      path: '/',
      name: 'Hello',
      component: Hello
    }
  ]
})
