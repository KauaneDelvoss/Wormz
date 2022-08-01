<template>
  <v-app class="search-bib">
    <ImgBackground>
    <div class="app">
      <div class="d-flex flex-column align-center mt-10">
        <div class="h1">Wormz</div>
        <v-divider color="#E8E5AE" style="width:15%"></v-divider>
        <div class="subtitulo mt-12 text-center">Pesquise por título ou por autor:</div>
      </div>

      <div class="form-container d-flex flex-column align-center mt-10">
          <input type="text" name="form-container" placeholder="Blade Runner..." id="form-area">
          <div class="icon-search d-flex flex-column">
            <v-img src="../assets/images/Search.png" alt="Search" style="bottom: 3vh; left: 33vw;" />
          </div>
          <v-icon style="width: 100%; left: 15vw" class="flex-column align-start" color="#e8e5ae">mdi-filter-menu</v-icon>

      </div>
    </div>
    </ImgBackground>
  </v-app>
</template>

<script>
import ImgBackground from "@/components/basic/ImgBackground.vue"
export default {
  components: { ImgBackground }
};
</script>

<style scoped>
template {
  overflow: hidden;
}

#form-area{
    width: 70vw;
    height: 4vh;
    background-color: rgb(232, 229, 174, 0.64);
    border-radius: 20px;
    padding-left: 2vw;
}

.icon-search{
    position: relative;
    width: 1%;
}

</style>
