<template>
  <div v-if="bookshelf.bookshelf_info" class="bookshelf-view">
    <v-row class="justify-start my-12 mx-5 align-center justify-space-between">
      <!-- <ImgBookshelf :books="(this.bookshelf.books).slice(0, 4)" /> -->

      <div class="d-flex flex-column ms-5 mt-2">
        <div class="h3">{{ bookshelf.bookshelf_info.bookshelf_name }}</div>
        <div class="subtitulo">
          {{ bookshelf.bookshelf_info.bookshelf_desc }}
        </div>
      </div>

      <div class="d-flex me-5 mt-2 align-center">
        <v-icon class="icon v-icon-item me-4" @click="dialog = true"
          >mdi-playlist-edit</v-icon
        >
        <v-icon
          class="icon delete-button v-icon-item"
          @click="deleteBookshelf()"
          >mdi-trash-can-outline</v-icon
        >
      </div>
    </v-row>

    <v-row class="d-flex justify-center row mt-8" v-if="bookshelf.book">
      <div v-for="book in bookshelf.book" :key="book.id" class="my-2 mx-5">
        <CardBooks :book="book" />
      </div>
    </v-row>

    <DialogEdit
      :id="'c' + bookshelf.bookshelf_info.id"
      :dialog="dialog"
      :bookshelf="bookshelf.bookshelf_info"
      @closeDialog="
        (dialog = false),
          getBookshelf({ user: user.username, id: id }),
          GET_BOOKSHELVES(user.username)
      "
    />
  </div>
</template>

<script>
import { mapState, mapActions } from "vuex";
import ImgBookshelf from "~/components/bib/ImgBookshelf";
import DialogEdit from "~/components/bib/DialogEdit";

export default {
  layout: "bib",
  middleware: 'auth',
  components: { ImgBookshelf, DialogEdit },
  data() {
    return {
      id: 0,
      bookshelf: {},
      dialog: false,
    };
  },
  mounted() {
    this.id = this.$router.currentRoute.params.id;
    this.bookshelf = {};
    this.getBookshelf({ user: this.user.username, id: this.id });
  },
  methods: {
    ...mapActions("bookshelf", ["GET_BOOKSHELVES"]),
    getBookshelf(payload) {
      this.$axios
        .get("/get/" + payload.user + "/bookshelf/" + payload.id)
        .then((response) => {
          this.bookshelf = response.data;
        });
    },
    deleteBookshelf() {
      this.$axios.get("/delete/bookshelf/" + this.id).then((response) => {
        this.bookshelf = response.data;
        this.GET_BOOKSHELVES(this.user.username);
        this.$router.push({ path: "/userBib" });
      });
    },
  },
  computed: {
    ...mapState("auth", ["user"]),
  },
};
</script>

<style scoped lang="scss">
.bookshelf-view {
  min-height: 100vh;
  margin-top: $header-height;
}

.delete-button:hover {
  color: red !important;
  transition: 1.2s;
}

.icon {
  cursor: pointer;
}
</style>
