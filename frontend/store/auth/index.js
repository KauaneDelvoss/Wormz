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
    async LOGIN( { commit }, user){
        try{
            const userInfo = await this.$authServiceLogin.login(user)
            commit('SET_LOGIN_INFO', user)
            return Promise.resolve(userInfo)
        } catch(e) {
            commit('SET_LOGOUT')
            return Promise.reject(e)
        }
    },
    LOGOUT({commit}){
        commit('SET_LOGOUT')
    }
}