var bodySelection1 = d3.select(".plot1");

createCircle1()

function calArcs(divisons) {
  maxRad = 6.28319;
  gap = .1
  start = []
  stop = []
  increments = (maxRad / divisons);
  for (i = 0; i < divisons; i++) {
    if (i === 0) {
      start[i] = 0 + gap / 2;
      stop[i] = increments - gap / 2;
    } else {
      start[i] = stop[i - 1] + gap;
      stop[i] = stop[i - 1] + increments;
    }
  }
  return [start,stop]
}

function createCircle1() {
  arcs = calArcs(5);
  startAngle = arcs[0];
  stopAngle = arcs[1];

  var svgContainer = bodySelection1.append("svg")
    .attr("width", 200)
    .attr("height", 200);

  svgContainer.append("text")
    .style("text-anchor", "middle")
    .text("jake");

  var circle1 = svgContainer.selectAll("path")
    .data(startAngle)
    .enter()
    .append("path")
    .attr("d", d3.arc()
      .innerRadius(function(d, i) {
        return 50;
      })
      .outerRadius(function(d, i) {
        return 70;
      })
      .startAngle(function(d, i) {
        return startAngle[i]
      })
      .endAngle(function(d, i) {
        return stopAngle[i]
      })
    )
    .attr("transform", "translate(100,100)")
    .style("fill", "red")
    .on("click", function(d, i) {
      alert(d);
    })
    .on("mouseover", function(d, i) {
        console.log(i);
        d3.select(this).transition()
          .duration(500)
          .attr("d", d3.arc()
            .innerRadius(function(d) {
              return 1;
            })
            .outerRadius(function(d) {
              return 100;
            })
            .startAngle(function(d) {
              return startAngle[i]
            })
            .endAngle(function(d) {
              return stopAngle[i]
            })
          )
    })
    .on("mouseout", function(d, i) {
        d3.select(this).transition()
          .duration(500)
          .attr("d", d3.arc()
            .innerRadius(function(d) {
              return 50;
            })
            .outerRadius(function(d) {
              return 70;
            })
            .startAngle(function(d) {
              return startAngle[i]
            })
            .endAngle(function(d) {
              return stopAngle[i]
            })
          )
    });

}

