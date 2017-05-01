function disp(args1, args2){
var ctx = document.getElementById("myChart");
var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: args1,
        datasets: [{
            label: '# of tweets',
            data: args2,
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255,99,132,1)',
                'rgba(75, 192, 192, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero:true
                }
            }]
        }
    }
});}

function disp1(args1, args2){
var ctx = document.getElementById("myChart1");
var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: args1,
        datasets: [{
            label: '# of tweets',
            data: args2,
            backgroundColor: [
                'rgba(128, 0, 0, 0.2)',
                'rgba(0, 255, 0, 0.2)',
                'rgba(255, 255, 0, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(255, 0, 0, 0.2)',
                'rgba(0, 0, 128, 0.2)',
                'rgba(0, 255, 255, 0.2)',
                'rgba(0, 0, 255, 0.2)',
                'rgba(255, 0, 0, 0.2)',
                'rgba(0, 255, 0, 0.2)'
            ],
            borderColor: [
                'rgba(128, 0, 0, 0.6)',
                'rgba(0, 255, 0, 0.6)',
                'rgba(255, 255, 0, 0.6)',
                'rgba(75, 192, 192, 0.6)',
                'rgba(255, 0, 0, 0.6)',
                'rgba(0, 0, 128, 0.6)',
                'rgba(0, 255, 255, 0.6)',
                'rgba(0, 0, 255, 0.6)',
                'rgba(255, 0, 0, 0.6)',
                'rgba(0, 255, 0, 0.6)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero:true
                }
            }]
        }
    }
});}

function pie(args1, args2){

var pdata = {
    labels: args1,
    datasets: [
        {
            data: args2,
            backgroundColor: [
                "#1d8348",
                "#424949",
                "#5b2c6f"
            ],
            hoverBackgroundColor: [
                "#27ae60",
                "#b2babb",
                "#8e44ad"
            ]
        }]
};
var ctx = document.getElementById("myChart");
var myPieChart = new Chart(ctx,{
    type: 'pie',
    data: pdata,
    options: {
        animation:{
            animateScale:true
        }
    }
});}