<template>
  <v-app class="search-bib">
    <ImgBackground>
      <div class="d-flex flex-column align-center mt-10">
        <div class="h1">Wormz</div>
        <v-divider color="#E8E5AE" style="width:15%"></v-divider>
        <div class="subtitulo mt-12 text-center">Pesquise por título ou por autor:</div>
      </div>

      <div class="form-container d-flex flex-column align-center mt-10">
          <input type="text" name="form-container" placeholder="Blade Runner..." id="form-area">
          <div class="icon-search d-flex flex-column">
            <v-img src="../assets/Search.png" alt="Search" style="bottom: 3vh; left: 33vw;" />
          </div>
          <v-icon style="width: 100%; left: 15vw" class="flex-column align-start" color="#e8e5ae">mdi-filter-menu</v-icon>

      </div>
    </ImgBackground>
  </v-app>
</template>

<script>
import ImgBackground from "../components/ImgBackground.vue";
export default {
  components: { ImgBackground },
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Alegreya+Sans+SC:wght@300&family=Encode+Sans&family=Libre+Baskerville&display=swap");

.h1 {
  font-family: "Libre Baskerville", serif;
  font-size: 10vh;
  text-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  color: #e8e5ae;
}

template {
  overflow: hidden;
}

.subtitulo {
  font-family: "Encode Sans", sans-serif;
  font-size: 2vh;
  color: #e8e5ae;
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
