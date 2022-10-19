<template>
  <div class="teste">
    {{ this.api_key }} <br />
    {{ this.url }} <br />
    {{ this.url_search }} <br />

    <!-- livros.volumeInfo.imageLinks.thumbnail !-->
    <div v-for="(item, index) in books" :key="index">
      <v-img
        v-if="
          (item.volumeInfo.imageLinks
            ? item.volumeInfo.imageLinks.thumbnail
            : false) != false
        "
        :src="item.volumeInfo.imageLinks.thumbnail"
        max-width="200px"
      ></v-img>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";
export default {
  data() {
    return {
      livros: {},
      loadState: false,
    };
  },
  mounted() {
    this.$store.commit(
      "google_books/MAKE_URL_SEARCH",
      "O Retrato de Dorian Gray"
    );
    this.$store.dispatch("google_books/GET_URL");
    console.log(this.books[0])
  },
  computed: {
    ...mapState("google_books", ["books"]),
  },
};
</script>

<style>
</style>