function plot_stats(type,myContainer, rosterCats,seriesData){

    Highcharts.chart(myContainer, {
        chart: {
            type: 'column',
            zoomType: 'x'
        },
        credits: {
            enabled: false
        },
        title: {
            text: type+' vs. Player'
        },

        xAxis: {
            categories: rosterCats
        },

        yAxis: {
            allowDecimals: false,
            min: 0,
            title: {
                text: type
            }
        },

        tooltip: {
            formatter: function () {
                return '<b>' + this.x + '</b><br/>' +
                    "Game: "+this.series.name + '<br/>' +
                    type+': ' + this.y;
            }
        },

        series: seriesData
    });
}