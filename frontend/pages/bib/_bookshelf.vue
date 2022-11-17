<template>
  <div v-if="bookshelf" class="bookshelf-view">
    <v-row class="justify-start my-12 mx-5 align-center">
      <!-- <ImgBookshelf :books="(this.bookshelf.books).slice(0, 4)" /> -->

      <div class="d-flex flex-column ms-5">
        <div class="h3">{{ bookshelf.bookshelf_info.bookshelf_name }}</div>
        <div class="subtitulo">{{ bookshelf.bookshelf_info.bookshelf_desc }}</div>
      </div>
    </v-row>

    <v-row class="d-flex justify-center row mt-8" v-if="this.bookshelf.book">
      <!-- <div
        v-for="book in this.bookshelf.book"
        :key="book.id"
        class="my-2 mx-5"
      >
        <CardBooks :book="book" />
      </div> -->
      <CardBooks :book="this.bookshelf.book" />
    </v-row>

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
    this.GET_BOOKSHELF({ user: this.user.username, id: this.id })
    console.log(this.bookshelf)
  },
  methods: {
    ...mapActions('bookshelf', ["GET_BOOKSHELF"])
  },
  computed: {
    ...mapState("bookshelf", ["bookshelf"]),
    ...mapState("auth", ["user"])
  },
};
</script>

<style scoped lang="scss">
.bookshelf-view{
  min-height: 100vh;
  margin-top: $header-height;
}

</style>
