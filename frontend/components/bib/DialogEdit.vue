<template>
  <v-row justify="center">
    <v-dialog
      transition="dialog-bottom-transition"
      v-model="dialog"
      scrollable
      max-width="55vw"
    >
      <v-card class="card-container">
        <v-card-title class="h3">Editar estante:</v-card-title>
        <v-divider class="divider"></v-divider>
        <v-container class="container px-5">
            <div class="name-form">
                <div class="subtitulo"> Nome: </div>
                <input
                type="text"
                name="form-container"
                placeholder="Nova Estante"
                class="form-area py-2 white--text"
                v-model="bookshelf_local.bookshelf_name"
            />
            </div>
            <div class="description-form mt-5">
                <div class="subtitulo"> Descrição: </div>
                <textarea
                type="text"
                name="form-container"
                placeholder="Lista de Desejos"
                class="form-area py-2 white--text"
                v-model="bookshelf_local.bookshelf_desc"
                max-lenght="150"
            />
            </div>
          </v-container>
        <v-card-actions>
          <v-btn class="button white--text" text @click="($emit('closeDialog'), bookshelf_local = {})">
            CANCELAR
          </v-btn>
          <v-spacer></v-spacer>
          <v-btn class="button white--text" text @click="($emit('closeDialog'), editBookshelf(), bookshelf_local = {})">
            CONFIRMAR
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>

<script>
export default {
  props: ["dialog", "bookshelf"],
  data(){
    return{
        bookshelf_local: {}
    }
  },
  mounted(){
    this.bookshelf_local.id = this.bookshelf.id
    console.log(this.bookshelf)
  },
  methods:{
    editBookshelf(){
        this.$axios.post('post/editBookshelf', JSON.stringify(this.bookshelf_local), {headers: {'Content-Type': 'application/json'}}).then(
            response => {
                console.log(response.data)
            }
        )
    }
  }
};
</script>

<style scoped lang="scss">
.card-container {
  background-color: $bg-color !important;
}
</style>