<template>
  <div class="navigation-drawer d-flex align-center">
    <div class="margin-left-page hide-desktop">
      <v-icon class="v-icon-item" @click="$emit('activeToggle', !toggleBar)">mdi-view-headline</v-icon>
    </div>
    <div class="list-wrapper d-flex flex-grow-1 flex-row margin-left-page align-center hide-mobile-l">
      <div v-for="(item, n) in items" :key="n" class="d-flex list-for mr-7" @click="transitionMaker(item.path)">
        <div v-if="item.path == pageActive" class="d-flex flex-grow-1">
          <div class="d-flex page-box">
            <div class="header-title list-item-box">
                {{ item.name.toUpperCase() }}
            </div>
          </div>
        </div>
        <div v-else class="header-title list-item">
          {{ item.name.toUpperCase() }}
        </div>
      </div>
    </div>
    <div class="icon-wrapper d-flex flex-row align-center justify-center margin-right-page hide-mobile-l">
      <div class="dropdown">
        <div v-if="user.username" class="header-title list-item perfil" @click="show = !show">
          <span>
            OLÁ, {{ user.username.toUpperCase() }}
          </span>
          <v-icon v-if="!show" class="v-icon-item">mdi-chevron-down</v-icon>
          <v-icon v-if="show" class="v-icon-item">mdi-chevron-up</v-icon>
        </div>
      </div>
      <div v-if="show" class="dropdown-content">
        <div class="d-flex dropdown-item flex-row align-center header-title justify-between" @click="show=false, transitionMaker('/PerfilUser')">ACESSAR PERFIL
          <v-icon small class="v-icon-item ms-2">mdi-menu-right</v-icon>
        </div>
        <div class="d-flex dropdown-item flex-row align-center header-title justify-between" @click="(show=false, showConfig = true)">CONFIGURAÇÕES
          <v-icon small class="v-icon-item ms-2">mdi-nut</v-icon>
        </div>
        <div class="d-flex dropdown-item flex-row align-center header-title justify-between" @click="show=false, logOut()">LOG-OUT
          <v-icon small class="v-icon-item ms-2">mdi-logout-variant</v-icon>
        </div>
        <ConfigUser :dialog="showConfig" @close="showConfig = false" />

        
      </div>
    </div>

    <v-divider class="divider-item" />

  </div>
</template>

<script>
import {mapActions, mapState} from 'vuex'
import ConfigUser from '~/components/ConfigUser'

export default {
  props: {activeToggleBar: Boolean}  ,
  components: {ConfigUser},
    data(){
        return{
            pageActive: '',
            transition: '',
            items: [
              { name: 'Home', path: '/' },
              { name: 'Login', path: '/loginWormz' },
              { name: 'Explorar', path: '/SearchBib'},
              { name: 'Biblioteca', path: '/userBib' },
              { name: 'Quizz', path: '/quizz' },
            ],
            toggleBar: false,
            show: false,
            showConfig: false,
        }
    },
    mounted() {
      let route = this.$router.currentRoute.path
      this.pageActive = route

      this.toggleBar = this.activeToggleBar
    },

    methods:{
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
      }
    },
    watch: {
      '$route' (to, from){
        this.pageActive = to.path
      }
    },
    computed: {
      ...mapState('auth', ['user'])
    }
};
</script>

<style lang="scss" scoped>
@include breakpoints;

.list-for{
  height: 100%;
  cursor: pointer;
}

.list-wrapper{
  height: 100%;
}

.navigation-drawer{
  top: 0;
  width: 100vw;
  height: $header-height;
  background-color: #434c6d;
  position: fixed;
  z-index: 2;
}

.v-icon-item{
  color: $primary-color;
}

.divider-item{
  top: $header-height;
  width: 100vw;
  border-color: $primary-color;
  z-index: 1;
  position: absolute;
}

.page-box{
  background-color: $primary-color;
  width: 6vw;
  opacity: 50%;
  justify-content: center;
  margin-top: 10px;
  border-radius: 10% 10% 0 0;
  flex: 1;
}

.list-item-box{
  opacity: 100%;
  color: $bg-color;
}

.list-item, .list-item-box{
  align-self: center;
  justify-self: center;
}

.dropdown{
  cursor: pointer;
}

.dropdown-content{
  position: absolute;
  z-index: 1;
  top: $header-height;
  min-width: 100px;
  background-color: $bg-color;
  padding: 10px;
  min-height: 10vh;
}

.dropdown-item:hover{
  text-decoration: underline;
  cursor: pointer;
}

</style>