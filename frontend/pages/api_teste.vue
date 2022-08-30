<template>
  <div class="teste">
    {{this.api_key}} <br />
    {{ this.url }} <br />
    {{this.url_search}}   <br />

    <!-- livros.volumeInfo.imageLinks.thumbnail !-->
    <div v-for="(item, index) in livros" :key="index">
        {{item.volumeInfo.title}}
        <div v-if="imgs[index]">{{ imgs }}</div>
    </div>
  </div>
</template>

<script>
import {mapState, mapMutations} from 'vuex'
export default {
    data(){
        return{
            api_key: 'AIzaSyDb8Cue7PCPcACj9eba6p82EDDLHwXDNLk',
            url: 'https://www.googleapis.com/books/v1/volumes?q=',
            url_search: '',
            livros: {},
            imgs: []
        }
    },
    mounted(){
        this.MAKE_URL_SEARCH('O Retrato de Dorian Gray')
        this.GET_URL()
    },
    methods:{
        MAKE_URL_SEARCH(payload){
        this.url_search = this.url + payload + "&key=" + this.api_key
        console.log(this.url_search)
    },

    async GET_URL(){
        let dataItems = await this.$axios.$get(this.url_search)
        this.livros = dataItems.items

        for (let i = 0; i<dataItems.items.length; i++){
            this.imgs.push(dataItems.items[i].volumeInfo.imageLinks.thumbnail)
            console.log(this.imgs)
        }
    },
    }
}
</script>

<style>

</style>