<template>
  <div>
    <div class="subtitulo">Alterar informações:</div>
    <form @submit.prevent class="row-wrapper">
      <div class="box-config-user d-flex flex-row align-center">
        <div class="header-title me-3">Foto:</div>
        <v-file-input
          label="Foto"
          prepend-icon="mdi-camera"
          dark
        ></v-file-input>
      </div>
    </form>
    <form @submit.prevent class="row-wrapper">
      <div class="box-config-user d-flex flex-row align-center">
        <div class="header-title me-3">Nickname:</div>
        <v-text-field value="" v-model="userLocal.username" dark></v-text-field>
      </div>
      <div class="box-config-user d-flex flex-row align-center">
        <div class="header-title me-3">Nome:</div>
        <v-text-field value="" v-model="userLocal.first_name" dark></v-text-field>
      </div>
      <div class="box-config-user d-flex flex-row align-center">
        <div class="header-title me-3">Sobrenome:</div>
        <v-text-field value="" v-model="userLocal.last_name" dark></v-text-field>
      </div>
      <div class="box-config-user d-flex flex-row align-center">
        <div class="header-title me-3">E-mail:</div>
        <v-text-field value="" v-model="userLocal.email" dark></v-text-field>
      </div>
      <!--
      <div class="box-config-user d-flex flex-row align-center">
        <div class="header-title me-3">Senha:</div>
        <v-text-field value="" v-model="userLocal.password" dark></v-text-field>
      </div>
      !-->
    </form>

    <form @submit.prevent class="row-wrapper">
      <div class="box-config-user d-flex flex-row align-center">
        <div class="header-title me-3">Biografia:</div>
        <v-textarea
            name="Biografia"
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
        <v-text-field value="Lugar nenhum" dark></v-text-field>
      </div>
      <div class="box-config-user d-flex flex-row align-center">
        <div class="header-title me-3">Estado:</div>
        <v-text-field value="Lugar nenhum" dark></v-text-field>
      </div>
      <div class="box-config-user d-flex flex-row align-center">
        <div class="header-title me-3">Cidade:</div>
        <v-text-field value="Lugar nenhum" dark></v-text-field>
      </div>
    </form>
    <div class="button d-flex flex-row align-center justify-end me-3">
      <button class="btnWormz ms-3" type="button" @click="submitAuthData">SALVAR</button>
    </div>
    <div class="box-config-user d-flex flex-row align-center">
      <div class="header-title ms-3">Deletar Perfil</div>
      <button class="btnWormz special mt-5 ms-3" type="button" @click="deleteUser">DELETAR</button>
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
  mounted(){
    this.userLocal.id = this.user.id
  },
  methods:{
    ...mapActions('auth', ['LOGOUT']),
    submitAuthData(){
      const getFormData = object => Object.keys(object).reduce((formData, key) => {
                formData.append(key, object[key]);
                return formData;
            }, new FormData());

      this.$axios.post('/update/user', getFormData(this.userLocal)).then(
        response => console.log(response)
      )
    },

    deleteUser(){
      const getFormData = object => Object.keys(object).reduce((formData, key) => {
                formData.append(key, object[key]);
                return formData;
            }, new FormData());
        
      this.$axios.post('/delete/user', getFormData({'id': this.userLocal.id})).then(
        response => {if(response.status==200){
          this.LOGOUT()
          this.$router.push({
            path: '/'
          })
        }}
      )
    }
  },
  computed: {
    ...mapState('auth', ['user'])
  }
};
</script>

<style lang="scss" scoped>
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
</style>