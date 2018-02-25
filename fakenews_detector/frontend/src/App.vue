<template>
  <div id="app">
    <router-view/>
    <Footer></Footer>
  </div>
</template>

<script>
import NavBar from './components/NavBar';
import Footer from './components/Footer';

export default {
  name: 'App',
  components: {
    NavBar,
    Footer,
  },
};
</script>

