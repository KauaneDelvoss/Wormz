<template>
  <v-app class="default-app">
    <NavigationDrawer
      :activeToggleBar="activeToggleBar"
      @activeToggle="activeToggleBar = !activeToggleBar"
    />
    <ToggleBar v-if="activeToggleBar" />
    <Nuxt />
  </v-app>
</template>

<script>
export default {
  data() {
    return {
      activeToggleBar: false,
    };
  },
};
</script>

<style lang="sass" scoped>
.default-app
    position: relative
    overflow: hidden
    max-height: 100vh
    min-height: 100vh

</style>