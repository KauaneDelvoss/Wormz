<template>
  <div class="bookshelf-view">
    <v-row class="justify-center mt-8 margin-left-page">
      <ImgBookshelf :books="bookshelf.books" />

      <div class="d-flex flex-column">
        <div class="h3">{{ bookshelf.name }}</div>
        <div class="subtitulo">{{ bookshelf.description }}</div>
      </div>
    </v-row>
    <v-row class="d-flex justify-center row mt-8">
      <div
        v-for="book in this.bookshelf.books"
        :key="book.id"
        class="my-2 mx-5"
      >
        <CardBooks :book="book" />
      </div>
    </v-row>
  </div>
</template>

<script>
import { mapState } from "vuex";

export default {
  layout: "bib",
  data() {
    return {
      id: 0,
    };
  },
  mounted() {
    this.$store.dispatch("bib/GET_URL");
    this.id = this.$router.currentRoute.params.id;

    console.log(this.bookshelf);
  },
  computed: {
    ...mapState("bib", ["bookshelf"]),
  },
};
</script>

<style scoped lang="scss">
.bookshelf-view{
  min-height: 100vh;
  margin-top: $header-height;
}

</style>
