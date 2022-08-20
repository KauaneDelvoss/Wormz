<template>
  <transition name="slide-fade">
  <div class="toggle-bar">
    <div class="list-wrapper subtitulo-minimo margin-left-page mt-5">
      HOME
    </div>
  </div>
  </transition>
</template>

<script>
export default {

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