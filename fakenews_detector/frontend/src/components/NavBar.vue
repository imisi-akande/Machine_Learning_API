<template>
  <div class="w3-bar w3-white w3-large">
    <a href="#" class="w3-bar-item w3-button w3-red w3-mobile">
      <i class="fa fa-home w3-margin-right"></i>
      Fake News Detector
     </a>
     <router-link
        to='/getNews/real'
        class="w3-bar-item w3-button w3-mobile w3-hover-teal">
        Real news
      </router-link>
      <router-link
        to='/getNews/fake'
        class="w3-bar-item w3-button w3-mobile w3-hover-teal">
        Fake news
      </router-link>
  </div>
</template>

<script>
export default {
  name: 'NavBar',
};
</script>

