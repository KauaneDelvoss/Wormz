<template>
  <ImgBackground>
    <div class="question-quizz d-flex align-center justify-center">
      <div class="d-flex flex-column">
        <v-row class="justify-space-between mb-5">
          <v-icon large class="v-icon-item">mdi-arrow-left</v-icon>
          <div class="h3">Questão {{ question_id }} de 10</div>
          <v-icon large class="v-icon-item">mdi-arrow-right</v-icon>
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
            <div class="subtitulo reading-text">{{ snip }}</div>
            <div class="subtitulo little justify-self-end">
              {{ book }} - {{ author }}
            </div>
          </div>
          <div class="d-flex justify-space-around" style="width: 100%">
            <div class="radio-box d-flex align-center flex-column">
              <div class="subtitulo mb-2">Não gostei</div>
              <v-icon
                small
                class="v-icon-item"
                v-if="selected == 1"
                @click="selected = 1"
                >mdi-circle-slice-8</v-icon
              >
              <v-icon small class="v-icon-item" v-else @click="selected = 1"
                >mdi-circle-outline</v-icon
              >
            </div>
            <div class="radio-box d-flex align-center flex-column">
              <div class="subtitulo mb-2">Não tenho certeza</div>
              <v-icon
                small
                class="v-icon-item"
                v-if="selected == 2"
                @click="selected = 2"
                >mdi-circle-slice-8</v-icon
              >
              <v-icon small class="v-icon-item" v-else @click="selected = 2"
                >mdi-circle-outline</v-icon
              >
            </div>
            <div class="radio-box d-flex align-center flex-column">
              <div class="subtitulo mb-2">Gostei!</div>
              <v-icon
                small
                class="v-icon-item"
                v-if="selected == 3"
                @click="selected = 3"
                >mdi-circle-slice-8</v-icon
              >
              <v-icon small class="v-icon-item" v-else @click="selected = 3"
                >mdi-circle-outline</v-icon
              >
            </div>
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
      id: "",
      question_id: 1,
      snip: "Aqui vai o texto",
      book: "Um título",
      author: "Um autor",
      selected: 0,
    };
  },
  mounted() {
    this.id = this.$router.currentRoute.params.id;
  },
};
</script>

<style scoped lang="scss">
.question-quizz {
  height: 100vh;
}

.card {
  height: 50vh;
  width: 50vw;
  background-color: $bg-color;
  border-radius: 20px;
  border: 1px solid $primary-color;
}
</style>