<template>
  <div class="login-wormz">
    <v-row class="d-fluid flex-row">
      <v-col cols="6" class="m-5 d-flex flex-column">
        <div class="box-input d-flex flex-column align-center">
          <v-text-field
            style="width: 80%"
            v-model="inputEmail"
            label="E-mail"
          ></v-text-field>
          <v-text-field
            style="width: 80%"
            v-model="inputSenha"
            label="Senha"
          ></v-text-field>
          <v-text-field
            style="width: 80%"
            v-model="inputConfirmarSenha"
            label="Confirme a Senha"
          ></v-text-field>
        </div>
      </v-col>
      <v-col cols="6 m-5 mb-6 d-flex flex-column">
        <div class="box-title d-flex flex-column align-end">
          <titleWormz class="title-wormz"></titleWormz>
        </div>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import titleWormz from "../components/titleWormz.vue";
export default {
  name: "HomeWormz",
  components: { titleWormz },
  methods: {},
};
</script>

<style scoped>
.login-wormz {
  height: 100vh;
  width: 100vw;
  background-color: #22273c;
  background-image: url("../assets/blobblue.png");
  background-position: right;
  background-repeat: no-repeat;
  background-size: 100vh;
}

.title-wormz {
  transform: scale(0.7);
}

.box-title {
  position: absolute;
  bottom: 0;
  right: 0;
}
</style>