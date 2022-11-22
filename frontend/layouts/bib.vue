<template>
  <v-app class="bib-view">
    <NavigationDrawer
      :activeToggleBar="activeToggleBar"
      @activeToggle="activeToggleBar = !activeToggleBar"
    />
    <ToggleBar v-if="activeToggleBar" class="hide-desktop" />
    <DesktopView class="hide-mobile-l" />
    <MobileView class="hide-desktop" />
  </v-app>
</template>

<script>
import DesktopView from '~/pages/bib/default/desktop'
import MobileView from '~/pages/bib/default/mobile'

export default {
  components: { DesktopView, MobileView },
  middleware: 'tokenInit',
  data(){
    return{
      activeToggleBar: false,
    }
  }
}
</script>

<style scoped lang="scss">
@include breakpoints;
</style>