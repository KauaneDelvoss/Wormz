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
            class="d-flex justify-center flex-column justify-center"
          >
            <div class="h1">Usuário</div>
            <div
              class="local-wrapper d-flex flex-row mt-n5"
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
      <v-row class="mt-3 mb-3">
        <div
          v-for="(item, i) in items"
          :key="i"
          @click="active = i"
          class="header-title margin-left-page bookshelf-name"
        >
          {{ item }}
        </div>
      </v-row>
      <v-divider class="hr"></v-divider>
    </div>
    <v-row class="mt-5">
      <v-col cols="9">
        <div v-if="active == 0">
          <div class="margin-left-page" style="max-width: 40vw">
            <div class="h3">Título da biografia</div>
            <div class="subtitulo mt-5">
              Lorem ipsum dolor sit amet, consectetur adipiscing elit. Eget a a
              ac, fermentum, id amet, sagittis. Urna justo fermentum in nascetur
              elementum ornare. Phasellus blandit proin molestie elit, etiam et
              in duis purus. In quis placerat nisl aliquam ullamcorper tristique
              a, suspendisse velit.
            </div>
          </div>
          <div class="box-books">
            <div class="h3 bookshelf-name margin-left-page mt-5">Favoritos</div>
            <BooksCarousel />
          </div>
        </div>

        <div v-if="active == 1">
          <div class="h3 bookshelf-name margin-left-page mt-5">Favoritos</div>
          <BooksCarousel />
          <div class="h3 bookshelf-name margin-left-page mt-5">Dark Vibes</div>
          <BooksCarousel />
        </div>

        <div v-if="active == 2" class="margin-left-page margin-right-page">
          <v-card elevation="2" class="review-card">
            <div class="d-flex flex-row align-center">
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
                value="3"
                ></v-rating>
            </div>
            <v-divider class="hr"></v-divider>
            <div class="subtitulo px-5 py-5">Trecho da review ...</div>
          </v-card>
        </div>
      </v-col>
      <v-col cols="auto">
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
export default {
  data() {
    return {
      items: ["OVERVIEW", "ESTANTES", "AVALIAÇÕES"],
      active: 0,
    };
  },
};
</script>

<style lang="scss" scoped>
.profile {
  background-color: $bg-color;
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