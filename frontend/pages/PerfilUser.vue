<template>
  <div class="profile">
    <div class="box-profile">
      <ImgBackground style="width: 100%">
        <v-row class="row-wrapper">
          <v-col cols="4" class="d-flex align-center justify-center">
            <v-icon size="30vh" class="v-icon-item">mdi-account-circle</v-icon>
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
              <div class="h3 ms-3">{{user.first_name}}{{user.last_name}}</div>
            </div>
            <div
              class="local-wrapper d-flex flex-row mt-3"
              style="opacity: 90%"
            >
              <v-icon class="v-icon-item">mdi-google-maps</v-icon>
              <div class="h3 ms-3">Local</div>
            </div>
          </v-col>
        </v-row>
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
            <div class="subtitulo mt-5">
              {{ user.user_biography }}
            </div>
          </div>
          <div class="box-books">
            <div class="h3 bookshelf-name margin-left-page mt-5">Favoritos</div>
            <BooksCarousel class="mx-7" />
          </div>
        </div>

        <div v-if="active == 1">
          <div class="h3 bookshelf-name margin-left-page mt-5">Favoritos</div>
          <BooksCarousel  /> <!-- erro ! (não aceita mais de um uso na pg)-->
          <div class="h3 bookshelf-name margin-left-page mt-5">Dark Vibes</div>
          <BooksCarousel />
        </div>

        <div v-if="active == 2" class="margin-left-page margin-right-page">
          <v-card elevation="2" class="review-card">
            <div class="d-flex flex-row align-center div-wrapper">
                <div class="h3 bookshelf-name px-5 py-5">
                Em Despertar dos Deuses
                </div>
                <v-rating
                empty-icon="mdi-star-outline"
                full-icon="mdi-star"
                half-icon="mdi-star-halffull"
                class="v-rating"
                readonly
                length="5"
                :value="3"
                ></v-rating>
            </div>
            <v-divider class="hr"></v-divider>
            <div class="subtitulo px-5 py-5">Trecho da review ...</div>
          </v-card>
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
import {mapState} from 'vuex'
export default {
  data() {
    return {
      items: ["OVERVIEW", "ESTANTES", "AVALIAÇÕES"],
      active: 0,
    };
  },
  middleware: 'auth',
  computed: {
    ...mapState('auth', ['user'])
  }
};
</script>

<style lang="scss" scoped>
@include breakpoints;

@media (max-width: $phone_l) {
  .row-wrapper{
    flex-direction: column !important;
    align-content: center;
    justify-content: center;
  }
  .col-mobile{
    margin-top: -4vh;
    gap: 5px;
  }
  .h1.mobile{
      font-size: 5vh !important;
  }
  .nav-mobile{
    justify-content: center;
  }
  .header-title-mobile{
    font-size: 1.5vh !important;
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