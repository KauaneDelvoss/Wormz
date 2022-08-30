<template>
  <div class="teste">
    {{this.api_key}} <br />
    {{ this.url }} <br />
    {{this.url_search}}   <br />

    <!-- livros.volumeInfo.imageLinks.thumbnail !-->
    <div v-for="(item, index) in livros" :key="index">
        {{item.volumeInfo.title}}
        {{item.volumeInfo.imageLinks.thumbnail}}
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
            livros: '',
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
        let dataItems = (await this.$axios.$get(this.url_search)).items
        this.livros = dataItems
        console.log(this.livros)
    },
    }
}
</script>

<style>

</style>