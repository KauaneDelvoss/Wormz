<template>
  <div class="bib-user-desktop">

    <div class="sidebar">
        <div class="search-bar d-flex justify-center">
          <input
            type="text"
            name="form-container"
            placeholder="Blade Runner..."
            id="form-area"
            v-model="searchField"
            @keyup.enter="search(searchField)"
          />
        </div>
        <!-- <div class="filter-box d-flex">
            <v-icon class="icon">mdi-filter-menu</v-icon>
            <span class="header-title ms-2">Filtros</span>
          </div>  -->

      <v-divider class="divider-item mt-2" />
      <div class="box-item d-flex align-center">
        <v-icon class="icon">mdi-cards-playing</v-icon>
        <div class="header-title item-title">Quizzes</div>
      </div>
      <v-divider class="divider-item" />
      <div
        class="box-item d-flex align-center pointer"
        @click="openNewBook = true"
      >
        <v-icon class="icon">mdi-playlist-plus</v-icon>
        <div class="header-title item-title">Criar Estante</div>
      </div>
      <v-divider class="divider-item" />
      <div class="box-item d-flex align-center">
        <v-icon class="icon">mdi-human-greeting-proximity</v-icon>
        <div class="header-title item-title">Novo Match</div>
      </div>
      <v-divider class="divider-item" />
      <div class="wrapper-div d-flex flex-column">
        <div class="box-item align-center d-flex">
          <v-icon class="icon">mdi-bookshelf</v-icon>
          <div class="header-title item-title">Estantes</div>
          <v-icon class="icon" v-if="!open" @click="open = true"
            >mdi-chevron-down</v-icon
          >
          <v-icon class="icon" v-else @click="open = false"
            >mdi-chevron-up</v-icon
          >
        </div>
        <div v-if="open" class="bookshelves d-flex flex-column mb-3">
          <div v-for="bookshelf in bookshelves" :key="bookshelf.id" class="ms-12 header-title">
            <router-link style="color: white" :to="'/userBib/' + user.username + '/bookshelf/' + bookshelf.id"
              >{{ bookshelf.bookshelf_name }}</router-link
            >
          </div>
        </div>
      </div>
      <v-divider class="divider-item" />
      <div class="d-flex wrapper-div flex-column">
        <div class="box-item align-center d-flex">
          <v-icon class="icon">mdi-nut</v-icon>
          <div class="header-title item-title pointer" @click="openConfig = true">Configurações</div>
        </div>
        <!-- fazer configs !-->
      </div>
      <!-- <div class="d-flex wrapper-div flex-column">
        <div class="box-item align-center d-flex">
          <div class="header-title item-title pointer">
            <router-link :to="'/book/1'">Teste Livro</router-link>
          </div>
        </div>
      </div> -->
    </div>

    <div class="conteudo">
      <v-container fluid class="conteudo-box">
        <Nuxt />
      </v-container>
    </div>

    <OpenNewBook :dialog="openNewBook" @close="openNewBook = false" />
    <ConfigUser :dialog="openConfig" @close="openConfig = false" />
  </div>
</template>

<script>
import OpenNewBook from "~/components/bib/OpenNewBook";
import ConfigUser from "~/components/ConfigUser"
import { mapActions, mapState } from 'vuex'

export default {
  components: { OpenNewBook, ConfigUser },
  data() {
    return {
      open: false,
      searchField: "",
      openNewBook: false,
      openConfig: false
    };
  },
  mounted(){
    this.GET_BOOKSHELVES(this.user.username)
    console.log(this.bookshelves)
  },
  methods:{
    ...mapActions('bookshelf', ["GET_BOOKSHELVES"])
  },
  computed: {
    ...mapState('bookshelf', ["bookshelf", "bookshelves"]),
    ...mapState('auth', ["user"])
  }
};
</script>

<style lang="scss" scoped>
.search-bar{
  margin-top: $header-height;
}

#form-area {
  height: 3vh;
  margin-top: 10px;
  background-color: rgb(232, 229, 174, 0.64);
  border-radius: 20px;
  padding-left: 2vw;
  width: 14vw;
  font-size: 0.7rem;
}

.bib-user-desktop {
  background-color: $secondary-color !important;
  overflow: hidden;
  scrollbar-color: transparent;
  width: 100vw;
  overflow: hidden;
  min-height: 100vh;
}

.sidebar {
  background-color: $bg-color;
  width: 15vw;
  height: 100vh;
  z-index: 1;
  position: fixed;
  bottom: 0;
}

.conteudo {
  margin-left: 15vw;
  position: relative;
  background-color: $secondary-color;
}

.box-item {
  height: 8vh;
  padding-left: 20%;
  gap: 1vw;
}

.divider-item {
  border-color: $primary-color !important;
}

.icon {
  color: $primary-color !important;
}

.pointer:hover {
  cursor: pointer;
}

.search-bar {
  width: 15vw;
}
</style>
