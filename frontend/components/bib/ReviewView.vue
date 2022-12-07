<template>
  <div class="review-view">
    <div v-for="review in reviews" class="mt-3" :key="review.id">
      <div class="review-card py-2">
        <v-row class="justify-space-between">
          <span class="subtitulo mt-3">
            {{ review.user.username }}
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

        <div class="subtitulo reading-text mt-3"> {{ review.comment }} </div>
      </div>

      <v-divider class="divider" />
    </div>
  </div>
</template>

<script>
export default {
  props: ["reviews"],
  mounted(){
    console.log(this.reviews)
  }
}
</script>

<style scoped lang="scss">
.review-view{
  width: 50vw
}

</style>
