<template>
  <div class="book-carousel">
    <div class="modifier d-flex flex-row justify-center" style="gap: 5px">
        <v-icon large class="v-icon-item" @click="scrollToLeft()">mdi-chevron-left</v-icon>
    <div class="carousel-wrapper align-center d-flex flex-row">
        <div v-for="(book, i) in books" :key="i" class="box-books">
              <CardBooks :book="book" class="mt-5 ms-2" />
        </div>
    </div>
        <v-icon large class="v-icon-item" @click="scrollToRight()">mdi-chevron-right</v-icon>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex';
export default {
    computed: {
        ...mapState("search_books", ["books"])
    },
    methods:{
        scrollToLeft(){
            const sliders = document.querySelector(".carousel-wrapper");
            const width = sliders.getBoundingClientRect().width
            sliders.scroll({
                top: 0,
                left: - width,
                behavior: 'smooth'
            })
        },
        scrollToRight(){
            const sliders = document.querySelector(".carousel-wrapper");
            const width = sliders.getBoundingClientRect().width
            console.log(width)
            sliders.scroll({
                top: 0,
                left: width,
                behavior: 'smooth'
            })
            
    }
    }
}
</script>

<style>
.carousel-wrapper{
    max-width: 100vw;
    overflow-x: hidden;
    gap: 10px;
}

</style>