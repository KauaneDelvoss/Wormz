export const state = () => ({
    loggedIn: false,
    user: {}
})

export const mutations = {
    SET_LOGIN_INFO(state, user){
        state.user = user
        state.loggedIn = true
    },
    SET_LOGOUT(state){
        state.user = {}
        state.loggedIn = false
    }
}

export const actions = {
    LOGIN( { commit }, user){
        commit('SET_LOGIN_INFO', user)
    },
    logout({commit}){
        commit('SET_LOGOUT',  user )
    }
}