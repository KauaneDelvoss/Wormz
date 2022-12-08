<template>
  <div class="profile">
    <div class="box-profile">
      <ImgBackground style="width: 100%">
        <div class="d-flex flex-grow-1 row-wrapper mx-5">
          <v-col cols="4" class="d-flex align-center justify-center col-mobile mt-5">
            <v-icon :size="width" class="v-icon-item">mdi-account-circle</v-icon>
          </v-col>
          <v-col
            cols="auto"
            class="d-flex flex-column justify-center col-mobile"
          >
            <div class="h1 mobile">{{ user.username }}</div>
            <div
              class="local-wrapper d-flex flex-row mt-n5"
              style="opacity: 90%"
            >
              <div class="h3 mobile ms-3">{{user.first_name}} {{user.last_name}}</div>
            </div>
            <!-- <div
              class="local-wrapper d-flex flex-row mt-3"
              style="opacity: 90%"
            >
              <v-icon class="v-icon-item">mdi-google-maps</v-icon>
              <div class="h3 mobile ms-3">Local</div>
            </div> -->
          </v-col>
        </div>
      </ImgBackground>
    </div>
    <div class="nav-user-profile">
      <v-divider class="hr"></v-divider>
      <v-row class="mt-3 mb-3 nav-mobile">
        <div
          v-for="(item, i) in items"
          :key="i"
          @click="active = i"
          class="header-title header-title-mobile margin-left-page bookshelf-name"
        >
          {{ item }}
        </div>
      </v-row>
      <v-divider class="hr"></v-divider>
    </div>
    <v-row class="mt-5 nav-mobile">
      <v-col cols="9" class="col-mobile-content">
        <div v-if="active == 0">
          <div class="margin-left-page div-mobile-content" style="max-width: 40vw">
            <div class="h3">Biografia</div>
            <div class="header-title mt-5">
              {{ user.user_biography }}
            </div>
          </div>
          <div class="box-books">
            <div class="h3 bookshelf-name margin-left-page mt-5">Favoritos</div>
            <BooksCarousel carouselId="c1" :books="bookshelf" class="mx-7" />
          </div>
        </div>

        <div v-if="active == 1">
          <div v-for="bookshelf in bookshelves" :key="bookshelf.id">
            <div class="h3 bookshelf-name margin-left-page mt-5">{{ bookshelf.bookshelf_name }}</div>
            <BooksCarousel v-if="bookshelf.book.length > 0" :carouselId="'c' + bookshelf.id" :books="bookshelf.book"  />
          </div>
        </div>

        <div v-if="active == 2" class="margin-left-page margin-right-page">
          <ReviewUser />
        </div>
      </v-col>
      <v-col cols="auto hide-mobile-l">
        <v-row>
          <v-col cols="auto">
            <div class="subtitulo-minimo">CLASSIFICAÇÃO</div>
            <div class="h3">#1</div>
          </v-col>
          <v-col cols="auto">
            <div class="subtitulo-minimo">AVALIAÇÕES</div>
            <div class="h3">108</div>
          </v-col>
          <v-col cols="auto">
            <div class="subtitulo-minimo">SEGUIDORES</div>
            <div class="h3">43</div>
          </v-col>
        </v-row>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import ReviewUser from '~/components/user/ReviewUser'

export default {
  components: { ReviewUser },
  middleware: 'auth',
  data() {
    return {
      items: ["OVERVIEW", "ESTANTES", "AVALIAÇÕES"],
      active: 0,
    };
  },
  middleware: 'auth',
  mounted(){
    this.$store.dispatch("bib/GET_URL")
    this.GET_BOOKSHELVES(this.user.username)
    console.log(this.bookshelves)
  },
  methods:{
    ...mapActions('bookshelf', ["GET_BOOKSHELVES"])
  },
  computed: {
    ...mapState('auth', ['user']),
    ...mapState('bookshelf', ['bookshelves']),
    width(){
        switch (this.$vuetify.breakpoint.name) {
          case 'xs': return 200
          case 'sm': return 200
          case 'md': return 200
          case 'lg': return 200
          case 'xl': return 300
        }
      }
  }
};
</script>

<style lang="scss" scoped>
@include breakpoints;

@media (max-width: $phone_l) {
  .row-wrapper{
    flex-direction: column !important;
    align-content: center !important;
    justify-content: center !important;
  }
  .col-mobile{
    margin-top: -4vh;
    gap: 5px;
    max-width: 100% !important;
  }
  .h1.mobile{
      font-size: 4vh !important;
  }
  .h3.mobile{
    font-size: 3vh !important;
  }
  .nav-mobile{
    justify-content: center;
  }
  .header-title-mobile{
    font-size: 1.2vh !important;
    margin-right: $distance-margin;
  }
  .col-default-content{
    columns: 12 !important;
  }
  .div-mobile-content{
    max-width: 100vw !important;
  }
  .div-wrapper{
    flex-direction: column !important;
  }
}

.profile {
  background-color: $bg-color !important;
  min-height: 100vh;
}

.box-profile,
.row-wrapper {
  height: 45vh;
  overflow: hidden;
}

.hr {
  border-color: $primary-color;
}

.review-card {
  background-color: transparent;
}

</style>