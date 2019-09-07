<template>
  <div id="app">
    <Navbar v-on:change_page="changeRender"/>
    <div v-if="page === 'A'">
        <HomePage v-on:change_page="changeRender"/>
    </div>  
    <div v-if="page === 'B'">
        <DatasetPage/>
    </div>
    <div v-if="page === 'C'">
        <WalletPage/>
    </div>
  </div>
</template>

<script>
import Navbar from "./components/Navbar.vue"
import HomePage from "./components/HomePage.vue"
import DatasetPage from "./components/DatasetPage.vue"
import WalletPage from "./components/Wallet.vue"
export default {
    name: 'App',
    components:{
        HomePage,
        DatasetPage,
        WalletPage,
        Navbar
    },
    data(){ 
        return {
            page: 'A'
        }
    },
    methods:{
        changeRender(id){
            console.log(id)
            this.page = id;
        }
    }
    
}
</script>

<style scoped>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
