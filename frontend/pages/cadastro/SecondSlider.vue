<template>
  <div class="second-slider">
    <div class="box-input d-flex flex-column align-center" style="gap:3vh;">
         <v-text-field
            style="width: 70%;"
            dark
            color="#E8E5AE"
            v-model=userNickname
            label="Apelido (user)"
          ></v-text-field>
          <v-textarea
            name="Biografia"
            label="Biografia"
            auto-grow
            v-model="userBio"
            value=""
            style="width: 70%;"
            dark
            color="#E8E5AE"
          ></v-textarea>
          <slot></slot>
          </div>
  </div>
</template>

<script>
export default {
 data(){
  return{
    userBio: "",
    userNickname: "",
  }
 }
}
</script>

<style>

</style>