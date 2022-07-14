<template>
  <div class="title-wormz">
      <v-row align-content="center">

        <v-col cols="5" class="ms-md-12 d-flex justify-center">
            <div class="d-flex flex-column ">
                <div class="h1">Wormz</div>
                <v-divider id="divider" color="#E8E5AE"></v-divider>
                <div class="subtitulo mt-12 text-center">Quer descubrir sua próxima leitura? </div>
                <slot></slot>
                
            </div>
        </v-col>
      </v-row>
  </div>
</template>

<script>
export default {
}
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Alegreya+Sans+SC:wght@300&family=Encode+Sans&family=Libre+Baskerville&display=swap");

.h1{
    font-family: "Libre Baskerville", serif;
  font-size: 13vh;
  text-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  color: #e8e5ae;
}

.subtitulo{
  font-family: "Encode Sans", sans-serif;
  font-size: 2vh;
  color: #e8e5ae;

}

</style>