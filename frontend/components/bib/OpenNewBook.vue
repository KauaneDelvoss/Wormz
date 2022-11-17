<template>
  <div class="open-new-book">
    <v-dialog
      transition="dialog-bottom-transition"
      v-model="dialog"
      class="dialog"
      persistent
      max-width="55vw"
    >
      <v-card class="card-container d-flex flex-column">
        <v-card-title v-if="bookshelf.bookshelf_name" class="d-flex justify-center">
          <span class="h3 mt-5 align-self-center">{{ bookshelf.bookshelf_name }}</span>
        </v-card-title>
        <v-card-title v-else class="d-flex justify-center">
          <span class="h3 mt-5 align-self-center">Nova Estante</span>
        </v-card-title>
        <v-divider class="divider mx-2" />
        <v-card-text>
          <v-container class="container py-5 px-5">
            <div class="name-form mt-5">
                <div class="subtitulo"> Dê um nome à sua estante: </div>
                <input
                type="text"
                name="form-container"
                placeholder="Nova Estante"
                class="form-area py-2"
                v-model="bookshelf.bookshelf_name"
            />
            </div>
            <div class="description-form mt-5">
                <div class="subtitulo"> Descrição: </div>
                <textarea
                type="text"
                name="form-container"
                placeholder="Lista de Desejos"
                class="form-area py-2"
                v-model="bookshelf.bookshelf_desc"
                max-lenght="150"
            />
            </div>
          </v-container>
        </v-card-text>
        <v-card-actions>
            <v-btn
            class="dropdown-item"
            text
            color="white"
            @click="$emit('close')"
          >
            Cancelar
          </v-btn>
          <v-spacer></v-spacer>
          <v-btn
            class="dropdown-item"
            text
            color="white"
            @click="($emit('close'), bookshelf.user = user, ADD_BOOKSHELF(bookshelf)), bookshelf = {}"
          >
            Criar
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex';

export default {
    props: { dialog:Boolean },
    data(){
        return{
            bookshelf : {}
        }
    },
    methods:{
      ...mapActions('bookshelf', ['ADD_BOOKSHELF'])
    },
    computed: {
      ...mapState('auth', ['user'])
    }
}
</script>

<style scoped lang="scss">
.card-container {
  background-color: $bg-color !important;
}

.divider{
    border-color: $primary-color !important;
}

.form-area {
    height: 3vh;
    margin-top: 10px;
    margin-bottom: 10px;
    background-color: transparent;
    border-bottom: 1px solid $primary-color;
    padding-left: 2vw;
    width: 70%;
    color: $primary-color;
  }

</style>
