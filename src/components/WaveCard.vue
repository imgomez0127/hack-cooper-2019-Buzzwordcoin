<template>
    <div class="info-card">
      <mdb-card>
        <mdb-card-image v-bind:src="imgSrc" v-bind:alt="altText"></mdb-card-image>
        <mdb-card-body class="fix-width">
          <mdb-card-title>{{title}}</mdb-card-title>
          <mdb-card-text class="wrap-words">{{Content}}</mdb-card-text>
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
        props:["title","Content","imgSrc","altText"]
    }
</script>
<style scoped>
    .fix-width{
        width:700px;
    }
    .info-card{
        margin-bottom:50px;
    }
    .wrap-words{
        word-wrap:break-word;
    }        
</style>
