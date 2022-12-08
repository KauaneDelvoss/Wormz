<template>
  <ImgBackground>
    <div class="quizz-default d-flex align-center justify-center">
      <div class="card d-flex align-center justify-center flex-column">
        <div class="h3">Vai uma indicação aí?</div>
        <div class="h1">Quizz</div>
        <button type="button" class="btnWormz mt-5" @click="newQuizz()">COMEÇAR</button>
      </div>
    </div>
  </ImgBackground>
</template>

<script>
import ImgBackground from "~/components/basic/ImgBackground";

export default {
  middleware: 'auth',
  components: { ImgBackground },
  methods: {
    newQuizz(){
      this.$router.push({
        path: '/quizz/1'
      })
    }
  }
};
</script>

<style scoped lang="scss">
@media (max-width: $phone_l) {
  .card{
    width: 90vw !important;
  }
}

.quizz-default {
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