import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const store = new Vuex.Store({
  state: {
      step: 0,
      currentPage: 1,
      pageNum: 1,
      detail: {}
  },
  mutations: {
    stepchange(state, {n, item}){
      state.step=n;
      state.detail = item
      console.log("state.detail : ",state.detail)
      console.log("step:",state.step)
    },
    allpagenum(state, n){
      state.pageNum = n
      console.log("pageNum:",state.pageNum)
    },
    prevpage(state, n){
      if(state.currentPage > 1)
        state.currentPage -= n
      console.log("이전 현재페이지:",state.currentPage)
    },
    nextpage(state, n){
      if(state.currentPage < state.pageNum)
        state.currentPage += n
      console.log("다음 현재페이지:",state.currentPage)
    },
    gopage(state, n){
      state.currentPage = n
      console.log("이동 현재페이지:",state.currentPage)
    }
  }
});

export default store