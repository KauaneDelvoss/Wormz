<template>
  <div class="open-new-book">
    <v-dialog
      transition="dialog-bottom-transition"
      v-model="dialog"
      class="dialog"
      persistent
      max-width="55vw"
    >
      <template v-slot:activator="{ on, attrs }">
        <div
          class="
            mb-3
            d-flex
            dropdown-item
            flex-row
            align-center
            header-title
            justify-between
          "
          v-on="on"
          v-bind="attrs"
        >
          CONFIGURAÇÕES
          <v-icon small class="v-icon-item ms-2">mdi-nut</v-icon>
        </div>
      </template>
      <v-card class="card-container d-flex flex-column">
        <v-card-title>
          <span class="h3 mt-5 align-self-center">{{ bookshelf_name }}</span>
        </v-card-title>
        <v-divider class="divider mx-2" />
        <v-card-text>
          <v-container class="container py-5 px-5">
            <div class="name-form mt-5">
                <div class="subtitulo"> Dê um nome à sua estante: </div>
                <input
                type="text"
                name="form-container"
                placeholder="Lista de Desejos"
                id="form-area"
                v-model="bookshelf_name"
            />
            </div>
            <div class="description-form mt-5">
                <div class="subtitulo"> Descrição: </div>
                <textarea
                type="text"
                name="form-container"
                placeholder="Lista de Desejos"
                id="form-area"
                v-model="bookshelf_description"
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
            @click="$emit('close')"
          >
            Criar
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
export default {
    props: { dialog:Boolean },
    data(){
        return{
            bookshelf_name: 'Nova Estante',
            bookshelf_description: 'Tudo que desejo ler este ano...'
        }
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

#form-area {
    height: 3vh;
    margin-top: 10px;
    margin-bottom: 10px;
    background-color: rgb(232, 229, 174, 0.64);
    border-radius: 20px;
    padding-left: 2vw;
    width: 70%;
  }

</style>