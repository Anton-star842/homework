import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import axios from 'axios';

// Налаштування axios для автоматичного додавання JWT-токена до кожного запиту
axios.interceptors.request.use(config => {
  const token = localStorage.getItem('access_token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

const app = createApp(App);

app.use(router);
app.config.globalProperties.$axios = axios; // Додаємо axios у глобальні змінні
app.mount('#app');
