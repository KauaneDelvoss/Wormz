<template>
  <div class="book-carousel">
    <div class="modifier d-flex flex-row justify-center" style="gap: 5px">
        <v-icon large class="v-icon-item" @click="scrollToLeft()">mdi-chevron-left</v-icon>
    <div :id="carouselId" class="carousel-wrapper align-center d-flex flex-row">
        <div v-for="(book, i) in books" :key="i" class="box-books">
              <CardBooks :book="book" class="mt-5 ms-2" />
        </div>
    </div>
        <v-icon large class="v-icon-item" @click="scrollToRight()">mdi-chevron-right</v-icon>
    </div>
  </div>
</template>

<script>
export default {
    props: ['books', 'carouselId'],
    data(){
        return{
            scroll: 0,
        }
    },
    methods:{
        scrollToLeft(){
            let sliders = document.querySelector(`#${this.carouselId}`);
            let width = sliders.getBoundingClientRect().width
            sliders.scroll({
                top: 0,
                left: (this.scroll-width),
                behavior: 'smooth'
            })
            this.scroll-=width
            if (this.scroll < 0){
                this.scroll = 0
            }
        },
        scrollToRight(){
            let sliders = document.querySelector(`#${this.carouselId}`);
            let width = sliders.getBoundingClientRect().width
            let width_box = (document.querySelector(".box-books").getBoundingClientRect().width)*(document.querySelectorAll('.box-books').length)
            sliders.scroll({
                top: 0,
                left:(this.scroll + width),
                behavior: 'smooth'
            })
            this.scroll += width
            if (this.scroll > width_box){
                this.scroll = 0
            }
    }   
    }
}
</script>

<style scoped lang="scss">

.carousel-wrapper {
    max-width: 100vw;
    overflow-x: hidden;
    gap: 10px;
}

</style>