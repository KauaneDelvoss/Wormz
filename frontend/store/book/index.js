export const state = () => ({
    book: {},
    api_key: 'AIzaSyDb8Cue7PCPcACj9eba6p82EDDLHwXDNLk',

})

export const mutations = {
    COMMIT_URL(state, payload){
        state.bookshelf = payload
    },
}

export const actions = {
    GET_URL({state, commit}, id){
            const url = 'https://www.googleapis.com/books/v1/volumes/' + id + "&key=" + state.api_key
            this.$axios.$get(url, {headers: {
                'Authorization': ''
            }})
            .then(res => { 
                commit('COMMIT_URL',  res.items)
                console.log(res)
            })
        }
    }