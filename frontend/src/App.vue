<template>
  <div>
    <nav>
      <router-link to="/">Home</router-link> |
      <router-link to="/Inventory">Inventory</router-link> |
      <router-link to="/Orders">Orders</router-link> |
      <router-link to="/Processes">Processes</router-link> |
      <router-link to="/Shipments">Shipments</router-link>
    </nav>
    <router-view />
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
