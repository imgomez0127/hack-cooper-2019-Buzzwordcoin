<template>
    <div id="jumbotron">
      <mdb-card class="card-image" style="background-image: url(https://mdbootstrap.com/img/Photos/Others/gradient1.jpg)">
        <div class="text-white text-center py-5 px-4 my-5">
          <div>
            <h2 class="card-title h1-responsive pt-3 mb-5 font-bold"><strong>ML Coin a Cryptocurrency Focused on Making Machine Learning More Open Sourced</strong></h2>
            <p class="mx-5 mb-5">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Repellat fugiat, laboriosam, voluptatem,
              optio vero odio nam sit officia accusamus minus error nisi architecto nulla ipsum dignissimos. Odit sed qui, dolorum!
            </p>
            <mdb-btn outline="white" size="md" icon="clone" @click="$emit('change_page','B')">View Datasets</mdb-btn>
          </div>
        </div>
      </mdb-card>
    </div>
</template>

<script>
   
  import { mdbCard, mdbBtn } from 'mdbvue';
  export default {
    name: 'JumbotronPage',
    components: {
      mdbCard,
      mdbBtn
    }
  }
</script>

<style>
    #jumbotron{
       margin-bottom:50px;
    } 
</style>    
