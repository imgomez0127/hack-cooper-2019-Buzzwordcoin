<template>
    <mdb-tabs
    :active="0"
    default
    :links="[
      { text: 'Wallet' },
      { text: 'Statistics' }
      ]"
    :transition-duration="0.5"
    transition-style="linear"
  >
    <template :slot="'Wallet'">
      <mdb-container>
        <mdb-jumbotron class="text-center hoverable">
          <mdb-row>
            <mdb-col md="4" offsetMd="1" class="m-3">
              <mdb-view src="https://mdbootstrap.com/img/Photos/Others/laptop-sm.jpg" alt="Sample image for first version of blog listing">
                <a><mdb-mask waves overlay="white-slight"/></a>
              </mdb-view>
            </mdb-col>
            <mdb-col md="7" class="text-md-left ml-3 mt-3">
              <a href="#!" class="green-text">
                <h2 class="h6 pb-1"><mdb-icon icon="wallet" class="pr-1"/>My Wallet</h2>
              </a>
              <h1 class="h4 mb-4">Current Balance</h1>
              <h3 class="font-weight-normal">{{current_balance}} ML Coins</h3>
              <mdb-btn color="primary" @click="$emit('change_page','B')">Submit More Models</mdb-btn>
            </mdb-col>
          </mdb-row>
        </mdb-jumbotron>
      </mdb-container>
    </template>
    <template :slot="'Statistics'">
      <mdb-container>
        <mdb-jumbotron class="text-center hoverable">
              <h3 class="font-weight-bold mb-3 p-0">
                <strong>Recent Rankings</strong>
              </h3>
            <LineChart/>
        </mdb-jumbotron>
        <mdb-jumbotron class="text-center hoverable">
            <h3 class="font-weight-bold mb-3 p-0">
                <strong>Most Popular Architectures</strong>
            </h3>
            <BubbleChart/>
        </mdb-jumbotron>
      </mdb-container>
    </template>
  </mdb-tabs>
</template>

<script>
  import { mdbContainer, mdbCol, mdbRow, mdbIcon, mdbTabs, mdbJumbotron, mdbView, mdbMask, mdbBtn, mdbTextarea, mdbInput, mdbCarousel, mdbCarouselItem } from 'mdbvue';
  import LineChart from "./LineChart.vue"
  import BubbleChart from "./BubbleChart.vue"
  export default {
    name: 'TabPage',
    components: {
      mdbContainer,
      mdbCol,
      mdbRow,
      mdbIcon,
      mdbTabs,
      mdbJumbotron,
      mdbView,
      mdbMask,
      mdbBtn,
      mdbTextarea,
      mdbInput,
      mdbCarouselItem,
      mdbCarousel,
      LineChart,
      BubbleChart
    },
    props:["current_balance"]
  };
</script>
