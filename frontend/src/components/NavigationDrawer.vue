<template>
  <div class="navigation-drawer d-flex align-center">
    <v-row class="list-wrapper d-flex align-center margin-left-page teste2">
      <div v-for="(item, n) in items" :key="n" class="d-flex teste mr-5">
        <div v-if="activeItem == n" class="page-box">
            <div class="subtitulo list-item-box">
                {{ item.toUpperCase() }}
            </div>
        </div>
        <div v-else class="subtitulo list-item">
          {{ item.toUpperCase() }}
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
    data(){
        return{
            items: ['Home', 'Login'],
            activeItem: 1
        }
    },
    mounted(){
      this.showPageBox();
    },
    methods:{
      showPageBox(){

      }
    }
};
</script>

<style lang="sass" scoped>
@use '@/assets/sass/style.sass'
@use '@/assets/sass/variables'

.teste
  width: 7%
  height: 100%

.teste2
  height: 100%

.navigation-drawer 
  width: 100vw
  height: 7vh
  background-color: #434c6d

.v-icon-item
  color: variables.$primary-color

.divider-item
  top: 7vh
  width: 100vw
  color: variables.$primary-color
  position: absolute

.page-box
  z-index: 0
  background-color: variables.$primary-color
  opacity: 50%
  display: flex
  justify-content: center
  margin-top: 10px
  border-radius: 10% 10% 0 0
  flex: 1

.list-item-box
  opacity: 100%
  z-index: 2
  color: variables.$bg-color
  align-self: center

.list-item
  align-self: center
  justify-self: center
</style>