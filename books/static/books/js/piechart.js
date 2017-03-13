function piechart(arr) {
  var bodySelection1 = d3.select(".plot1");
//  myarr = [{
//    "text": "Being Mortal",
//    "value": 87090,
//    "color": "rgba(144,153,255,1)"
//  }, {
//    "text": "The Road",
//    "value": 59691,
//    "color": "rgba(0,153,255,.5)"
//  }, {
//    "text": "The Hitchhikers Guide to the Galaxy	",
//    "value": 76836,
//    "color": "rgba(0,153,255,.5)"
//  }, {
//    "text": "The Sun Also Rises",
//    "value": 70839,
//    "color": "rgba(0,153,255,.5)"
//  }, {
//    "text": "Foundation",
//    "value": 71829,
//    "color": "rgba(0,153,255,.5)"
//  }, {
//    "text": "A Short History Of Nearly Everything",
//    "value": 171661,
//    "color": "rgba(144,153,255,1)"
//  }, {
//    "text": "1984",
//    "value": 105477,
//    "color": "rgba(0,153,255,.5)"
//  }, {
//    "text": "The Passage",
//    "value": 333479,
//    "color": "rgba(0,153,255,.5)"
//  }].reverse();
//
  myarr = arr;

  createCircle(myarr, 50, 100)

  function calArcs(arr) {
    foo_arr = [];
    sum = 0;
    for (i = 0; i < arr.length; i++) {
      foo_arr[i] = (arr[i].value);
      sum += foo_arr[i];
    }
    arr = foo_arr;
    maxRad = 6.28319;
    gap = .1
    start = []
    stop = []
    max = Math.max.apply(Math, arr);
    min = Math.min.apply(Math, arr);

    if (max == min) {
      increments = (maxRad / arr.length);
      for (i = 0; i < arr.length; i++) {
        if (i === 0) {
          start[i] = 0 + gap / 2;
          stop[i] = increments - gap / 2;
        } else {
          start[i] = stop[i - 1] + gap;
          stop[i] = stop[i - 1] + increments;
        }
      }
      return [start, stop]
    } else {
      for (i = 0; i < arr.length; i++) {
        if (i === 0) {
          start[i] = 0 + gap / 2;
          stop[i] = maxRad * ((arr[i]) / (sum)) - gap / 2;
        } else {
          start[i] = stop[i - 1] + gap;
          stop[i] = stop[i - 1] + maxRad * ((arr[i]) / (sum));
        }
      }
      return [start, stop]
    }
  }

  function createCircle(myarr, inner, outer) {
    inner_radius = inner;
    outer_radius = outer;
    myarr = myarr;
    arcs = calArcs(myarr);
    startAngle = arcs[0];
    stopAngle = arcs[1];

    var tooltip = d3.select("body")
      .append("div")
      .style("position", "absolute")
      .style("z-index", "10")
      .style("visibility", "hidden")
      .style("color", "black")
      .style("font-size", "120%")
      .style("background", "rgba(255,255,255,0.6)")
      .style("border-radius", "10px");

    var svgContainer = bodySelection1.append("svg")
      .attr("width", 400)
      .attr("height", 375);

    var legend = svgContainer.append("g")
      .attr("height", 100)
      .attr("width", 100)
      .attr('transform', 'translate(-20,50)');

    var title = svgContainer.append("text")
        .attr("x", 200)
        .attr("y", 5)
        .style("text-anchor", "middle")
        .style("text-align","center")
        .attr('transform', 'translate(-20,50)')
        .style("font-size","18px")
        .text("Word Count");

    var circle = svgContainer.selectAll("path")
      .data(myarr)
      .enter()
      .append("path")
      .attr("d", d3.arc()
        .innerRadius(function(d, i) {
          return inner_radius;
        })
        .outerRadius(function(d, i) {
          return outer_radius;
        })
        .startAngle(function(d, i) {
          return startAngle[i]
        })
        .endAngle(function(d, i) {
          return stopAngle[i]
        })
      )
      .attr("transform", "translate(200,220)")
      .style("fill", function(d, i) {
        return d.color
      })
//      .on("click", function(d, i) {
//        alert(d);
//      })
      .on("mouseover", function(d, i) {
        d3.select(this).transition()
          .duration(500)
          .attr("d", d3.arc()
            .innerRadius(function(d) {
              return 1;
            })
            .outerRadius(function(d) {
              return outer_radius * 1.5;
            })
            .startAngle(function(d) {
              return startAngle[i]
            })
            .endAngle(function(d) {
              return stopAngle[i]
            })
          );
        tooltip.style("visibility", "visible");
        tooltip.html(d.text + "<br/>" + "Word Count: " + d.value);
      })
      .on("mousemove", function() {
        return tooltip.style("top", (event.pageY - 10) + "px").style("left", (event.pageX + 10) + "px");
      })
      .on("mouseout", function(d, i) {
        d3.select(this).transition()
          .duration(1000)
          .attr("d", d3.arc()
            .innerRadius(function(d) {
              return inner_radius;
            })
            .outerRadius(function(d) {
              return outer_radius;
            })
            .startAngle(function(d) {
              return startAngle[i]
            })
            .endAngle(function(d) {
              return stopAngle[i]
            })
          );
        tooltip.style("visibility", "hidden");
      });

    legend.selectAll('rect')
      .data(["Non-Fiction", "Fiction"])
      .enter()
      .append("rect")
      .attr("x", 20)
      .attr("y", function(d, i) {
        return 40 + 20 * (i + 1);
      })
      .attr("width", 10)
      .attr("height", 10)
      .style("fill", function(d, i) {
        if (i === 0) return "rgba(144,153,255,1)";
        else return "rgba(0,153,255,.5)"
      })

    legend.selectAll('text')
      .data(["Non-Fiction", "Fiction"])
      .enter()
      .append("text")
      .attr("x", 20 + 15)
      .attr("y", function(d, i) {
        return 50 + 20 * (i + 1);
      })
      .text(function(d, i) {
        return d;
      });
  }
}
