<template>
  <div class="input-group">
    <div class="input-group-prepend">
      <span class="input-group-text hover" id="inputGroupFileAddon01" @click="$emit('upload_file')" >Upload</span>
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
    components: {
      mdbFileInput
    },
  }
</script>
<style scoped>
    .hover:hover{
        cursor:pointer;
    }
</style>
