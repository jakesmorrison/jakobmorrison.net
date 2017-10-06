function player_game_stat(data,cats,bands){
    Highcharts.chart('container', {
      chart: {
        type: 'areaspline'
      },
      title: {
        text: 'Player Progress'
      },
      legend: {
        borderWidth: 1,
        backgroundColor: (Highcharts.theme && Highcharts.theme.legendBackgroundColor) || '#FFFFFF'
      },
      xAxis: {
        categories: cats,
        plotBands: bands
      },
      yAxis: {
        title: {
          text: 'OPS'
        },
        min: 0,
        max: 4
      },
      tooltip: {
        shared: true,
        valueSuffix: ' OPS'
      },
      credits: {
        enabled: false
      },
      plotOptions: {
        areaspline: {
          fillOpacity: 0.5
        },
      },
      series: data
    });
}

