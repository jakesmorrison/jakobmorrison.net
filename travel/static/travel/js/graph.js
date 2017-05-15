var bodySelection1 = d3.select(".plot1");



myarr = [{"text":"Chase CSR","value": 20,"color":"blue"},
            {"text":"Amex Plat","value": 5,"color":"silver"},
            {"text":"Chase CSP","value": 50,"color":"blue"},
            {"text":"Discover IT","value": 25,"color":"orange"}]

createCircle(myarr,50,100)

function calArcs(arr) {
  foo_arr = [];
  for (i = 0; i < arr.length; i++) {
    foo_arr[i]=(arr[i].value);
  }
  arr=foo_arr;
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
  }
  else {
    for (i = 0; i < arr.length; i++) {
      if (i === 0) {
        start[i] = 0 + gap / 2;
        stop[i] = maxRad*((arr[i])/(100)) - gap / 2;
      }
      else{
        start[i] = stop[i - 1] + gap;
        stop[i] = stop[i - 1] + maxRad*((arr[i])/(100));
      }
    }
    return [start, stop]
  }
}


function createCircle(myarr,inner,outer) {
  inner_radius = inner;
  outer_radius = outer;
  myarr = myarr;
  arcs = calArcs(myarr);
  startAngle = arcs[0];
  stopAngle = arcs[1];

  var tooltip = d3.select("body")
	.append("div")
    .style("position","absolute")
    .style("z-index","10")
    .style("visibility","hidden")
    .style("color","black")
    .style("font-size","200%")
    .style("background","white");

  var svgContainer = bodySelection1.append("svg")
    .attr("width", 400)
    .attr("height", 400);

  svgContainer.append("text")
    .style("text-anchor", "middle")
    .text("jake");

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
    .attr("transform", "translate(200,200)")
    .style("fill", function(d,i){
      return d.color
    })
    .on("click", function(d, i) {
      alert(d);
    })
    .on("mouseover", function(d, i) {
        d3.select(this).transition()
          .duration(500)
          .attr("d", d3.arc()
            .innerRadius(function(d) {
              return 1;
            })
            .outerRadius(function(d) {
              return outer_radius*1.5;
            })
            .startAngle(function(d) {
              return startAngle[i]
            })
            .endAngle(function(d) {
              return stopAngle[i]
            })
          );
          tooltip.style("visibility", "visible");
          tooltip.text(d.text);
    })
  	.on("mousemove", function(){
      return tooltip.style("top", (event.pageY-10)+"px").style("left",(event.pageX+10)+"px");
    })
    .on("mouseout", function(d, i) {
        d3.select(this).transition()
          .duration(500)
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

}

