<template>
  <v-app class="login-wormz">
    <v-row class="app flex-row mt-5" style="height: 100vh">
      <v-col class="m-5 d-flex flex-column justify-center col-default">
        <div class="box-input d-flex flex-column align-center" style="gap: 3vh">
          <div class="titulo">Login</div>
          <v-text-field
            style="width: 70%"
            dark
            color="#E8E5AE"
            v-model="user.username"
            label="Nickname"
          ></v-text-field>
          <v-text-field
            style="width: 70%"
            dark
            color="#E8E5AE"
            v-model="user.password"
            label="Senha"
            :type="show ? 'text' : 'password'"
            :append-icon="show ? 'mdi-eye-off' : 'mdi-eye'"
            @click:append="show = !show"
          ></v-text-field>
          <div class="subtitulo-minimo">Não lembro minha senha</div>
          <button class="btnWormz" type="button" @click="submitLogin">
            ENTRAR
          </button>

          <v-row
            class="box-google d-flex align-center my-2"
            style="width: 70%; gap: 20px"
          >
            <v-divider color="#e8e5ae"></v-divider>
            <v-img class="img-google" src="Group 4.png"></v-img>
            <v-divider color="#e8e5ae"></v-divider>
          </v-row>
          <v-row
            class="box-google d-flex align-center justify-center my-2"
            style="width: 70%; gap: 20px"
          >
            <div class="subtitulo-minimo">Não tenho cadastro:</div>
            <button class="btnWormz" type="button" @click="submitSignIn">
              CADASTRAR
            </button>
          </v-row>
        </div>
      </v-col>
      <v-col class="m-5 mb-6 d-flex flex-column">
        <div class="box-title d-flex flex-column align-end mobile-hide-l">
          <titleWormz class="title-wormz"></titleWormz>
        </div>
      </v-col>
    </v-row>

    <v-snackbar v-model="loginMessage" timeout="2000" :color="loginColor">
      {{ loginText }}
      <template v-slot:action="{ attrs }">
        <v-btn color="black" text v-bind="attrs" @click="loginMessage = false">
          Fechar
        </v-btn>
      </template>
    </v-snackbar>
  </v-app>
</template>

<script>
import { mapActions } from "vuex";

export default {
  data() {
    return {
      roll: 0,
      show: false,
      user: {},
      loginMessage: false,
      loginColor: "",
      loginText: "",
    };
  },
  methods: {
    ...mapActions("auth", ["LOGIN", "LOGOUT"]),
    irPara(local) {
      this.$router.push({
        path: "/" + local,
      });
    },
    async submitLogin() {
      try {
        await this.LOGIN(this.user);

        this.loginMessage = true;
        this.loginText = "Login realizado com sucesso";
        this.loginColor = "sucess";

        setTimeout(() => {
          this.$router.push({
            path: "/SearchBib",
          });
        }, 1000);
      } catch (e) {
        this.loginMessage = true;
        this.loginText = "Falha na autenticação";
        this.loginColor = "error";
      }
    },
    submitSignIn() {
      this.$router.push({
        path: "/cadastroUser",
      });
    },
  },
};
</script>

<style lang="scss" scoped>
@include breakpoints;
.login-wormz {
  min-height: $template-height;
  width: 100vw;
  background-color: $bg-color !important;
  background-image: url("../assets/images/blobblue.png") !important;
  background-position: right !important;
  background-repeat: no-repeat !important;
  background-size: $template-height !important;
  overflow: hidden;
}

.title-wormz {
  transform: scale(0.7);
}

.box-title {
  position: fixed;
  bottom: 0;
  right: 0;
}

.img-google {
  height: 8vh;
  max-width: 8vh;
}
</style>