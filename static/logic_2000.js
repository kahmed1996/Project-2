// Create a map object
var myMap = L.map("map", {
    center: [37.09, -95.71],
    zoom: 5
  });
  
  L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
    attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
    maxZoom: 18,
    id: "mapbox.streets-basic",
    accessToken: API_KEY
  }).addTo(myMap);
  
  // Define a markerSize function that will give each city a different radius based on its population
  function markerSize(population) {
    return population / 40;
  }
  
  // Each city object contains the city's name, location and population
  var cities = [
        {
      name: "Anchorage",
      location: [61.17755, -149.274],
      population: 260283,
      snow:"true"
    },
  
  {
      name: "Phoenix",
      location: [33.57216, -112.088],
      population: 1321045,
      snow:"false"
    },
  
  {
      name: "Los Angeles",
      location: [34.01939, -118.411],
      population: 3694820,
      snow:"false"
    },
  
  {
      name: "San Diego",
      location: [32.8153, -117.135],
      population: 1223400,
      snow:"false"
    },
  
  {
      name: "Miami",
      location: [25.77516, -80.2086],
      population: 362470,
      snow:"false"
    },
  
  {
      name: "Atlanta",
      location: [33.76291, -84.4227],
      population: 416474,
      snow:"false"
    },
  
  {
      name: "Honolulu",
      location: [21.32585, -157.845],
      population: 371657,
      snow:"false"
    },
  
  {
      name: "Chicago",
      location: [41.83755, -87.6818],
      population: 2896016,
      snow:"true"
    },
  
  {
      name: "Fort Wayne",
      location: [41.08817, -85.1439],
      population: 205727,
      snow:"true"
    },
  
  {
      name: "Louisville",
      location: [38.17808, -85.6667],
      population: 256231,
      snow:"true"
    },
  
  {
      name: "Detroit",
      location: [42.38304, -83.1022],
      population: 951270,
      snow:"true"
    },
  
  {
      name: "Minneapolis",
      location: [44.96332, -93.2683],
      population: 382618,
      snow:"true"
    },
  
  {
      name: "New York City",
      location: [40.66427, -73.9385],
      population: 8008278,
      snow:"true"
    },
  
  {
      name: "Cleveland",
      location: [41.47814, -81.6795],
      population: 478403,
      snow:"true"
    },
  
  {
      name: "Nashville",
      location: [36.1718, -86.785],
      population: 545524,
      snow:"false"
    },
  
  {
      name: "Corpus Christi",
      location: [27.80455, -97.3963],
      population: 277454,
      snow:"false"
    },
  
  {
      name: "Houston",
      location: [29.78047, -95.3863],
      population: 1953631,
      snow:"false"
    },
  
  {
      name: "Las Vegas",
      location: [36.0719, -115.1634],
      population: 478434,
      snow:"false"
    },
  
  ];
  
  // Loop through the cities array and create one marker for each city object
  for (var i = 0; i < cities.length; i++) {
  
    var sunicon = L.icon({
      iconUrl:'./static/Sun_icon.png',
      // Setting our circle's radius equal to the output of our markerSize function
      // This will make our marker's size proportionate to its population
      iconSize:[(cities[i].population)/40000,(cities[i].population)/40000],
    }
    );
    var snowicon = L.icon({
      iconUrl:'./static/HieloSnowflake.png',
      // Setting our circle's radius equal to the output of our markerSize function
      // This will make our marker's size proportionate to its population
      iconSize:[(cities[i].population)/40000,(cities[i].population)/40000],
    }
    );
      if (cities[i].snow == "false")
          {icon=sunicon;}
      else {icon=snowicon;}
    L.marker(cities[i].location, {icon: icon}).bindPopup("<h1>" + cities[i].name + "</h1> <hr> <h3>Population: " + cities[i].population + "</h3>").addTo(myMap);
  
  }