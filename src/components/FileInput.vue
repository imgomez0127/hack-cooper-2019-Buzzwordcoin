<template>
  <div class="input-group">
    <div class="input-group-prepend">
      <span class="input-group-text" id="inputGroupFileAddon01" @click="test">Upload</span>
    </div>
    <div class="custom-file">
      <input type="file" class="custom-file-input" id="inputGroupFile01" aria-describedby="inputGroupFileAddon01">
      <label class="custom-file-label" for="inputGroupFile01">Choose file</label>
    </div>
  </div>
</template>

<script>
  import { mdbFileInput } from 'mdbvue';
  export default {
    name: "FileInput",
    componens: {
      mdbFileInput
    },
    methods: {
        test(){
            console.log("hello world");
        }
    }
  }
</script>
