import Vue from 'vue'
import Router from 'vue-router'
import Dashboard from '@/components/Dashboard'
import AuthForm from '@/components/AuthForm'
import RegisterForm from '@/components/Register'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/login',
      name: 'Login',
      component: AuthForm,
      meta: {requiresAnon: true}
    },
    {
      path: '/register',
      name: 'Register',
      component: RegisterForm,
      meta: {requiresAnon: true}
    },
    {
      path: '/',
      name: 'Dashboard',
      component: Dashboard,
      meta: {requiresAuth: true}
    }
  ]
})
