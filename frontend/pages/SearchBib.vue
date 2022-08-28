<template>
  <v-app class="search-bib">
        <v-row>
          <v-col class="ms-md-12 d-flex flex-column align-center col-default">
            <div class="d-flex flex-column">
              <div class="h1">Wormz</div>
              <v-divider id="divider" class="mb-n4" color="#E8E5AE"></v-divider>
              <div class="subtitulo mt-12 text-center">
                Procure por livro ou por autor:
              </div>
            </div>
          </v-col>
        </v-row>

        <div class="form-container d-flex flex-column align-center mt-10">
          <input
            type="text"
            name="form-container"
            placeholder="Blade Runner..."
            id="form-area"
            
          />
          <div class="icon-search d-flex flex-column">
            <v-img
              src="../assets/images/Search.png"
              alt="Search"
              style="bottom: 3vh; left: 33vw"
            />
          </div>
          <v-icon
            style="width: 100%; left: 15vw"
            class="flex-column align-start mb-2"
            color="#e8e5ae"
            >mdi-filter-menu</v-icon
          >
        </div>

        <div class="margin-left-page margin-right-page">
          <div class="h3 mt-10 mb-2">Destaques</div>
          <v-row>
            <v-col cols="12" class="ps-5 pe-5">
                <BooksCarousel />
            </v-col>
          </v-row>
        </div>
  </v-app>
</template>

<script>
import CardBooks from "@/components/basic/CardBooks.vue";
import ImgBackground from "@/components/basic/ImgBackground.vue";
import { mapState } from "vuex";

export default {
  components: { ImgBackground, CardBooks },
  computed: {
    ...mapState("search_books", ["books"]),
  },
};
</script>

<style lang="scss" scoped>
@include breakpoints;

template {
  overflow-x: hidden;
}

.search-bib{
  background-color: $bg-color;
  max-width: 100vw;
}

#form-area {
  width: 70vw;
  height: 4vh;
  background-color: rgb(232, 229, 174, 0.64);
  border-radius: 20px;
  padding-left: 2vw;
}

.icon-search {
  position: relative;
  width: 1%;
}
</style>
