<template>
    <v-app class="default-app">
        <NavigationDrawer  />
        <Nuxt />
    </v-app>
</template>

<script>
export default {
}

</script>

<style lang="sass" scoped>
.default-app
    overflow: hidden
    max-height: 100vh
    min-height: 100vh
</style>