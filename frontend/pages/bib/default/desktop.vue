<template>
  <div class="bib-user-desktop">
    <v-row class="top-menu ms-5 me-8 align-center justify-space-between">
        <v-col cols="2" class="search-bar d-flex">
          <input
              type="text"
              name="form-container"
              placeholder="Blade Runner..."
              id="form-area"
              v-model="searchField"
              @keyup="search(searchField)"

            />
        </v-col>
        <!-- <div class="filter-box d-flex">
          <v-icon class="icon">mdi-filter-menu</v-icon>
          <span class="header-title ms-2">Filtros</span>
        </div>  -->
    </v-row>

    <div class="sidebar">
      <div class="box-item d-flex align-center mt-2">
            <v-icon class="icon">mdi-cards-playing</v-icon>
            <div class="header-title item-title">Quizzes</div>
          </div>
          <v-divider class="divider-item"></v-divider>
          <div class="box-item d-flex align-center">
            <v-icon @click="openNewBook = true" class="icon">mdi-playlist-plus</v-icon>
            <div class="header-title item-title" >Criar Estante</div>

          </div>
          <v-divider class="divider-item"></v-divider>
          <div class="box-item d-flex align-center">
            <v-icon class="icon">mdi-human-greeting-proximity</v-icon>
            <div class="header-title item-title">Novo Match</div>

          </div>
          <v-divider class="divider-item"></v-divider>
          <div class="wrapper-div d-flex flex-column">
            <div class="box-item align-center d-flex">
              <v-icon class="icon">mdi-bookshelf</v-icon>
              <div class="header-title item-title">Estantes</div>
              <v-icon class="icon" v-if="!open" @click="open = true">mdi-chevron-down</v-icon>
              <v-icon class="icon" v-else @click="open = false">mdi-chevron-up</v-icon>
            </div>
            <div v-if="open" class="bookshelves d-flex flex-column mb-3">
              <div class="margin-left-page header-title">
                <router-link style="color: white" to="/userBib/bookshelf/1">Exemplo</router-link>
              </div>
            </div>
          </div>
          <v-divider class="divider-item"></v-divider>
          <div class="d-flex wrapper-div flex-column">
            <div class="box-item align-center d-flex">
              <v-icon class="icon">mdi-nut</v-icon>
              <div class="header-title item-title" >Configurações</div>
            </div>
            <!-- fazer configs !-->
          </div>
    </div>

    <div class="conteudo">
      <v-container fluid class="conteudo-box">
            <Nuxt />
          </v-container>
    </div>


  </div>
</template>

<script>
  import OpenNewBook from '~/components/bib/OpenNewBook'
  export default {
    components: { OpenNewBook },
    data(){
      return{
        open: false,
        searchField: '',
        openNewBook: false
      }
    }

  }
  </script>

<style lang="scss" scoped>

.top-menu{
  position: absolute;
  margin-top: $header-height;
  z-index: 1;
}

#form-area {
    height: 2.5vh;
    margin-top: 10px;
    margin-bottom: 10px;
    background-color: rgb(232, 229, 174, 0.64);
    border-radius: 20px;
    padding-left: 2vw;
  }

  .bib-user-desktop{
    background-color: $secondary-color !important;
    overflow: hidden;
    scrollbar-color: transparent;
    width: 100vw;
    overflow: hidden;
    min-height: 100vh;
  }

  .sidebar{
    background-color: $bg-color;
    width: 15vw;
    height: 100vh;
    z-index: 1;
    position: fixed;
    margin-top: $header-height;
  }

  .conteudo{
    margin-left: 15vw;
    position: relative;
    background-color: $secondary-color;
  }

  .box-item{
    height: 8vh;
    padding-left: 20%;
    gap: 1vw;
  }

  .divider-item{
    border-color: $primary-color !important;
  }

  .icon{
    color: $primary-color !important;
  }

  </style>
