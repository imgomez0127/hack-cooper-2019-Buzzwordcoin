<template>
  <accordion :panes="panes" material></accordion>
</template>

<script>
  import { Accordion } from 'mdbvue';
  export default {
    components: {
      Accordion,
    },
    props:["panes"]
}
</script>
