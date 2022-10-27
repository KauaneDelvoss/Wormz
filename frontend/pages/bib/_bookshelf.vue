<template>
  <div v-if="this.bookshelf.books" class="bookshelf-view">
    <v-row class="justify-start my-12 mx-5 align-center">
      <!-- <ImgBookshelf :books="(this.bookshelf.books).slice(0, 4)" /> -->

      <div class="d-flex flex-column ms-5">
        <div class="h3">{{ bookshelf.bookshelf_name }}</div>
        <div class="subtitulo">{{ bookshelf_desc }}</div>
      </div>
    </v-row>
    <!-- <v-row class="d-flex justify-center row mt-8">
      <div
        v-for="book in this.bookshelf.books"
        :key="book.id"
        class="my-2 mx-5"
      >
        <CardBooks :book="book" />
      </div>
    </v-row> -->
  </div>
</template>

<script>
import { mapState, mapActions } from "vuex";
import ImgBookshelf from '~/components/bib/ImgBookshelf'

export default {
  layout: "bib",
  components: { ImgBookshelf },
  data() {
    return {
      id: 0,
    };
  },
  mounted() {
    this.id = this.$router.currentRoute.params.id;
    this.GET_BOOKSHELF(this.id)
  },
  methods: {
    ...mapActions('bookshelf', ["GET_BOOKSHELF"])
  },
  computed: {
    ...mapState("bookshelf", ["bookshelf"]),
  },
};
</script>

<style scoped lang="scss">
.bookshelf-view{
  min-height: 100vh;
  margin-top: $header-height;
}

</style>
