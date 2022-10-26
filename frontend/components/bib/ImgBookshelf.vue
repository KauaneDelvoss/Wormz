<template>
  <div class="img-bookshelf d-flex flex-wrap">
    <!-- <v-img class="img" :src="books[0].volumeInfo.imageLinks.thumbnail"></v-img>
    <v-img class="img" :src="books[1].volumeInfo.imageLinks.thumbnail"></v-img>
    <v-img class="img" :src="books[2].volumeInfo.imageLinks.thumbnail"></v-img>
    <v-img class="img" :src="books[3].volumeInfo.imageLinks.thumbnail"></v-img> -->
  </div>
</template>

<script>
export default {
    props: ["books"],
    mounted() {
      console.log(this.books)
    }
}
</script>

<style scoped lang="scss">

.img-bookshelf{
    height: 20vh;
    width: 20vh;
    background-color: $primary-color;
}

</style>