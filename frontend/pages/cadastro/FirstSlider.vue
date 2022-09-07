<template>
  <div class="box-input d-flex flex-column align-center" style="gap:3vh;">
          <v-text-field
            style="width: 70%;"
            dark
            color="#E8E5AE"
            v-model=resultFirstForm.username
            label="Nickname"
          ></v-text-field>
         <v-text-field
            style="width: 70%;"
            dark
            color="#E8E5AE"
            v-model="resultFirstForm.email"
            label="E-mail"
          ></v-text-field>
         <v-text-field
            style="width: 70%;"
            dark
            color="#E8E5AE"
            v-model="resultFirstForm.password"
            label="Senha"
            :type="show ? 'text' : 'password'"
            :append-icon="show ? 'mdi-eye-off' : 'mdi-eye'"
            @click:append="show = !show"
          ></v-text-field>
          <button type="button" class="btnWormz" @click="$emit('resultFirstForm', resultFirstForm)">PRÓXIMO</button>
        </div>
         
</template>

<script>
export default {
    data(){
      return{
        resultFirstForm: {},
        show: false,
        showConfirmation: false,
      }
    }
}
</script>

<style scoped>
</style>