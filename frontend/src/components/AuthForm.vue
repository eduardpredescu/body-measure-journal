<template>
  <form novalidate>
  Login<input v-model="username" type="text">
  Password<input v-model="password" type="text">
  <button @click="Login">Login</button>
  </form>
</template>

<script>
import Vuex from 'vuex'
export default {
  name: 'AuthForm',
  data () {
    return {
      username: '',
      password: ''
    }
  },
  computed: {
    ...Vuex.mapGetters(['user'])
  },
  methods: {
    Login () {
      this.$store.dispatch('Login', {'email': this.username, 'password': this.password})
    }
  }
}
</script>