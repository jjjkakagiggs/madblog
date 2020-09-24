<template>
  <div id="app">
    <img src="./assets/logo.png">
    <!-- 路由占位符 -->
    <navbar></navbar>
    <router-view></router-view>
  </div>
</template>

<script>
import Navbar from './components/Navbar'
export default {
  name: 'App',
  components: {
      navbar:Navbar
  }
}
</script>

<style>
</style>
