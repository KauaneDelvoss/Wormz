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
            <div v-for="bookshelf in bookshelves" :key="bookshelf.name" class="my-n2">
                <v-checkbox dark v-model="checkboxActive" :label="bookshelf.name" :value="bookshelf.name" class="subtitulo"/>
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
            @click="$emit('closeDialog')"
          >
            ADICIONAR
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>

<script>

export default {
    props: { dialog:Boolean },
    data(){
        return{
            checkboxActive: [],
            bookshelves: [
                { id: 1, name: 'Primeira' },
                { id: 1, name: 'Segunda' },
                { id: 2, name: 'Terceira' }
            ]
        }
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