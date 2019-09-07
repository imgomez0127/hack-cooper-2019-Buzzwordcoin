<template>
    <div>
        <!-- Provides extra visual weight and identifies the primary action in a set of buttons -->
        <mdb-btn color="primary" @click="download">{{message}}</mdb-btn>
    </div>
</template>

<script>
    const axios = require("axios");
    import { mdbBtn } from 'mdbvue';
    export default {
        name: 'Button',
        components: {
            mdbBtn
        },
        methods:{
            async download(){
                    const test = await axios.get("http://localhost:8000/download-dataset/"+this.link,{
                    method: 'HEAD',
                    mode: 'no-cors',
                    headers: {
                        'Access-Control-Allow-Origin': '*',
                        'Access-Control-Allow-Credentials':true,
                    },
                    responseType:'blob'
                });
                const url = window.URL.createObjectURL(new Blob([test.data]));
                const link = document.createElement('a');
                link.href = url;
                link.setAttribute('download',this.link+".zip");
                document.body.appendChild(link);
                link.click()
            }
        },
        props:["message","link"]
    }
</script>
