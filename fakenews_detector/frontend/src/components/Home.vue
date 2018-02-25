<template>
  <!-- Header -->
  <div>

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
      <form>
       <button
          class="w3-button w3-red w3-right w3-round-large"
          v-on:click="searchNews"
          title="Click to Search"
          v-bind:disabled="disenableValidateButton"
          type="submit">
          <i class="fa fa-search w3-margin-right"></i>
        </button>
        <input
        type="text"
        v-model="searchPhrase"
        placeholder="Enter a phrase to search ..."
        style="min-width: 40%; margin-right:2px"
        class="w3-bar-item w3-input w3-right w3-border-pink w3-border  w3-round-large" />
       </form>
  </div>

  <!-- Page content -->
  <div class="w3-content" style="max-width:1532px;">
      <p v-if="message" class="w3-pink w3-center" autofocus>{{ message }}</p>
      <!-- modal start -->
      <div
        v-if="currentNews"
        class="w3-container">
        <div
          id="currentNewsDiv"
          class="w3-modal"
          v-bind:style="currentNewsDiv">
          <div class="w3-modal-content w3-animate-top w3-card-4">
            <header class=" currentNewsHeader w3-container">
              <span v-on:click="closeCurrentNewsDiv"
              class="w3-button w3-display-topright w3-hover-grey">&times;</span>
              <h2>{{ currentNews.headline }}</h2>
            </header>
            <div class="w3-container">
              <p>{{ currentNews.body }} </p>
              <i class="fa fa-calendar w3-right">
                  {{ new Date(currentNews.pub_date).toUTCString() }}
              </i>
              <br/>
            </div>
            <footer class="currentNewsHeader w3-container">
              <button
              v-if="currentNews.fakeness===0"
                class="w3-button w3-block w3-indigo w3-hover-indigo"
                >Real News
               </button>
              <button
                v-else
                class="w3-button w3-grey w3-block w3-hover-grey"
                >Fake News
               </button>

               <button v-on:click="closeCurrentNewsDiv"
                class="w3-button w3-block w3-grey w3-hover-red">Close</button>
                <br/>
            </footer>
          </div>
        </div>
      </div>
      <!-- modal ends -->
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
      <div class="w3-row-padding w3-padding-16" v-if="newsBoard.length!==0">
         <div
          class=" w3-third w3-margin-bottom"
          v-for="news in newsBoard"
          v-bind:key="news.id"
          >
          <h6 class="w3-block w3-padding  newHeadline">
            {{ news.headline}}
           </h6>
          <div class="w3-container w3-white">
            <div class="newcontainer">
              <p >
                {{ news.body }}
              </p>
            </div>
            <p class="w3-right">
              <i class="fa fa-calendar datePub"></i>
              <i>{{ new Date(news.pub_date).toUTCString() }}</i>
             </p>

              <button
                v-if="news.fakeness===0"
                  class="w3-button w3-block w3-indigo w3-hover-indigo"
                  >Real News
               </button>
              <button
                v-else
                class="w3-button w3-grey w3-block w3-hover-grey"
                >Fake News
               </button>

              <p class=" w3-center w3-blue-grey">
                &nbsp; Read the Complete news
                <i
                  class="readmore"
                  v-on:click="completeNews(news.id)"
                 > here </i>
              </p>
          </div>
        </div>
      </div>
      <!-- home div -->
       <div class="w3-row-padding w3-padding-6 " v-if="isInitial">
         <div class="w3-panel w3-leftbar w3-light-blue">
          <p class=" w3-serif">
            <i class=" w3-serif">"Lies sound like facts to those
            who've been conditioned to mis-recognize the truth."</i>
            - DaShanne Stokes
          </p>
        </div>
         <div
          class=" w3-half w3-margin-bottom"
          v-for="news in initialNews"
          v-bind:key="news.id"
          >
          <h6
           v-if="news.fakeness===0"
           class=" w3-block w3-padding w3-blue">
            Is it the latest <i>Real</i> news in the world
          </h6>
          <h6
           v-else
           class=" w3-block w3-padding w3-light-blue">
            Or  the Latest <i>Fake</i> news in the world
          </h6>
          <h6 class="w3-block w3-padding  newHeadline">
            {{ news.headline}}
           </h6>
          <div class="w3-container w3-white">
            <div class="newcontainer">
              <p >
                {{ news.body }}
              </p>
            </div>
            <p class="w3-right">
              <i class="fa fa-calendar datePub"></i>
              <i>{{ new Date(news.pub_date).toUTCString() }}</i>
            </p>

            <button
              v-if="news.fakeness===0"
                class="w3-button w3-block w3-indigo w3-hover-indigo"
                >Real News
             </button>
            <button
              v-else
              class="w3-button w3-grey w3-block w3-hover-grey"
              >Fake News
             </button>

              <p class="w3-center w3-blue-grey">
                Read the Complete news
                <i
                  class="readmore"
                  v-on:click="completeNews(news.id)"
                 > here </i>
              </p>
          </div>
        </div>
      </div>
      <!-- home div end -->
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
/* eslint-disable quote-props */
/* eslint-disable quotes */
/* eslint-disable indent */
/* eslint-disable comma-dangle  */

export default {
  name: 'Test',
  data() {
    return {
      initialNews: [
        {
            "id": 1,
            "headline": "Muslims BUSTED: They Stole Millions In Govt Benefits",
            "body": "Print They should pay all the back all the money plus interest. The entire family and everyone who came in with them need to be deported asap. Why did it take two years to bust them? Here we go again another group stealing from the government and taxpayers! A group of Somalis stole over four million in government benefits over just 10 months! Weve reported on numerous cases like this one where the Muslim refugees/immigrants commit fraud by scamming our systemIts way out of control! More Related",
            "pub_date": "2016-10-26T18:41:00Z",
            "fakeness": 0
        },
        {
            "id": 2,
            "headline": "Re: Why Did Attorney General Loretta Lynch Plead The Fifth?",
            "body": "Why Did Attorney General Loretta Lynch Plead The Fifth? Barracuda Brigade 2016-10-28 Print The administration is blocking congressional probe into cash payments to Iran. Of course she needs to plead the 5th. She either cant recall, refuses to answer, or just plain deflects the question. Straight up corruption at its finest! 100percentfedUp.com ; Talk about covering your ass! Loretta Lynch did just that when she plead the Fifth to avoid incriminating herself over payments to IranCorrupt to the core! Attorney General Loretta Lynch is declining to comply with an investigation by leading members of Congress about the Obama administrations secret efforts to send Iran $1.7 billion in cash earlier this year, prompting accusations that Lynch has pleaded the Fifth Amendment to avoid incriminating herself over these payments, according to lawmakers and communications exclusively obtained by the Washington Free Beacon. Sen. Marco Rubio (R., Fla.) and Rep. Mike Pompeo (R., Kan.) initially presented Lynch in October with a series of questions about how the cash payment to Iran was approved and delivered. In an Oct. 24 response, Assistant Attorney General Peter Kadzik responded on Lynchs behalf, refusing to answer the questions and informing the lawmakers that they are barred from publicly disclosing any details about the cash payment, which was bound up in a ransom deal aimed at freeing several American hostages from Iran. The response from the attorney generals office is unacceptable and provides evidence that Lynch has chosen to essentially plead the fifth and refuse to respond to inquiries regarding [her]role in providing cash to the worlds foremost state sponsor of terrorism, Rubio and Pompeo wrote on Friday in a follow-up letter to Lynch. More Related",
            "pub_date": "2016-10-29T05:47:11.259000Z",
            "fakeness": 1
        },
      ],
      newsBoard: [],
      message: null,
      searchPhrase: '',
      currentPage: 0,
      disenableValidateButton: true,
      nextUrl: null,
      previousUrl: null,
      currentNews: null,
      isInitial: true,
      currentNewsDiv: { display: 'none' },
    };
  },
  /* eslint-disable quote-props */
  methods: {
    closeCurrentNewsDiv(event) {
      event.preventDefault();
      this.currentNewsDiv = { display: 'none' };
    },
    completeNews(id) {
      const newID = id - 1;
      if (this.isInitial) {
        this.currentNews = this.initialNews[newID];
      } else {
        this.isInitial = false;
        this.currentNews = this.newsBoard.filter(news => news.id === id)[0];
      }
      this.currentNewsDiv = { display: 'block' };
    },
    searchNews(event) {
      event.preventDefault();
      const searchText = this.searchPhrase;
      this.message = 'Investigating this news snippet';
      if (!this.newsBoard.length) {
        this.isInitial = true;
      } else {
        this.isInitial = false;
      }
      axios.get(`/api/news/?q=${searchText}&limit=9&offset=0`)
        .then((result) => {
          if (result.data.results.length) {
            this.message = null;
          } else {
            if (!this.newsBoard.length) {
              this.isInitial = true;
            }
            this.message = 'No news was found, type another keyword or try again later';
          }
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
      this.message = 'Investaging this news snippet';
      if (!this.newsBoard.length) {
        this.isInitial = true;
      } else {
        this.isInitial = false;
      }
      /* eslint-disable quote-props */
      /* eslint-disable func-names */
      axios.get(searchUrl)
        .then((result) => {
          if (result.data.results.length) {
            this.message = null;
          } else {
            this.message = 'No news was found, type another keyword or try again later';
          }
          /* eslint-disable no-console */
          this.newsBoard = result.data.results;
          console.log(this.newsBoard, result.data.results);
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
  overflow: hidden;
  font-size: 14px;
}
.newcontainer{
  height: 200px !important;
  overflow: hidden;
  font-size: 12px;
}
.router-link-exact-active{
  border-bottom-style: solid !important;
  border-bottom-color: coral !important;
}
.readmore{
  color: #F28032;
  cursor: pointer;
}
.currentNewsHeader {
  background-color: #D5D2D4;
  margin-bottom: 0px !important;
  font-size: 14px;
}
.w3-leftbar {
    border-left: 6px solid #1FBCD3!important;
}
</style>
