<template>
  <v-app class="default-app">
    <NavigationDrawer
      :activeToggleBar="activeToggleBar"
      @activeToggle="activeToggleBar = !activeToggleBar"
    />
    <ToggleBar v-if="activeToggleBar" class="hide-desktop" />
    <Nuxt />
  </v-app>
</template>

<script>
export default {
  middleware: 'tokenInit',
  data() {
    return {
      activeToggleBar: false,
    };
  }
};
</script>

<style lang="sass" scoped>
@use '~/assets/sass/mixins'

.default-app
    position: relative
    overflow: hidden
    min-height: 100vh

</style>