<template>
  <div class="review-view">
    <div v-for="review in reviews" class="mt-3" :key="review.id">
      <div class="review-card py-2">
        <v-row class="justify-space-between">
          <span class="subtitulo mt-3">
            Em {{ review.book }}
          </span>
          <v-rating
            class="rating"
            empty-icon="mdi-star-outline"
            full-icon="mdi-star"
            half-icon="mdi-star-half-full"
            half-increments
            length="5"
            readonly
            size="20"
            :value="review.stars"
          ></v-rating>
        </v-row>

        <div class="subtitulo reading-text mt-3">{{ review.description }}</div>
      </div>

      <v-divider class="divider" />
    </div>
  </div>
</template>

<script>
export default {
  props: ["user"],
  data() {
    return {
      reviews: [
        {
          id: 0,
          stars: 4.5,
          book: "Kafka à beira mar",
          description: "muito bom muito bom"
        },
        {
          id: 1,
          stars: 3.5,
          book: "O estrangeiro",
          description: "me fez pensar bastante"
        },
        {
          id: 2,
          stars: 4.0,
          book: "Sagarana",
          description: "um dos melhores que li este ano",
        },
      ],
    };
  },
};
</script>

<style scoped lang="scss">
.review-view {
  width: 50vw;
}
</style>
