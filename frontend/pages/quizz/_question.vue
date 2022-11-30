<template>
  <ImgBackground>
    <div class="question-quizz d-flex align-center justify-center">
      <div class="d-flex flex-column">
        <v-row class="justify-space-between mb-5">
          <v-icon large class="v-icon-item">mdi-arrow-left</v-icon>
          <div class="h3">Questão {{ question_id }} de 10</div>
          <v-icon v-if="question_id != 10" large class="v-icon-item">mdi-arrow-right</v-icon>
          <v-icon v-else large class="v-icon-item">mdi-check-bold</v-icon>
        </v-row>
        <div
          class="
            card
            d-flex
            align-center
            justify-space-between
            flex-column
            py-10
          "
        >
          <div class="d-flex flex-column">
            <div class="subtitulo reading-text">{{ pergunta_um.snip }}</div>
            <div class="subtitulo little justify-self-end">
              {{ book }} - {{ author }}
            </div>
          </div>
          <div v-for="radio in pergunta_um.radios" :key="radio.id" class="justify-content">


            <div class="radio-box d-flex  flex-row">
              <v-icon
              small
              class="v-icon-item"
              v-if="pergunta_um.selected == radio.id"
              @click="pergunta_um.selected = radio.id"
              >mdi-circle-slice-8</v-icon
              >
              <v-icon small class="v-icon-item" v-else @click="pergunta_um.selected = radio.id"
              >mdi-circle-outline</v-icon
              >
              <div class="subtitulo mb-2"
               >{{radio.subtitle}}</div>
            </div>

          </div >
          <div>
              informações: {{pergunta_um}}
          </div>

        </div>
      </div>
    </div>
  </ImgBackground>
</template>

<script>
import ImgBackground from "~/components/basic/ImgBackground";

export default {
  components: { ImgBackground },
  data() {
    return {

      pergunta_um: {
        id : 1,
        snip: "Quantas páginas você gostaria de ler?",
        selected: "",
        radios : [
        {
        id: 1,
        subtitle: "30 páginas"
        },
        {
        id: 2,
        subtitle: "100 páginas"
        },
        {
        id: 3,
        subtitle: "300 páginas"
        }, ],

      },
      question_id: 1,



      book: "Um título",
      author: "Um autor",
      // Não vamos conseguir usar autor e livro, serão perguntas técnicas
    };
  },
  mounted() {
    this.id = this.$router.currentRoute.params.id;
  },
};
</script>

<style scoped lang="scss">
@media (max-width: $phone_l) {
  .card{
    width: 90vw !important;
  }
}


.question-quizz {
  height: 100vh;
}

.card {
  height: 50vh;
  width: 50vw;
  background-color: $bg-color !important;
  border-radius: 20px;
  border: 1px solid $primary-color;
}
</style>
