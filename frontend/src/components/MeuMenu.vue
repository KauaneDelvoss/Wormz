<template>
  <v-app id="inspire">

    <v-app-bar
      app
      color="#434C6D"
      flat
      outlined 
    >
      <v-avatar
        :color="$vuetify.breakpoint.smAndDown ? 'grey darken-1' : 'transparent'"
        size="32"
      ></v-avatar>

      <v-tabs
        left
        class="ml-n20"
        color="#E8E5AE"
        slider-color="#E8E5AE"
        background-color="#434C6D"
        
  
      >
        <v-tab
          v-for="link in links"
          :key="link"
        >
          {{ link }}
        </v-tab>
      </v-tabs>

      <v-avatar
        class="hidden-sm-and-down"
        color="grey darken-1 shrink"
        size="32"
      ></v-avatar>
    </v-app-bar>

    <v-main class="white"
    >
      <p>oi</p>
    </v-main>
  </v-app>
</template>

<script>
  export default {
    data: () => ({
      links: [
        'Explorar',
        'Biblioteca',
        'Quizz'
      ],
    }),
  }
</script>
<style scoped>
  .v-toolbar__content {
    width:834 px;
    height: 10vh;
  }
  .v-sheet v-sheet--outlined theme--light v-toolbar v-toolbar--flat v-app-bar v-app-bar--fixed v-app-bar--is-scrolled {
    height: 10vh;
  }
</style>