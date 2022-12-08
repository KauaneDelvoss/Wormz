<template>
  <div class="second-slider">
    <div class="box-input d-flex flex-column align-center" style="gap:3vh;">
          <v-text-field
            style="width: 70%;"
            dark
            color="#E8E5AE"
            v-model=resultSecondForm.first_name
            label="Nome"
          ></v-text-field>
          <v-text-field
            style="width: 70%;"
            dark
            color="#E8E5AE"
            v-model=resultSecondForm.last_name
            label="Sobrenome"
          ></v-text-field>
          <v-textarea
            name="Biografia"
            label="Biografia"
            auto-grow
            v-model="resultSecondForm.user_biography"
            value=""
            style="width: 70%;"
            dark
            color="#E8E5AE"
          ></v-textarea>
              <v-row style="gap: 2vw">
                <button type="button" class="btnWormz" @click="$emit('goBack')">VOLTAR</button>
                <button type="button" class="btnWormz" @click="$emit('resultSecondForm', resultSecondForm)">CONCLUIR</button>
              </v-row>
          </div>
  </div>
</template>

<script>
export default {
 data(){
  return{
    resultSecondForm: {}
  }
 }
}
</script>

<style>

</style>