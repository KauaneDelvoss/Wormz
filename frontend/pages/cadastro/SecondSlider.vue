<template>
  <div class="second-slider">
    <div class="box-input d-flex flex-column align-center" style="gap:3vh;">
          <v-text-field
            style="width: 70%;"
            dark
            color="#E8E5AE"
            v-model=userName
            label="Nome"
          ></v-text-field>
         <v-text-field
            style="width: 70%;"
            dark
            color="#E8E5AE"
            v-model=userNickname
            label="Apelido (user)"
          ></v-text-field>
          <slot></slot>
          </div>
  </div>
</template>

<script>
export default {
 data(){
  return{
    userName: "",
    userNickname: "",
  }
 }
}
</script>

<style>

</style>