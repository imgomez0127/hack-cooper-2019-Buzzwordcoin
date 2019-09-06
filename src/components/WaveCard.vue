<template>
    <div class="card">
      <mdb-card>
        <mdb-card-image src="https://mdbootstrap.com/img/Photos/Horizontal/Nature/4-col/img%20%286%29.jpg" alt="Card image cap"></mdb-card-image>
        <mdb-card-body>
          <mdb-card-title>{{title}}</mdb-card-title>
          <mdb-card-text>{{Content}}</mdb-card-text>
        </mdb-card-body>
      </mdb-card>
    </div>
</template>

<script>
    import { mdbCard, mdbCardImage, mdbCardBody, mdbCardTitle, mdbCardText, mdbBtn } from 'mdbvue';
    export default {
        name: 'WaveCard',
        components: {
            mdbCard,
            mdbCardImage,
            mdbCardBody,
            mdbCardTitle,
            mdbCardText,
            mdbBtn
        },
        props:["title","Content"]
    }
</script>
<style>
    .card{
        margin-top:50px;
    }
</style>
