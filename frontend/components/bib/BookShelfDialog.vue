<template>
  <v-row justify="center">
    <v-dialog
      v-model="dialog"
      scrollable
      max-width="300px"
    >
      <v-card class="card-container">
        <v-card-title class="h3">Adicionar à estante</v-card-title>
        <v-divider class="divider"></v-divider>
        <v-card-text style="height: 300px;" class="mt-5">
          <div class="checkboxes">
            <div v-for="bookshelf in bookshelves" :key="bookshelf.id" class="my-n2">
                <v-checkbox dark v-model="checkboxActive" :label="bookshelf.bookshelf_name" :value="bookshelf" class="subtitulo"/>
            </div>
          </div>
        </v-card-text>
        <v-divider class="divider"></v-divider>
        <v-card-actions>
          <v-btn
            class="button"
            text
            @click="$emit('closeDialog')"
          >
            CANCELAR
          </v-btn>
          <v-spacer></v-spacer>
          <v-btn
            class="button"
            text
            @click="($emit('closeDialog'), ADD_TO_BOOKSHELF({bookshelves: checkboxActive, id_book: book}))"
          >
            ADICIONAR
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>

<script>
import { mapActions, mapState } from 'vuex'

export default {
    props: { dialog: Boolean, book: Number },
    data(){
        return{
            checkboxActive: [],
        }
    },
    mounted(){
      this.GET_BOOKSHELVES(this.user.username)
      console.log(this.book)
    },
  methods:{
    ...mapActions('bookshelf', ["GET_BOOKSHELVES", "ADD_TO_BOOKSHELF"])
  },
  computed: {
    ...mapState('bookshelf', ["bookshelf", "bookshelves"]),
    ...mapState('auth', ["user"])
  }
}
</script>

<style scoped lang="scss">
.card-container{
    background-color: $bg-color !important;
}

.divider{
    border-color: $primary-color !important;
}

.button{
    color: $primary-color !important
}

</style>