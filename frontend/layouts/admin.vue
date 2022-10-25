<template>
  <v-app>
    <div class="admin-layout">
      <div class="sidebar d-flex flex-column justify-center">

        <div class="box-item d-flex align-center">
          <div class="header-title item-title">Olá admin!</div>
        </div>
        <v-divider class="divider-item" />
        <div class="box-item d-flex align-center pointer" @click="goTo('/addBook')">
          <v-icon class="icon">mdi-bookshelf</v-icon>
          <div class="header-title item-title">Livros</div>
        </div>
        <v-divider class="divider-item" />
        <div class="box-item d-flex align-center pointer" @click="goTo('/addAuthor')">
          <v-icon class="icon">mdi-account-cowboy-hat</v-icon>
          <div class="header-title item-title">Autores</div>
        </div>
        <v-divider class="divider-item" />
        <div class="box-item d-flex align-center pointer" @click="goTo('/addQuestion')">
          <v-icon class="icon">mdi-notebook</v-icon>
          <div class="header-title item-title">Questões</div>
        </div>

      </div>

      <div class="conteudo">
        <v-container fluid class="conteudo-box">
          <Nuxt />
        </v-container>
      </div>
    </div>
  </v-app>
</template>

<script>

export default {
  data() {
    return {};
  },
  methods: {
    goTo(path) {
      this.$router.push({
        path: 'admin' + path
      })
    }
  }
};
</script>

<style lang="scss" scoped>
.admin-layout {
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
</style>
