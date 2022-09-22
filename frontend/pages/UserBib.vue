<template>
  <div class="bib-user">
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
    <v-divider class="divider-item mb-3" style="border-style:dashed;"></v-divider>
    <v-row>
      <v-col class="barra-lateral d-flex flex-column" cols="2">
        <div class="box-item d-flex align-center">
          <v-icon class="icon" large>mdi-cards-playing</v-icon>
          <div class="header-title item-title">Indicações</div>
        </div>
        <v-divider class="divider-item"></v-divider>
        <div class="box-item d-flex align-center">
          <v-icon class="icon" large>mdi-playlist-plus</v-icon>
          <div class="header-title item-title">Criar Estante</div>
          
        </div>
        <v-divider class="divider-item"></v-divider>
        <div class="box-item d-flex align-center">
          <v-icon class="icon" large>mdi-human-greeting-proximity</v-icon>
          <div class="header-title item-title">Novo Match</div>
          
        </div>
        <v-divider class="divider-item"></v-divider>
        <div class="wrapper-div d-flex flex-column">
          <div class="box-item align-center d-flex">
            <v-icon class="icon" large>mdi-bookshelf</v-icon>
            <div class="header-title item-title">Estantes</div>
            <v-icon class="icon" large v-if="!open" @click="open = true">mdi-chevron-down</v-icon>
            <v-icon class="icon" large v-else @click="open = false">mdi-chevron-up</v-icon>
          </div>
          <div v-if="open" class="bookshelves d-flex flex-column">
            <div class="margin-left-page header-title">Exemplo</div>
          </div>
        </div>
      </v-col>
      <v-col class="conteudo" cols="10">
        <v-container fluid fill-height class="conteudo-box">
          <router-view />
        </v-container>
      </v-col>
    </v-row>
  </div>
</template>

<script>
export default {
  data(){
    return{
      open: false,
      searchField: ''
    }
  }

}
</script>

<style lang="scss" scoped>
  #form-area {
  height: 2.5vh;
  margin-top: 10px;
  margin-bottom: 10px;
  background-color: rgb(232, 229, 174, 0.64);
  border-radius: 20px;
  padding-left: 2vw;
}

.bib-user{
  background-color: $secondary-color !important;
  overflow: hidden;
  scrollbar-color: transparent;
  height: $template-height;
  width: 100vw;
}

.barra-lateral{
  background-color: $bg-color;
  height: 100vh;
  position: sticky;
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