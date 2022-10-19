export const state = () => ({
    api_key: 'AIzaSyDb8Cue7PCPcACj9eba6p82EDDLHwXDNLk',
    url: 'https://www.googleapis.com/books/v1/volumes?q=',
    url_search: '',
    books: {},
})

export const mutations = {
    MAKE_URL_SEARCH(state, payload){
        state.url_search = state.url + payload + "&maxResults=40" + "&key=" + state.api_key 
        console.log(state.url_search)
    },

    COMMIT_URL(state, payload){
        state.books = payload
    },
}

export const actions = {
    GET_URL({state, commit}){
            this.$axios.$get(state.url_search, {headers: {
                'Authorization': ''
            }})
            .then(res => { 
                commit('COMMIT_URL',  res.items)
            })
        },

    GET_BOOKS({state}, payload){
        const url_search = state.url + payload + "&maxResults=40" + "&key=" + state.api_key 
    
        this.$axios.$get(url_search, {headers: {
            'Authorization': ''
        }})
        .then(res => { 
            console.log(res.items)
            return res.items
        })
        
    }
}
