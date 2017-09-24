<template>
  <div id="app">
    <v-app>
      <main>
        <v-container fill-height>
          <router-view></router-view>
        </v-container>
      </main>
   </v-app>
  </div>
</template>

<script>
export default {
  name: 'app'
}
</script>

<style>
</style>
