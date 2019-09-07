<template>
    <div id="HomePage">
        <JumbotronPage v-on:change_page="$emit('change_page','B')"/>
        <div id="cards">
            <WaveCard title="Our mission" content="Our mission is to connect talented data scientists, machine learning engineers, and statisticians with large companies and researchers to create models which outperform state of the art implementations" imgSrc="https://mdbootstrap.com/img/Photos/Horizontal/Nature/4-col/img%20%286%29.jpg"/>
            <WaveCard title="What we do" content="We utilize a blockchain and partner with large companies to incentivize people to create high accuracy models, and reward them for performing well." imgSrc="https://mdbootstrap.com/img/Photos/Horizontal/Nature/4-col/img%20%287%29.jpg"/>
            <WaveCard title="How it Works" content="We utilize the results of a trained neural network to compute the hash function and based on the results of testing we reward people who have the highest performing models." imgSrc="https://mdbootstrap.com/img/Photos/Horizontal/Work/4-col/img%20%2821%29.jpg"/>
        </div>
    </div>
</template>

<script>
import  JumbotronPage from "./Jumbotron.vue"
import WaveCard from "./WaveCard.vue"

export default{
    name:"HomePage",
    components:{
        JumbotronPage,
        WaveCard
    }
}
</script>
<style scoped>
#cards{
    display:flex;
    justify-content:space-around;
    flex-wrap: wrap;
}

</style>
