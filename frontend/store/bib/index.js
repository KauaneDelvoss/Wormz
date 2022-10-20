export const state = () => ({
    bookshelf: {},
    api_key: 'AIzaSyDb8Cue7PCPcACj9eba6p82EDDLHwXDNLk',

})

export const mutations = {
    COMMIT_URL(state, payload){
        state.bookshelf.books = payload
        state.bookshelf.name = 'Nome da Estante'
        state.bookshelf.description = 'Descrição da Estante'
    },
}

export const actions = {
    GET_URL({state, commit}){
            const url_search = 'https://www.googleapis.com/books/v1/volumes?q=' + 'kafka a beira mar'+ "&maxResults=40" + "&key=" + state.api_key 
            this.$axios.$get(url_search, {headers: {
                'Authorization': ''
            }})
            .then(res => { 
                commit('COMMIT_URL',  res.items)
            })
        }
    }