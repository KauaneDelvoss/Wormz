<template>
  <div class="review-action">
    <v-card
      outlined
      min-height="15vh"
      width="50vw"
      class="card-container d-flex justify-center align-center"
    >
      <div
        class="
          d-flex
          flex-column flex-grow-1
          margin-left-page margin-right-page
          flex-column
          my-5
        "
      >
        <div class="box d-flex">
          <div class="subtitulo mt-3">Avalie este livro:</div>
          <v-rating
            class="rating my-2 ms-2"
            empty-icon="mdi-star-outline"
            full-icon="mdi-star"
            half-icon="mdi-star-half-full"
            half-increments
            length="5"
            size="20"
            :value="2.5"
          ></v-rating>
        </div>
        <v-textarea
          style="width: 70%"
          color="#E8E5AE"
          background-color="#E8E5AE"
          v-model="review.text"
          label="Review"
          rows="3"
          solo
        ></v-textarea>
        <div>
          <button class="btnWormz mb-3" type="button">SUBMETER</button>
        </div>
      </div>
    </v-card>
  </div>
</template>

<script>
export default {
  data() {
    return {
      review: {},
    };
  },
};
</script>

<style scoped lang="scss">
.card-container {
  background-color: transparent !important;
  border-color: $primary-color !important;
}
</style>
