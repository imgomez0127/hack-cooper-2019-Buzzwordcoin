<template>
    <div>
        <div class = "box-wrapper">
            <div class="profile_box">
                <h1>Ian Gomez</h1>
            </div>
        </div>
        <div class="box">
            <Tabs v-on:change_page="$emit('change_page','B')" v-bind:current_balance='current_balance'/>
        </div>
    </div>
</template>

<script>
import Tabs from "./Tabs.vue"
export default{
    name:"WalletPage",
    components:{Tabs},
    props:["current_balance"]
}
</script>
<style scoped>
    .box{
        margin-top:10px;
        display:flex;
        justify-content:center;
        flex-wrap:wrap;
    }
    .box-wrapper{
        margin-top:30px;
        display:flex;
        justify-content:center;
    }
    .profile_box{
        display:flex;
        justify-content:flex-start;
        width:60%;
    }
</style>
