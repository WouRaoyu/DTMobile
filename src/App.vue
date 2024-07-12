<template>
  <div id="app">
    <van-nav-bar title="数字孪生终端" left-text="返回" left-arrow>
      <template #right>
        <van-icon name="search" size="18" />
      </template>
    </van-nav-bar>
    <router-view />
    <van-tabbar :style="{'z-index':999}" v-model="active">
      <van-tabbar-item replace to="/home" icon="home-o">首页</van-tabbar-item>
      <van-tabbar-item icon="scan">扫描</van-tabbar-item>
      <van-tabbar-item icon="bullhorn-o" badge="20">通知</van-tabbar-item>
      <van-tabbar-item icon="setting-o" dot>设置</van-tabbar-item>
    </van-tabbar>
  </div>
</template>

<script>
import { ref } from 'vue';
import { Tabbar, TabbarItem, NavBar } from 'vant';

export default {
  setup() {
    const active = ref('home');
    return { active };
  },
  data() { return {}; },
  components: {
    [Tabbar.name]: Tabbar, 
    [TabbarItem.name]: TabbarItem,
    [NavBar.name]: NavBar
  },
  computed: {},
  methods: {}
};
</script>

<style>
body {
  font-size: 16px;
  background-color: #f8f8f8;
  -webkit-font-smoothing: antialiased;
}
</style>
