<template>
  <div class="carouselWidth">
  <mdb-carousel :interval="8000" showControls showIndicators class="carousel">
    <mdb-carousel-item img src="https://mdbootstrap.com/img/Photos/Slides/img%20(68).jpg" mask="black-light" alt="First slide">
      <mdb-carousel-caption title="ImageNet" text="First text"></mdb-carousel-caption>
    </mdb-carousel-item>
    <mdb-carousel-item img src="https://mdbootstrap.com/img/Photos/Slides/img%20(6).jpg" mask="black-strong" alt="Second slide">
      <mdb-carousel-caption title="MNIST" text="Second text"></mdb-carousel-caption>
    </mdb-carousel-item>
    <mdb-carousel-item img src="https://mdbootstrap.com/img/Photos/Slides/img%20(9).jpg" mask="black-slight" alt="Third slide">
      <mdb-carousel-caption title="Boston Housing Prices" text="Third text"></mdb-carousel-caption>
    </mdb-carousel-item>
  </mdb-carousel>
  </div>
</template>

<script>
  import { mdbCarousel, mdbCarouselItem, mdbCarouselCaption } from 'mdbvue';
  export default {
    name: 'CarouselPage',
    components: {
      mdbCarousel,
      mdbCarouselItem,
      mdbCarouselCaption
    }
  }
</script>

<style scoped>
    .carouselWidth{ 
        width:1200px;
    }  
    .carousel{
        box-shadow:5px 5px 5px;
    }
</style>
