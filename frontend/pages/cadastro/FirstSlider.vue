<template>
  <div class="box-input d-flex flex-column align-center" style="gap:3vh;">
          <v-text-field
            style="width: 70%;"
            dark
            color="#E8E5AE"
            v-model=userEmail
            label="E-mail"
          ></v-text-field>
         <v-text-field
            style="width: 70%;"
            dark
            color="#E8E5AE"
            v-model="userPassword"
            label="Senha"
            :type="show ? 'text' : 'password'"
            :append-icon="show ? 'mdi-eye-off' : 'mdi-eye'"
            @click:append="show = !show"
          ></v-text-field>
         <v-text-field
            style="width: 70%;"
            dark
            color="#E8E5AE"
            v-model="passwordConfirmation"
            label="Senha"
            :type="showConfirmation ? 'text' : 'password'"
            :append-icon="showConfirmation ? 'mdi-eye-off' : 'mdi-eye'"
            @click:append="showConfirmation = !showConfirmation"
          ></v-text-field>
          <slot></slot>
        </div>
         
</template>

<script>
export default {
    data(){
      return{
        userEmail: '',
        userPassword: '',
        passwordConfirmation: '',
        show: false,
        showConfirmation: false,
      }
    },
}
</script>

<style scoped>
</style>