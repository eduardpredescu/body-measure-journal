<template>
  <v-layout row wrap align-center>
    <v-flex xs8 md8 offset-xs2 class="text-xs-center">
      <v-card>
        <v-card-text>
          <v-form v-model="valid">
            <v-alert v-if="error.non_field_errors" error value="true">
              {{ error.non_field_errors[0] }}
            </v-alert>
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
            <v-btn primary @click="Login" :disabled="!valid" >Login</v-btn>
          </v-form>
        </v-card-text>
        <router-link :to="{path: '/register'}">Don't have an account? Create an account here!</router-link>
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
      email: '',
      emailRules: [
        (v) => !!v || 'E-mail is required',
        (v) => /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(v) || 'E-mail must be valid'
      ],
      password: '',
      passwordRules: [
        (v) => !!v || 'Password is required'
      ]
    }
  },
  computed: {
    ...Vuex.mapGetters(['error'])
  },
  methods: {
    Login () {
      this.$store.dispatch('Login', {'email': this.email, 'password': this.password}).then(() => {
        this.$router.push('/')
      })
    }
  }
}
</script>