<template>
  <div>
    <h2>Ваші курси та рейтинг</h2>
    <ul>
      <li v-for="course in courses" :key="course.id">
        <strong>{{ course.title }}</strong> - Опис: {{ course.description }}
        <p>Рейтинг: {{ course.rating }}</p>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from '../axios';

export default {
  data() {
    return {
      courses: [],
    };
  },
  created() {
    this.fetchCourses();
  },
  methods: {
    async fetchCourses() {
      try {
        const response = await axios.get('courses/');
        this.courses = response.data;
      } catch (error) {
        console.error('Error fetching courses:', error);
      }
    },
  },
};
</script>
