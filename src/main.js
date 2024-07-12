import { createApp } from 'vue';
import App from './App.vue';
import { router } from './router';

const app = createApp(App);
app.config.globalProperties.$DTGlobe = []
app.use(router);
app.mount('#app');
