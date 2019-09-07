<template>
  <div class="spinner-border text-primary" role="status">
    <span class="sr-only">Loading...</span>
  </div>
</template>

<script>
  import { mdbSpinner } from 'mdbvue';
  export default {
    name: 'PageLoader',
    components: {
      mdbSpinner
    }
  }
</script>
