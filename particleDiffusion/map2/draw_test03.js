//alert("aa");
function initialize(_width, _height) {
    var margin = {top: 20, right: 20, bottom: 30, left: 40},
        width = _width - margin.left - margin.right,
        height = _height - margin.top - margin.bottom;
    var svg = d3.select("#d3js").append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");
 
/*
    var svg = d3.select("#d3js").append("svg")
        .attr("width", width)
        .attr("height", height);
*/
}

function test(map, pri_map, width, height) {
    var svg = d3.select("#d3js").select("svg"); 
    console.log(pri_map);
    console.log(map);
    var xScale = d3.scale.linear()
        .domain([-20,20])
        .range([0,width]);
    
    var yScale = d3.scale.linear()
        .domain([-20,20])
        .range([height,0]);
 
    // 軸を設定する。
    var xAxis = d3.svg.axis()
        .scale(xScale)
        .orient("bottom")
        .tickSize(6, -height); // 棒の長さと方向。
        //.tickFormat(function(d){ return d+"年"; }); // 数字に年をつけている。
 
    var yAxis = d3.svg.axis()
        .ticks(5) // 軸のチックの数。
        .scale(yScale)
        .orient("left")
        .tickSize(6, -width);

    //var testDat = [3, 1, 2, 3, 4, 8,9, -3];
    //console.log(map);
    //console.log(xScale(2) + "," + yScale(2));
    var dots;
    if (pri_map == null) {
        svg.selectAll("circle").data(map)
            .enter()
            .append("circle")
            .attr("r",10)
            .attr("fill", "black")
            .attr("id", function(d) { return "#" + String(d.vehicleId);})
            .attr("cx", function(d) { return yScale(d.pos[0]);})
            .attr("cy", function(d) { return yScale(d.pos[1]);})

    } else {
        var dots = svg.selectAll("circle");
        dots.transition()
            .duration(1000)
            .attr("r",10)
            .attr("fill", "black")
            .attr("cx", function(d) {
                for (var i =0; i < map.length; i++) {
                    console.log(d.vehicleId + ":::" + "#" +String(map[i].vehicleId));
                    if (map[i].vehicleId == d.vehicleId) {
                        return yScale(map[i].pos[0]);
                    }
                }
            })
            .attr("cy", function(d) { 
                for (var i =0; i < map.length; i++) {
                    console.log(d.vehicleId + ":::" + "#" +String(map[i].vehicleId));
                    if (map[i].vehicleId == d.vehicleId) {
                        return yScale(map[i].pos[1]);
                    }
                }
            });

    }
    //.dots.transition()
    //      .duration(1000)
    //    .attr("cx", function(d, i) { 
    //      console.log(d);
    //console.log(xScale(d[0]) + "," + yScale(d));
    //console.log(xScale(d["pos"][0]) + "," + yScale(d["pos"][1]));
    //        return xScale(d.pos[0]);})
    //.attr("cy", function(d) { return yScale(d.pos[1]);});

/*
    var dots = null;
    if (updateflag != null) {
        var dots = svg.selectAll("circle")
            .data(pri_map)
            .enter()
            .append("circle")
            .attr("r",10)
            .attr("fill", "black")
            .attr("cx", function(d) { 
                console.log(d);
                //console.log(xScale(d[0]) + "," + yScale(d));
                //console.log(xScale(d["pos"][0]) + "," + yScale(d["pos"][1]));
                return xScale(d.pos[0]);})
            .attr("cy", function(d) { return yScale(d.pos[1]);});
    }
    

    dots.transition()
        .duration(1000)
        .data(map)
        .attr("cx", function(d) { 
            console.log(d);
            //console.log(xScale(d[0]) + "," + yScale(d));
            //console.log(xScale(d["pos"][0]) + "," + yScale(d["pos"][1]));
            return xScale(d.pos[0]);})
        .attr("cy", function(d) { return yScale(d.pos[1]);});
*/

//        .attr("cx", function(d){ return xScale(d["年"]); })
//        .attr("cy", function(d){ return yScale(d["gdp"]); });



    svg.append("g")
        .attr("class", "y axis")
        .call(yAxis)
        .append("text")
        .attr("y", -10)
        .attr("x",10)
        .style("text-anchor", "end")
        .text("GDP");

/*
    svg.append("g")
        .attr("class", "x axis")
        .attr("transform", "translate(0," + height + ")")
        .call(xAxis);
*/
};
