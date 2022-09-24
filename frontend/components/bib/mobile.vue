<template>
  <div class="bib-view-mobile">
    <v-row class="mobile-profile mt-5">
      <v-col class="ms-md-12 d-flex flex-column align-center col-default">
        <div class="d-flex flex-column">
          <div class="h1 mb-n2">Wormz</div>
          <v-divider id="divider" color="#E8E5AE"></v-divider>
          <div class="subtitulo mt-4 text-center">
            Procure na sua biblioteca:
          </div>
        </div>
      </v-col>
    </v-row>
    <div class="form-container d-flex flex-column align-center mt-4">
      <input
        type="text"
        name="form-container"
        placeholder="Blade Runner..."
        id="form-area"
        v-model="searchField"
        @keyup="search(searchField)"
      />
      <v-icon
        style="width: 100%; left: 15vw"
        class="flex-column align-start my-2"
        color="#e8e5ae"
        >mdi-filter-menu</v-icon
      >
    </div>

    <div class="margin-left-page margin-right-page">
      <div class="margin-left-page margin-right-page static-data">
        <div class="h3 mt-10 mb-2">
          Destaques:
            <v-card class="card mt-2" width="36vw" height="28vh">
                <div style="height: 100%" class="icon d-flex align-center justify-center">
                    <v-icon large>mdi-plus</v-icon>
                </div>
            </v-card>
          <p class="subtitulo-minimo">carrosel</p>
        </div>
      </div>
    </div>
    <div class="margin-left-page margin-right-page">
      <div class="margin-left-page margin-right-page static-data">
        <div class="h3 mt-10 mb-2">
          Matches:
          <v-card class="card mt-2" width="36vw" height="28vh">
                <div style="height: 100%" class="icon d-flex align-center justify-center">
                    <v-icon large>mdi-plus</v-icon>
                </div>
            </v-card>
          <p class="subtitulo-minimo">carrosel</p>
        </div>
      </div>
    </div>
    <div class="margin-left-page margin-right-page">
      <div class="margin-left-page margin-right-page static-data">
        <div class="h3 mt-10 mb-2">
          Estantes:
          <v-card class="card mt-2" width="36vw" height="28vh">
                <div style="height: 100%" class="icon d-flex align-center justify-center">
                    <v-icon large>mdi-plus</v-icon>
                </div>
            </v-card>
          <p class="subtitulo-minimo">carrosel</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      searchField: "",
    };
  },
};
</script>

<style scoped lang="scss">
.bib-view-mobile {
  background-image: linear-gradient(45deg, $bg-color, $secondary-color);
  min-height: 100vh;
  overflow: hidden;
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

.card{
    border-radius: 15px;
    background-color: $primary-color;
}
</style>