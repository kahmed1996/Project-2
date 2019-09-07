// Step 1: Set up our chart
//= ================================
var svgWidth = 960;
var svgHeight = 500;

var margin = {
  top: 20,
  right: 40,
  bottom: 60,
  left: 50
};

var width = svgWidth - margin.left - margin.right;
var height = svgHeight - margin.top - margin.bottom;

// Step 2: Create an SVG wrapper,
// append an SVG group that will hold our chart,
// and shift the latter by left and top margins.
// =================================
var svg = d3
  .select("body")
  .append("svg")
  .attr("width", svgWidth)
  .attr("height", svgHeight);

var chartGroup = svg.append("g")
  .attr("transform", `translate(${margin.left}, ${margin.top})`);

// Step 3:
// Import data from the Data.csv file
// =================================
d3.csv("Snow_Population1.csv", function(error, WeatherData) {
  console.log(WeatherData);
  if (error) throw error;

  // Step 4: Parse the data
  // Format the data and convert to numerical and date values
  // =================================
  // Create a function to parse date and time
  //var parseTime = d3.timeParse("%d-%b");
    var parseTime = d3.timeParse("%Y-%b");
 


  // Format the data
  WeatherData.forEach(function(data) {
    data.DATE = new Date(data.DATE);
    data.City = +data.City;
    data.Population = +data.Population;
    data.SNOW = +data.SNOW;
   
  });

  // Step 5: Create Scales
  //= ============================================
  var xTimeScale = d3.scaleTime()
    .domain(d3.extent(WeatherData, d => d.DATE))
    .range([0, width]);

  var yLinearScale1 = d3.scaleLinear()
    .domain([0, d3.max(WeatherData, d => d.City)])
    .range([height, 0]);

  var yLinearScale2 = d3.scaleLinear()
    .domain([0, d3.max(WeatherData, d => d.Population)])
    .range([height, 0]);

    var yLinearScale3= d3.scaleLinear()
    .domain([0, d3.max(WeatherData, d => d.SNOW)])
    .range([height, 0]);


  // Step 6: Create Axes
  // =============================================
  var bottomAxis = d3.axisBottom(xTimeScale).tickFormat(d3.timeFormat("%d-%b"));
  var leftAxis = d3.axisLeft(yLinearScale1);
  var rightAxis = d3.axisRight(yLinearScale2);


  // Step 7: Append the axes to the chartGroup
  // ==============================================
  // Add bottomAxis
  chartGroup.append("g").attr("transform", `translate(0, ${height})`).call(bottomAxis);

  // Add leftAxis to the left side of the display
  chartGroup.append("g").call(leftAxis);

  // Add rightAxis to the right side of the display
  chartGroup.append("g").attr("transform", `translate(${width}, 0)`).call(rightAxis);


  // Step 8: Set up two line generators and append two SVG paths
  // ==============================================
  // Line generators for each line
  var line1 = d3
    .line()
    .x(d => xTimeScale(d.DATE))
    .y(d => yLinearScale1(d.City));

  var line2 = d3
    .line()
    .x(d => xTimeScale(d.DATE))
    .y(d => yLinearScale2(d.Population));

    var line3 = d3
    .line()
    .x(d => xTimeScale(d.DATE))
    .y(d => yLinearScale3(d.SNOW));


  // Append a path for line1
  chartGroup.append("path")
    .data([WeatherData])
    .attr("d", line1)
    .classed("line green", true);

  // Append a path for line2
  chartGroup.append("path")
    .data([WeatherData])
    .attr("d", line2)
    .classed("line orange", true);

     // Append a path for line3
  chartGroup.append("path")
  .data([WeatherData])
  .attr("d", line3)
  .classed("line black", true);

});
