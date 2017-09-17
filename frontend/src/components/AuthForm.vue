<template>
  <form novalidate>
  Login<input v-model="username" type="text">
  Password<input v-model="password" type="text">
  <button @click="Login">Login</button>
  </form>
</template>

<script>
import axios from 'axios'
export default {
  name: 'AuthForm',
  data () {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    Login () {
      axios.post('http://localhost:8000/api/login/', {
        'email': this.username,
        'password': this.password
      })
      .then(response => {
        console.log(response.data)
        localStorage.setItem('JWTToken', response.data.token)
      })
      .catch(e => console.log(e.data))
    }
  }
}
</script>