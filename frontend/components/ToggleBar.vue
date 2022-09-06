<template>
  <transition name="slide-fade">
  <div class="toggle-bar">
    <div v-for="(item, index) in items" :key="index" @click="changeRoute(item.path)" class="list-wrapper subtitulo-minimo margin-left-page mt-5">
      {{ item.name.toUpperCase() }}
    </div>
  </div>
  </transition>
</template>

<script>
export default {
  data(){
    return {
      items: [
              { name: 'Home', path: '/' },
              { name: 'Login', path: '/loginWormz' },
              { name: 'Explorar', path: '/SearchBib'},
              { name: 'Biblioteca', path: '/userBib' },
              { name: 'Quizz', path: '/quizz' },
            ],
    }
  },
  methods:{
    changeRoute(path){
      this.$router.push({
        path: path
      })
    }
  }
}
</script>

<style lang="sass" scoped>
@use '~/assets/sass/variables' as variables
@use '~/assets/sass/style'

.toggle-bar
    position: absolute
    top: variables.$header-height
    height: 100vh
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