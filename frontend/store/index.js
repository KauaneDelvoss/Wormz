

export const state = () => ({
      currentPath: ''
    })

export const mutations = () => ({
        ALTER_CURRENT_PATH(state, payload){
            state.currentPath = payload
        }
    })