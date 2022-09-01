export const state = () => ({
    api_key: 'AIzaSyDb8Cue7PCPcACj9eba6p82EDDLHwXDNLk',
    url: 'https://www.googleapis.com/books/v1/volumes?q=',
    url_search: '',
    books: {},
})

export const mutations = {
    MAKE_URL_SEARCH(state, payload){
        state.url_search = state.url + payload + "&key=" + state.api_key
        console.log(state.url_search)
    },

    COMMIT_URL(state, payload){
        state.books = payload
    },
}

export const actions = {
    GET_URL({state, commit}){
            this.$axios.$get(state.url_search)
            .then(res => { 
                commit('COMMIT_URL',  res.items)
            })
        }
}