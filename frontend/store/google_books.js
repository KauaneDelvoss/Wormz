export const state = () => ({
    api_key: 'AIzaSyDb8Cue7PCPcACj9eba6p82EDDLHwXDNLk',
    url: 'https://www.googleapis.com/books/v1/volumes?q=',
    url_search: ''
})

export const mutations = () => ({
    MAKE_URL_SEARCH(state, payload){
        state.url_search = state.url + payload + "&key=" + state.api_key
        console.log(url_search)
    },

    GET_URL(state){
        axios.get(state.url_search)
        .then(res => { 
            let data = res.data;
            console.log(res);
            console.log(data)
            })
    },
})