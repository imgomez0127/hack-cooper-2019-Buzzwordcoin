<template>
  <mdb-container>
    <mdb-bubble-chart :data="bubbleChartData" :options="bubbleChartOptions" :width="600" :height="300"></mdb-bubble-chart>
  </mdb-container>
</template>

<script>
  import { mdbBubbleChart, mdbContainer } from 'mdbvue';
  export default {
    name: 'BubbleChart',
    components: {
      mdbBubbleChart,
      mdbContainer
    },
    data() {
      return {
        bubbleChartData: {
          datasets: [
            {
              label: "Support Vector Machine",
              backgroundColor: "rgba(255, 99, 132, 0.1)",
              borderColor: "rgba(255, 99, 132, 1)",
              borderWidth: 0.7,
              data: [{
                x: 5,
                y: 7,
                r: 20
              }]
            },
            {
              label: "Artificial Neural Network",
              backgroundColor: "rgba(151,187,205,0.2)",
              borderColor: "rgba(151,187,205,1)",
              borderWidth: 0.8,
              data: [{
                x: 15,
                y: 2,
                r: 20
              }]
            },
            {
              label: "Convolutional Neural Network",
              backgroundColor: "rgba(255, 206, 86, 0.2)",
              borderColor: "rgba(255, 206, 86, 1)",
              borderWidth: 0.8,
              data: [{
                x: 10,
                y: 4,
                r: 30
              }]
            },
             {
                label: "Linear Regression",
                backgroundColor: "rgba(202,32,79,0.2)",
                borderColor:"rgba(197,27,74)",
                borderWidth:0.8,
                data: [{
                    x:10,
                    y:6,
                    r:20,
                }]
            }

          ]
        },
        bubbleChartOptions: {
          responsive: false,
          maintainAspectRatio: false,
          scales: {
            xAxes: [{
              gridLines: {
                display: true,
                color: "rgba(0, 0, 0, 0.1)",
              }
            }],
            yAxes: [{
              gridLines: {
                display: true,
                color: "rgba(0, 0, 0, 0.1)",
              }
            }],
          }
        },
      };
    }
  }
</script>
