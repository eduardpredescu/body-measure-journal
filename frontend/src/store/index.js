import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import decode from 'jwt-decode'

Vue.use(Vuex)

export const store = new Vuex.Store({
  state: {
    user: null,
    measurements: null,
    users: null,
    isLoggedIn: !!localStorage.getItem('token')
  },
  mutations: {
    ADD_MEASUREMENT (state, measurement) {
      state.measurements.push(measurement)
    },
    EDIT_MEASUREMENT (state, measurement) {
      const index = state.measurements.findIndex(object => object.date === measurement.date)
      state.measurements[index] = measurement
    },
    DELETE_MEASUREMENT (state, measurement) {
      const index = state.measurements.findIndex(object => object.date === measurement.date)
      state.measurements.splice(index, 1)
    },
    SET_USER (state, token) {
      state.user = decode(token)
    },
    LOGIN (state) {
      state.pending = true
    },
    LOGIN_SUCCESS (state) {
      state.isLoggedIn = true
      state.pending = false
    },
    LOGOUT (state) {
      state.isLoggedIn = false
    },
    ADD_USER (state, user) {
      state.users.push(user)
    },
    EDIT_USER (state, user) {
      const index = state.users.findIndex(object => object.username === user.username)
      state.users[index] = user
    },
    DELETE_USER (state, user) {
      const index = state.users.findIndex(object => object.username === user.username)
      state.users.splice(index, 1)
    }
  },
  actions: {
    Login ({commit}, user) {
      commit('LOGIN')
      // TODO add env vars
      axios.post('http://localhost:8000/api/login/', user)
          .then(response => {
            localStorage.setItem('token', response.data.token)
            commit('SET_USER', response.data.token)
            commit('LOGIN_SUCCESS')
          })
    },
    Logout ({commit}) {
      localStorage.removeItem('token')
      commit('LOGOUT')
    }
  },
  getters: {
    user: state => state.user,
    measurements: state => state.measurements,
    users: state => state.users,
    isLoggedIn: state => state.isLoggedIn
  }
})
