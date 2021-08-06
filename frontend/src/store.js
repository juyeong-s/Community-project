import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const store = new Vuex.Store({
  state: {
      step: 0
  },
  mutations: {
    stepchange(state,n){
      state.step=n;
      console.log(state.step)
    }
  }
});

export default store