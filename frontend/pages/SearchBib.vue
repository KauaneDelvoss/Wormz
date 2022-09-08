<template>
  <v-app class="search-bib">
    <v-container fluid>

        <v-row class="mobile-profile">
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
            v-model="searchField"
            @keyup.enter="search()"
            
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

        <div v-if="searchField.length > 0" class="margin-left-page margin-right-page">
          <div class="h3 mt-10 mb-2">Resultados da sua pesquisa: </div>
          <v-row>
            <v-col cols="12">
                <BooksCarousel :books="books" />
            </v-col>
          </v-row>
        </div>

        <!--
          <div class="margin-left-page margin-right-page static-data">
            <div class="h3 mt-10 mb-2">Destaques em ficção científica:
              <BooksCarousel :books="searchStatic()" />
            </div>
          </div>
        !-->
    </v-container>
  </v-app>
</template>

<script>
import CardBooks from "@/components/basic/CardBooks.vue";
import ImgBackground from "@/components/basic/ImgBackground.vue";
import { mapState } from "vuex";

export default {
  data(){
    return{
      searchField: ''
    }
  },
  middleware: 'auth',
  components: { ImgBackground, CardBooks },
  methods: {
    search(){
      this.$store.commit(
      "google_books/MAKE_URL_SEARCH",
      this.searchField
    );
    this.$store.dispatch("google_books/GET_URL");
    }
  },
  computed: {
    ...mapState("google_books", ["books"]),

    // NECESSÁRIO GETTER !
    //seacrhStatic(){
      //this.$store.commit("google_books/MAKE_URL_SEARCH", "Phillip K Dick")
      //this.$store.dispatch("google_books/GET_URL");
      //return 
    //}
  }
};
</script>

<style lang="scss" scoped>
@include breakpoints;

template {
  overflow-x: hidden;
}

.search-bib{
  background-color: $bg-color !important;
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
