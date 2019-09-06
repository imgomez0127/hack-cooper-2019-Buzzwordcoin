<template>
    <div id="HomePage">
        <Navbar/>
        <JumbotronPage/>
        <div id="cards">
            <WaveCard title="Our mission" content=""/>
            <WaveCard title="Our mission" content=""/>
            <WaveCard title="Our mission" content=""/>
        </div>
    </div>
</template>

<script>
import  JumbotronPage from "./Jumbotron.vue"
import Navbar from "./Navbar.vue"
import WaveCard from "./WaveCard.vue"

export default{
    name:"HomePage",
    components:{
        JumbotronPage,
        Navbar,
        WaveCard
    }
}
</script>
<style>
#cards{
    display:flex;
    justify-content:space-around;
    flex-wrap: wrap;
}

</style>
