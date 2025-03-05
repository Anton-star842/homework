import { describe, it, expect, beforeEach, vi } from 'vitest';
import { mount, flushPromises } from '@vue/test-utils';
import Login from '../views/Login.vue';
import axios from 'axios';

vi.mock('axios'); // Мокаємо axios

beforeEach(() => {
  localStorage.clear();
});

describe('Login.vue', () => {
  it('відображає форму входу', () => {
    const wrapper = mount(Login);

    expect(wrapper.find('h2').text()).toBe('Логін');
    expect(wrapper.find('input[type="text"]').exists()).toBe(true);
    expect(wrapper.find('input[type="password"]').exists()).toBe(true);
    expect(wrapper.find('button').exists()).toBe(true);
  });

  it('успішний логін', async () => {
    axios.post.mockResolvedValue({ data: { access: 'test-token' } });

    const wrapper = mount(Login);
    await wrapper.find('input[type="text"]').setValue('testuser');
    await wrapper.find('input[type="password"]').setValue('password');
    await wrapper.find('button').trigger('click');

    await flushPromises(); // Чекаємо оновлення стану

    expect(localStorage.getItem('access_token')).toBe('test-token');
  });

  it('невдалий логін', async () => {
    axios.post.mockRejectedValue({ response: { data: { detail: 'Невірний логін або пароль' } } });

    const wrapper = mount(Login);
    await wrapper.find('input[type="text"]').setValue('wronguser');
    await wrapper.find('input[type="password"]').setValue('wrongpass');
    await wrapper.find('button').trigger('click');

    await flushPromises(); // Чекаємо оновлення стану

    expect(wrapper.find('.error').exists()).toBe(true);
    expect(wrapper.find('.error').text()).toBe('Невірний логін або пароль');
  });
});
