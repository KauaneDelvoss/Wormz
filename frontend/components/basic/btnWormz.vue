<template>
  <button class="btnWormz" type="button" @click="irPara(path)">
    {{ nome.toUpperCase() }}
  </button>
</template>

<script>
export default {
  props: { nome: String, path: String },
  methods: {
    irPara(path) {
      if (path) {
        this.$router.push({
          path: "/" + path,
        });
        this.$store.commit('ALTER_CURRENT_PATH', path)
      } else {
        this.$emit("sliderCount");
      }
    },
  }
};
</script>

<style lang="scss" scoped>
.btnWormz{
  background: $primary-color;
  border-radius: 20px;
  padding: 0.6vh 1.4vh;
  color: black;
  font-size: 1.5vh;
  font-family: "Encode Sans", sans-serif;

  &:hover{
    background: transparent;
    border: 1px solid $primary-color;
    color: $primary-color;
    transition: 00.5s;
  }
}

</style>