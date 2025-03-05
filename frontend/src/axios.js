import axios from 'axios';

const instance = axios.create({
  baseURL: 'http://localhost:8000/api/', // URL твого Django API
  timeout: 1000,
});

export default instance;
