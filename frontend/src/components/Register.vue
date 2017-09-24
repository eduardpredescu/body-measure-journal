<template>
  <v-layout row wrap align-center>
    <v-flex xs8 md8 offset-xs2 class="text-xs-center">
      <v-card>
        <v-card-text>
          <v-form v-model="valid">
            <v-text-field
            label="Username"
            v-model="username"
            :rules="usernameRules"
            required
            ></v-text-field>
            <v-text-field
            label="E-mail"
            v-model="email"
            :rules="emailRules"
            required
            ></v-text-field>
            <v-text-field
            label="Enter your password"
            v-model="password"
            :rules="passwordRules"
            :append-icon-cb= "() => (e1 = !e1)"
            :append-icon="e1 ? 'visibility_off' : 'visibility'"
            :type="e1 ? 'password' : 'text'"
            required
            counter></v-text-field>
            <v-text-field
            label="Enter your password again"
            v-model="confirmPassword"
            :rules="confirmPasswordRules"
            :append-icon-cb= "() => (e1 = !e1)"
            :append-icon="e1 ? 'visibility_off' : 'visibility'"
            :type="e1 ? 'password' : 'text'"
            required
            counter></v-text-field>
            <v-btn primary @click="Register" :disabled="!valid" >Register</v-btn>
          </v-form>
        </v-card-text>
        <router-link :to="{path: '/login'}">Already have an account? Login here!</router-link>
      </v-card>
    </v-flex>
  </v-layout>
</template>

<script>
import Vuex from 'vuex'
export default {
  name: 'RegisterForm',
  data () {
    return {
      valid: false,
      e1: false,
      username: '',
      usernameRules: [
        (v) => !!v || 'Username is required'
      ],
      email: '',
      emailRules: [
        (v) => !!v || 'E-mail is required',
        (v) => /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(v) || 'E-mail must be valid'
      ],
      password: '',
      passwordRules: [
        (v) => !!v || 'Password is required'
      ],
      confirmPassword: '',
      confirmPasswordRules: [
        (v) => !!v || 'Password is required',
        (v) => v === this.password || 'Passwords must match!'
      ]
    }
  },
  computed: {
    ...Vuex.mapGetters(['error'])
  },
  methods: {
    Register () {
      this.$store.dispatch('Register', {'username': this.username, 'email': this.email, 'password': this.password, 'confirm_password': this.confirmPassword}).then(() => {
        this.$router.push('/')
      })
    }
  }
}
</script>