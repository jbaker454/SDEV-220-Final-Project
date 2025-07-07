import { createApp } from 'vue'
import App from './App.vue'

createApp(App).mount('#app')

// GET users
fetch('http://localhost:8000/api/users')
  .then(res => res.json())
  .then(data => console.log('Users:', data));

// POST user
fetch('http://localhost:8000/api/users', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({ name: 'Charlie' })
})
  .then(res => res.json())
  .then(data => console.log('Created:', data));