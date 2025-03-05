<template>
  <div>
    <h2>Логін</h2>
    <input type="text" v-model="username" placeholder="Логін">
    <input type="password" v-model="password" placeholder="Пароль">
    <button @click="login">Увійти</button>
    <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      username: '',
      password: '',
      errorMessage: ''
    };
  },
  methods: {
    async login() {
      try {
        const response = await axios.post('/api/token/', {
          username: this.username,
          password: this.password
        });
        localStorage.setItem('access_token', response.data.access);
      } catch (error) {
        this.errorMessage = error.response?.data?.detail || 'Помилка входу';
      }
    }
  }
};
</script>
