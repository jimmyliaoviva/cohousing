//singleOldPie
var singleOldCtx = document.getElementById('singleOld').getContext('2d');
var singleOldPie = new Chart(singleOldCtx, {
    // The type of chart we want to create
    type: 'doughnut',

    // The data for our dataset
    data: {
        labels: ['獨居', '群居'],
        datasets: [{
            label: 'My First dataset',
            backgroundColor: ['rgb(242, 160, 87)','rgb(142,142,142)'],
            borderAlign:'inner',
            data: [60, 100]
        }]
    },
    // Configuration options go here
    options: {
        cutoutPercentage:70,
        legend:false,
    }
});
//rent percent pie chart
var rentPercentCtx = document.getElementById('rentPercent').getContext('2d');
var rentPercentPie = new Chart(rentPercentCtx, {
    // The type of chart we want to create
    type: 'doughnut',

    // The data for our dataset
    data: {
        labels: ['獨居', '群居'],
        datasets: [{
            label: 'My First dataset',
            backgroundColor: ['rgb(242, 160, 87)','rgb(142,142,142)'],
            borderAlign:'inner',
            data: [60, 100]
        }]
    },
    // Configuration options go here
    options: {
        cutoutPercentage:70,
        legend:false,

    }
});

//bar chart
var barChartCtx = document.getElementById('barChart').getContext('2d');
var barChart = new Chart(barChartCtx, {
    // The type of chart we want to create
    type: 'bar',

    // The data for our dataset
    data: {
        labels: ['龍坡里', '仁愛里','德安里','誠安里','光武里'],
        datasets: [{
            label: '獨居長者人數',
            backgroundColor: 'rgb(242, 160, 87)',
            borderAlign:'inner',
            data: [700, 1000, 450, 550, 100]
        },
        {
            label: '租屋族人數',
            backgroundColor: 'rgb(242, 215, 133)',
            borderAlign:'inner',
            data: [900, 800, 750, 50, 750]
        }
        ]
    },
    // Configuration options go here
    options: {
    }
});