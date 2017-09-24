// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import {store} from './store'
import {sync} from 'vuex-router-sync'
import Vuetify from 'vuetify'
import('../node_modules/vuetify/dist/vuetify.min.css')

Vue.use(Vuetify)
Vue.config.productionTip = false
sync(store, router)

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (!store.getters.user && !store.getters.isLoggedIn) {
      next({path: '/login'})
    } else {
      next()
    }
  } else if (to.matched.some(record => record.meta.requiresAnon)) {
    if (store.getters.user || store.getters.isLoggedIn) {
      next({path: '/'})
    } else {
      next()
    }
  } else {
    next()
  }
})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store: store,
  template: '<App/>',
  components: { App }
})
