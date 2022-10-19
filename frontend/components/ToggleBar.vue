<template>
  <transition name="slide-fade">
    <div class="toggle-bar d-flex justify-space-between flex-column">
      <div class="div-wrapper">
        <div
          v-for="(item, index) in items"
          :key="index"
          @click="changeRoute(item.path)"
          class="list-wrapper subtitulo-minimo margin-left-page mt-5"
        >
          {{ item.name.toUpperCase() }}
        </div>
      </div>
      <div
        v-if="user.username"
        class="list-wrapper margin-left-page mt-5 mb-10"
        @click="show = !show"
      >
        <span class="subtitulo-minimo"> OLÁ, {{ user.username.toUpperCase() }} </span>
        <v-icon v-if="!show" class="v-icon-item">mdi-chevron-down</v-icon>
        <v-icon v-if="show" class="v-icon-item">mdi-chevron-up</v-icon>

        <div v-if="show" class="dropdown-content d-flex flex-column" style="gap:15px;">
          <div
            class="
              d-flex
              dropdown-item
              flex-row
              align-center
              subtitulo-minimo
              justify-between
              mt-4
            "
            @click="(show = false), transitionMaker('/PerfilUser')"
          >
            ACESSAR PERFIL
            <v-icon small class="v-icon-item ms-2">mdi-menu-right</v-icon>
          </div>
          
          <div class="subtitulo-minimo" @click="dialog = true">CONFIGURAÇÕES</div>

          <div
            class="
              d-flex
              dropdown-item
              flex-row
              align-center
              subtitulo-minimo
              justify-between
            "
            @click="(show = false), logOut()"
          >
            LOG-OUT
            <v-icon small class="v-icon-item ms-2">mdi-logout-variant</v-icon>
          </div>
        </div>
      </div>

      <ConfigUser :dialog="dialog" @close="dialog = false" />
    </div>
  </transition>
</template>

<script>
import { mapState, mapActions } from "vuex";
export default {
  data() {
    return {
      items: [
        { name: "Home", path: "/" },
        { name: "Login", path: "/loginWormz" },
        { name: "Explorar", path: "/SearchBib" },
        { name: "Biblioteca", path: "/userBib" },
        { name: "Quizz", path: "/quizz" },
      ],
      show: false,
      dialog: false
    };
  },
  methods: {
    ...mapActions('auth', ['LOGOUT']),
      transitionMaker(path){
        
        if (path != this.pageActive){
          this.pageActive = path
          this.transition = ''
        
          setTimeout(() =>
          {
              return this.$router.push({
                path: path
              });
            }, 200
          )
        }
      },
      logOut(){
        this.LOGOUT()
        this.$router.push({
          path: '/loginWormz'
        })
      },
    changeRoute(path) {
      this.$router.push({
        path: path,
      });
    },
  },
  computed: {
    ...mapState("auth", ["user"]),
  },
};
</script>

<style lang="sass" scoped>
@use '~/assets/sass/variables' as variables
@use '~/assets/sass/style'

.toggle-bar
  position: fixed
  top: variables.$header-height
  height: calc(100vh - 6vh)
  width: 50vw
  background-color: variables.$bg-color
  opacity: 90%
  z-index: 2

.slide-fade-enter-active, .slide-fade-leave-active
  transition: all 0.3s cubic-bezier(1, 0.5, 0.8, 1)

.slide-fade-leave-to
  transform: translateX(-50vw)
  opacity: 0

.slide-fade-enter
  transform: translateX(-50vw)
  opacity: 0
</style>