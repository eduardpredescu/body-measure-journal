<template>
  <v-layout align-center>
    <v-flex xs8 md8 offset-xs2>
      <v-card>
        <v-card-text>
          <v-form v-model="valid">
            <v-text-field
            label="E-mail"
            v-model="username"
            :rules="emailRules"
            required
            ></v-text-field>
            <v-text-field
            label="Enter your password"
            v-model="password"
            :append-icon-cb= "() => (e1 = !e1)"
            :append-icon="e1 ? 'visibility_off' : 'visibility'"
            :type="e1 ? 'password' : 'text'"
            counter></v-text-field>
            <v-btn @click="Login" :class="{ green: valid, red: !valid }">Login</v-btn>
          </v-form>
        </v-card-text>
      </v-card>
    </v-flex>
  </v-layout>
</template>

<script>
import Vuex from 'vuex'
export default {
  name: 'AuthForm',
  data () {
    return {
      valid: false,
      e1: false,
      username: '',
      emailRules: [
        (v) => !!v || 'E-mail is required',
        (v) => /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(v) || 'E-mail must be valid'
      ],
      password: ''
    }
  },
  computed: {
    ...Vuex.mapGetters(['user'])
  },
  methods: {
    Login () {
      this.$store.dispatch('Login', {'email': this.username, 'password': this.password})
      this.$router.push('/')
    }
  }
}
</script>