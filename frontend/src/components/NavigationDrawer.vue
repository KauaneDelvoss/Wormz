<template>
  <div class="navigation-drawer d-flex align-center">
    <v-row class="list-wrapper d-flex align-center margin-left-page">
      <div v-for="(item, n) in items" :key="n" class="d-flex list-for mr-5" @click="transitionMaker(n, item.path)">
        <div v-if="activeItem == n" class="d-flex flex-grow-1">
          <div class="d-flex page-box">
            <div class="subtitulo list-item-box">
                {{ item.name.toUpperCase() }}
            </div>
          </div>
        </div>
        <div v-else class="subtitulo list-item">
          {{ item.name.toUpperCase() }}
        </div>
      </div>
    </v-row>
    <div class="icon-wrapper d-flex flex-row align-center margin-right-page">
      <div class="subtitulo list-item perfil">
          PERFIL
      </div>
      <v-icon class="v-icon-item">mdi-chevron-down</v-icon>
    </div>
    <hr class="divider-item" />
  </div>
</template>

<script>
export default {
  props:{ numActive: Number },
    data(){
        return{
            activeItem: this.numActive,
            transition: '',
            items: [
              { name: 'Home', path: '/home' },
              { name: 'Login', path: '/login' },
              { name: 'Explorar', path: '/searchBib'},
              { name: 'Biblioteca', path: '/userBib' },
              { name: 'Quizz', path: '/quizz' },
            ]
        }
    },
    methods:{
      transitionMaker(n, path){
        if (n != this.activeItem){
          this.transition = ''
          this.activeItem = n
        
          setTimeout(() =>
          {
              return this.$router.push({
                path: path
              });
            }, 200
          )
        }
      }
    }
};
</script>

<style lang="sass" scoped>
@use '@/assets/sass/style.sass'
@use '@/assets/sass/variables'

.list-for
  width: 7%
  height: 100%
  cursor: pointer

.list-wrapper
  height: 100%
  overflow: hidden

.navigation-drawer 
  width: 100vw
  height: 6vh
  background-color: #434c6d

.v-icon-item
  color: variables.$primary-color

.divider-item
  top: 6vh
  width: 100vw
  color: variables.$primary-color
  position: absolute

.page-box
  background-color: variables.$primary-color
  opacity: 50%
  justify-content: center
  margin-top: 10px
  border-radius: 10% 10% 0 0
  flex: 1

.list-item-box
  opacity: 100%
  color: variables.$bg-color

.list-item, .list-item-box
  align-self: center
  justify-self: center

.page-marker-enter-ative, .page-marker-leave-ative
  transition: opacity 0.8s ease

.page-marker-enter-from
  transition: opacity 0.3s ease-out
  transform: translateY(-50px)

.page-marker-leave-to
  transition: opacity 0.3s ease-out
  
  opacity: 0
  transform: translateY(50px)

</style>