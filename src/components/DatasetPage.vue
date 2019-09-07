<template>
    <div id="datasetPage">

        <div id="carouselBackground">
            <Carousel id="carousel"/>
        </div>
        <div id="accordian" v-if="loaded">
            <div v-for="dataset in panes">
                <DatasetCard v-bind:title="dataset.title" v-bind:content="dataset.content" v-on:upload_file="$emit('upload_file')"/>
            </div>

        </div>
        <div id="loading" v-else class="spinner">
            <Loading/>
        </div>
    </div>
</template>

<script>
const axios = require("axios");
import Accordian from "./Accordian.vue"
import Carousel from "./Carousel.vue"
import Loading from "./Loading.vue"
import DatasetCard from "./DatasetCard.vue"
export default{
    name:"DatasetPage",
    components:{Accordian,Carousel,Loading,DatasetCard},
    async created(){
        await this.x()
    },
    methods:{
        async x() {
            const test = await axios.get("http://localhost:8000/get-datasets",{
                method: 'HEAD',
                mode: 'no-cors',
                headers: {
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Credentials':true,
                },
            });
            this.panes = test["data"];
            console.log(this.panes[0]["content"])
            this.loaded = true;
        }
    },
    data(){
        return {
            panes:[],
            loaded:false
        };
    } 

}
</script>
<style scoped>
    #datasetPage{
        flex-wrap:wrap;   
        display:flex;
        justify-content:center;
    }
    #accordian{
        width:50%;
        margin-top:50px;
        margin-bottom:50px;
    }
    #carousel{
        margin-top:50px;
        margin-bottom:50px;    
    }
    .spinner{
        width:200%;
    }
    #carouselBackground{
        display:flex;
        justify-content:center;
        background:#f4f4f4;
        width:100%;
    }
</style>
