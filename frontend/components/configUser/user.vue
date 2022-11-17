<template>
  <div class="py-3">
    <div class="subtitulo hide-mobile-l">Alterar informações:</div>
    <form @submit.prevent class="row-wrapper">
      <div class="box-config-user d-flex flex-row align-center">
        <div class="header-title me-3">Foto:</div>
        <v-file-input
          label="Foto"
          prepend-icon="mdi-camera"
          dark
          class="photo-input"
        ></v-file-input>
      </div>
    </form>
    <form @submit.prevent class="row-wrapper">
      <div class="box-config-user d-flex flex-row align-center">
        <div class="header-title me-3">Nickname:</div>
        <v-text-field value="" class="text-field" v-model="userLocal.username" dark></v-text-field>
      </div>
      <div class="box-config-user d-flex flex-row align-center">
        <div class="header-title me-3">Nome:</div>
        <v-text-field value="" class="text-field" v-model="userLocal.first_name" dark></v-text-field>
      </div>
      <div class="box-config-user d-flex flex-row align-center">
        <div class="header-title me-3">Sobrenome:</div>
        <v-text-field value="" class="text-field" v-model="userLocal.last_name" dark></v-text-field>
      </div>
      <div class="box-config-user d-flex flex-row align-center">
        <div class="header-title me-3">E-mail:</div>
        <v-text-field value="" class="text-field" v-model="userLocal.email" dark></v-text-field>
      </div>
      <!--
      <div class="box-config-user d-flex flex-row align-center">
        <div class="header-title me-3">Senha:</div>
        <v-text-field value="" class="text-field" v-model="userLocal.password" dark></v-text-field>
      </div>
      !-->
    </form>

    <form @submit.prevent class="row-wrapper">
      <div class="box-config-user d-flex flex-row align-center">
        <div class="header-title me-3">Biografia:</div>
        <v-textarea
            name="Biografia"
            class="text-field"
            auto-grow
            v-model="userLocal.user_biography"
            value=""
            style="width: 70%;"
            dark
            color="#E8E5AE"
          ></v-textarea>
      </div>
    </form>

    <form @submit.prevent class="row-wrapper">
      <div class="box-config-user d-flex flex-row align-center">
        <div class="header-title me-3">País:</div>
        <v-text-field value="Lugar nenhum" class="text-field" dark></v-text-field>
      </div>
      <div class="box-config-user d-flex flex-row align-center">
        <div class="header-title me-3">Estado:</div>
        <v-text-field value="Lugar nenhum" class="text-field" dark></v-text-field>
      </div>
      <div class="box-config-user d-flex flex-row align-center">
        <div class="header-title me-3">Cidade:</div>
        <v-text-field value="Lugar nenhum" class="text-field" dark></v-text-field>
      </div>
    </form>
    <v-row class="box-config-user d-flex flex-row justify-end me-3">
      <button class="btnWormz special mt-5 ms-3" type="button" @click="deleteUser(), $emit('fechar')">DELETAR PERFIL</button>
    </v-row>
    <div class="button d-flex flex-row align-center justify-end me-3 mt-10">
      <button class="btnWormz ms-3" type="button" @click="submitAuthData">SALVAR</button>
    </div>
  </div>
</template>

<script>
import {mapState, mapActions} from 'vuex'
export default {
  data(){
    return{
      userLocal: {}
    }
  },
  // created(){
  //   this.userLocal = this.user
  // },
  methods:{
    ...mapActions('auth', ['LOGOUT', 'UPDATE_USER', 'DELETE_USER']),
    submitAuthData(){
      this.userLocal.id = this.user.id
      this.UPDATE_USER(this.userLocal)
    },

    deleteUser(){
      this.DELETE_USER({'id': this.userLocal.id})
    }
  },
  computed: {
    ...mapState('auth', ['user'])
  }
};
</script>

<style lang="scss" scoped>
@include breakpoints;

@media (max-width: $phone_l) {
  .box-config-user{
    flex-direction: column !important;
    align-content: flex-end !important;
    margin-right: $distance-margin;
  }

  .header-title{
    margin-left: 0 !important;
    align-self: flex-start  !important;
  }

  .photo-input{
    width: 100%;
  }
}

.row-wrapper {
  background: rgba(232, 229, 174, 0.2);
  padding: 20px;
  margin: 20px;
  border-radius: 20px;
}
.special{
  background-color: red !important;
  color: white !important;
}
.text-field{
  font-size: 2vh;
}
</style>
