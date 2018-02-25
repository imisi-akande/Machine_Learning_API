<template>
  <!-- Header -->
  <div>
  <header class="w3-display-container w3-content" style="max-width:1500px;">
    <img
      class="w3-image"
      src="../assets/fakenews.png"
      alt="The Fake News"
      style="min-width:1000px"
      width="1500"
      height="800"
     >
    <div class="w3-display-left w3-padding w3-col l6 m8">
      <div class="w3-container w3-red">
        <h2><i class="fa fa-balance-scale w3-margin-right"></i>Investigation Panel</h2>
      </div>
      <div class="w3-container w3-white w3-padding-16">
        <form>
          <div class="w3-row-padding" style="margin:0 -16px;">
            <div class="w3-card w3-margin-bottom">
              <label><i class="fa fa-edit"></i> News</label>
              <textarea
              placeholder="Enter a sentence or phrase to validate ..."
              class="w3-input w3-margin-bottom"
              v-model="searchPhrase">
              </textarea>
            </div>
          </div>
          <button
            class="w3-button w3-red"
            v-on:click="searchNews"
            v-bind:disabled="disenableValidateButton"
            type="submit">
            <i class="fa fa-search w3-margin-right"></i>
            Validate this news
           </button>
        </form>
      </div>
    </div>
  </header>

  <!-- Page content -->
  <div class="w3-content" style="max-width:1532px;">
      <p v-if="message" class="w3-pink w3-center" autofocus>{{ message }}</p>
      <!-- pagnition -->
      <div class="w3-bar w3-center">
         <a
          v-if="previousUrl"
          v-on:click="getNews(previousUrl)"
          href="#"
          class="w3-button w3-hover-teal">
          « Previous Page
        </a>
         <a
          v-if="nextUrl"
          v-on:click="getNews(nextUrl)"
          href="#"
          class="w3-button w3-hover-teal">
          Next Page »
        </a>
      </div>
      <!-- new list -->
      <div class="w3-row-padding w3-padding-16">
         <div
          class=" w3-third w3-margin-bottom"
          v-for="news in newsBoard"
          v-bind:key="news.id"
          >
          <h4 class="w3-block w3-padding  newHeadline"> {{ news.headline}} </h4>
          <div class="w3-container w3-white">
            <div class="newcontainer">
              <p >
                {{ news.body }}
              </p>
            </div>
            <p class="w3-large">
              <i class="fa fa-calendar"></i>
              <i>{{ new Date('2011-04-11T10:20:30Z').toUTCString() }}</i>
             </p>

            <button
              v-if="news.fakeness===0"
              class="w3-button w3-block w3-indigo w3-margin-bottom"
              >Real News
             </button>
            <button
              v-else
              class="w3-button w3-block w3-grey w3-margin-bottom"
              >Fake News
             </button>
          </div>
        </div>
      </div>
      <!-- pagnition -->
      <div class="w3-bar w3-center">
        <a
          v-if="previousUrl"
          v-on:click="getNews(previousUrl)"
          href="#"
          class="w3-button w3-hover-teal">
          « Previous Page
        </a>
         <a
          v-if="nextUrl"
          v-on:click="getNews(nextUrl)"
          href="#"
          class="w3-button w3-hover-teal">
          Next Page »
        </a>
      </div>
     </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'HelloWorld',
  data() {
    return {
      newsBoard: [],
      message: null,
      searchPhrase: '',
      currentPage: 0,
      disenableValidateButton: true,
      nextUrl: null,
      previousUrl: null,
    };
  },
  methods: {
    searchNews(event) {
      event.preventDefault();
      const searchText = this.searchPhrase;
      this.message = 'Investigating this news snippet';
      /* eslint-disable quote-props */
      axios.get(`/api/news/?q=${searchText}&limit=9&offset=0`)
        .then((result) => {
          this.message = null;
          this.newsBoard = result.data.results;
          this.nextUrl = result.data.next;
          this.previousUrl = result.data.previous;
        })
        .catch(() => {
          this.message = 'An error occurred, Please try again or contact us';
        });
    },
    getNews(url) {
      if (event) {
        event.preventDefault();
      }
      const apiurl = url.toString();
      const indexofAPi = apiurl.toString().indexOf('api');
      const searchUrl = `/${apiurl.substring(indexofAPi, apiurl.length)}`;
      this.message = 'Fetching news .....';
      /* eslint-disable quote-props */
      /* eslint-disable func-names */
      axios.get(searchUrl)
        .then((result) => {
          this.message = null;
          this.newsBoard = result.data.results;
          this.nextUrl = result.data.next;
          this.previousUrl = result.data.previous;
        })
        .catch(() => {
          this.message = 'An error occurred, Please try again or contact us';
        });
    },
  },
  mounted() {
    if (this.$route.params.type) {
      const searchValue = (this.$route.params.type === 'fake') ? 1 : 0;
      this.getNews(`/api/news/?limit=9&offset=0&search=${searchValue}`);
    }
  },
  watch: {
    searchPhrase(val) {
      if (val) {
        this.disenableValidateButton = false;
      } else {
        this.disenableValidateButton = true;
      }
    },
    '$route.params.type': function (val) {
      const searchValue = (val === 'fake') ? 1 : 0;
      this.getNews(`/api/news/?limit=9&offset=0&search=${searchValue}`);
    },
  },
};
</script>

<style>
.l6 {
  margin-top: 15%;
}
.newHeadline{
  background-color: #D5D2D4;
  margin-bottom: 0px !important;
  height: 50px;
  overflow: scroll;
}
.newcontainer{
  height: 200px !important;
  overflow: scroll;
}
.router-link-exact-active{
  border-bottom-style: solid !important;
  border-bottom-color: coral !important;
}
</style>
