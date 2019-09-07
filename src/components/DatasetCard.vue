<template>
    <div class="info-card">
      <mdb-card>
        <mdb-card-body class="fix-width">
          <mdb-card-title>{{title}}</mdb-card-title>
          <mdb-card-text class="wrap-words">{{content}}</mdb-card-text>
          <Button message="Download Dataset" v-bind:link="title"/>
          <div class="file-input">
            <FileInput v-on:upload_file="$emit('upload_file')"/>
          </div>
        </mdb-card-body>
      </mdb-card>
    </div>
</template>

<script>
    import { mdbCard, mdbCardImage, mdbCardBody, mdbCardTitle, mdbCardText, mdbBtn,  } from 'mdbvue';
    import Button from "./Button.vue"
    import FileInput from "./FileInput.vue"
    export default {
        name: 'DatasetCard',
        components: {
            mdbCard,
            mdbCardImage,
            mdbCardBody,
            mdbCardTitle,
            mdbCardText,
            mdbBtn,
            Button,
            FileInput
        },
        props:["title","content"]
    }
</script>
<style scoped>
    .fix-width{
        width:950px;
    }
    .info-card{
        margin-bottom:50px;
    }
    .wrap-words{
        word-wrap:break-word;
    }        
    .file-input{
        margin-top:50px;
    }
</style>
