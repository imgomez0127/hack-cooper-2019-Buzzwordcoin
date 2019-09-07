<template>
  <div id="app">
    <Navbar v-on:change_page="changeRender"/>
    <div v-if="page === 'A'">
        <HomePage v-on:change_page="changeRender"/>
    </div>  
    <div v-if="page === 'B'">
        <DatasetPage v-on:upload_file='upload_file'/>
    </div>
    <div v-if="page === 'C'">
        <WalletPage v-on:change_page="changeRender" v-bind:current_balance='current_balance'/>
    </div>
  </div>
</template>

<script>
import Navbar from "./components/Navbar.vue"
import HomePage from "./components/HomePage.vue"
import DatasetPage from "./components/DatasetPage.vue"
import WalletPage from "./components/Wallet.vue"
function getRandomInt(max) {
  return Math.floor(Math.random() * Math.floor(max));
}
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
            page: 'A',
            current_balance: "100.00"
        }
    },
    methods:{
        changeRender(id){
            console.log(id)
            this.page = id;
        },
        upload_file(){
            this.current_balance = parseInt(this.current_balance) + getRandomInt(100);
            this.page = 'C';
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
