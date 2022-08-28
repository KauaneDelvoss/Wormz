<template>
  <div class="cadastro-wormz">
    <v-row class="app d-fluid flex-row" style="height: 100vh">
      <v-col class="m-5 d-flex flex-column justify-center col-default">
        <div class="titulo d-flex flex-column align-center">Cadastro</div>
        <div v-if="sliderValue == 0">
          <transition :name="transition">
            <FirstSlider>
              <btnWormz :nome="'Próximo'" @sliderCount="next()" />
            </FirstSlider>
          </transition>
        </div>
        <div v-if="sliderValue == 1">
          <transition :name="transition">
            <SecondSlider>
              <v-row style="gap: 2vw">
                <btnWormz :nome="'Anterior'" @sliderCount="prev()" />
                <btnWormz :nome="'Próximo'" @sliderCount="next()" />
              </v-row>
            </SecondSlider>
          </transition>
        </div>
        <div v-if="sliderValue == 2">
          <transition :name="transition">
            <ThirdSlider>
              <v-row style="gap: 2vw">
                <btnWormz :nome="'Anterior'" @sliderCount="prev()" />
                <btnWormz :nome="'Concluir'" :path="'/loginWormz'" />
              </v-row>
            </ThirdSlider>
          </transition>
        </div>
      </v-col>

      <v-col cols="6" class="m-5 mb-6 d-flex flex-column hide-mobile-xl">
        <div class="box-title d-flex flex-column align-end">
          <titleWormz class="title-wormz"></titleWormz>
        </div>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import FirstSlider from '@/pages/cadastro/FirstSlider.vue'
import SecondSlider from '@/pages/cadastro/SecondSlider.vue'
import ThirdSlider from '@/pages/cadastro/ThirdSlider.vue'

export default {
  components: { FirstSlider, SecondSlider, ThirdSlider },
  data() {
    return {
      sliderValue: 0,
      active: false,
      transition: "",
      };
  },
  methods: {
    next() {
      this.goToIndex(this.nextIndex);
    },
    prev() {
      this.goToIndex(this.prevIndex);
    },
    goToIndex(index) {
      const direction = index > this.sliderValue ? "left" : "right";
      if (direction == "left") {
        this.show(direction);
      } else {
        this.hide(direction);
      }
      this.sliderValue = index;
    },
    hide(direction) {
      this.transition = `SliderSlide--transition-${direction}`;
      this.active = false;
    },
    show(direction) {
      this.transition = `SliderSlide--transition-${direction}`;
      this.active = true;
    },
  },
  computed: {
    nextIndex() {
      const nextIndex = this.sliderValue + 1;
      return nextIndex <= 3 - 1 ? nextIndex : 0;
    },
    prevIndex() {
      const prevIndex = this.sliderValue - 1;
      return prevIndex >= 0 ? prevIndex : 3 - 1;
    },
  },
  mounted() {
      this.goToIndex(this.sliderValue);
  },
};
</script>

<style lang="scss" scoped>
@include breakpoints;

.cadastro-wormz {
  height: $template-height;
  width: 100vw;
  background-color: #22273c;
  background-image: url("@/assets/images/blobblue.png");
  background-position: right;
  background-repeat: no-repeat;
  background-size: $template-height;
  overflow: hidden;
}

.title-wormz {
  transform: scale(0.7);
}

.box-title {
  position: absolute;
  bottom: 0;
  right: 0;
}

.titulo {
  font-family: "Libre Baskerville", serif;
  font-size: 5vh;
  color: #e8e5ae;
}

.SliderSlide--transition-left-enter-active,
.SliderSlide--transition-left-leave-active,
.SliderSlide--transition-right-enter-active,
.SliderSlide--transition-right-leave-active {
  transition-duration: 0.5s;
  transition-property: height, opacity, transform;
  transition-timing-function: cubic-bezier(0.55, 0, 0.1, 1);
}

.SliderSlide--transition-left-leave-active,
.SliderSlide--transition-right-leave-active {
  position: absolute;
  overflow: hidden;
}

.SliderSlide--transition-left-enter,
.SliderSlide--transition-right-leave-active {
  opacity: 0;
  transform: translate(2em, 0);
}

.SliderSlide--transition-left-leave-active,
.SliderSlide--transition-right-enter {
  opacity: 0;
  transform: translate(-2em, 0);
}
</style>
