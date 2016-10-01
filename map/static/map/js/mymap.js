var geocoder;
var map;

var map, mapOptions, currentLocation, currentLocationMarker;

function loadMapScript() {
  var script = document.createElement("script");
  script.type = "text/javascript";
  script.id = "googleMaps"
  script.src = "https://maps.googleapis.com/maps/api/js?key=AIzaSyBUBP8yy2VTKSfllFyMKmh89_e5PiTCUo0&callback=initMap";
  document.body.appendChild(script);
}

var my_locations = {
	"home": {"lat": 43.5734736,"lng": -116.4817242, "number": 1},
	"boi": {"lat": 43.5658231,"lng": -116.222316},
	"pdx": {"lat": 45.58976939999999,"lng": -122.5950942},
	"sfo": {"lat": 37.6213129,"lng": -122.3789554},
};

// Shapes define the clickable region of the icon. The type defines an HTML
// <area> element 'poly' which traces out a polygon as a series of X,Y points.
// The final coordinate closes the poly by connecting to the first coordinate.
var shape = {
  coords: [1, 1, 1, 20, 18, 20, 18, 1],
  type: 'poly'
};

var pathOptions_flight = {
    geodesic: true,
    strokeColor: 'blue',
    strokeOpacity: 1.0,
    strokeWeight: 2
};


function initMap() {
    var map = new google.maps.Map(document.getElementById('map'), {
      zoom: 6,
      center: {lat: 42.177388, lng: -119.8985576},
      styles: [
            {elementType: 'geometry', stylers: [{color: '#242f3e'}]},
            {elementType: 'labels.text.stroke', stylers: [{color: '#242f3e'}]},
            {elementType: 'labels.text.fill', stylers: [{color: '#746855'}]},
            {
              featureType: 'administrative.locality',
              elementType: 'labels.text.fill',
              stylers: [{color: '#d59563'}]
            },
            {
              featureType: 'poi',
              elementType: 'labels.text.fill',
              stylers: [{color: '#d59563'}]
            },
            {
              featureType: 'poi.park',
              elementType: 'geometry',
              stylers: [{color: '#263c3f'}]
            },
            {
              featureType: 'poi.park',
              elementType: 'labels.text.fill',
              stylers: [{color: '#6b9a76'}]
            },
            {
              featureType: 'road',
              elementType: 'geometry',
              stylers: [{color: '#38414e'}]
            },
            {
              featureType: 'road',
              elementType: 'geometry.stroke',
              stylers: [{color: '#212a37'}]
            },
            {
              featureType: 'road',
              elementType: 'labels.text.fill',
              stylers: [{color: '#9ca5b3'}]
            },
            {
              featureType: 'road.highway',
              elementType: 'geometry',
              stylers: [{color: '#746855'}]
            },
            {
              featureType: 'road.highway',
              elementType: 'geometry.stroke',
              stylers: [{color: '#1f2835'}]
            },
            {
              featureType: 'road.highway',
              elementType: 'labels.text.fill',
              stylers: [{color: '#f3d19c'}]
            },
            {
              featureType: 'transit',
              elementType: 'geometry',
              stylers: [{color: '#2f3948'}]
            },
            {
              featureType: 'transit.station',
              elementType: 'labels.text.fill',
              stylers: [{color: '#d59563'}]
            },
            {
              featureType: 'water',
              elementType: 'geometry',
              stylers: [{color: '#17263c'}]
            },
            {
              featureType: 'water',
              elementType: 'labels.text.fill',
              stylers: [{color: '#515c6d'}]
            },
            {
              featureType: 'water',
              elementType: 'labels.text.stroke',
              stylers: [{color: '#17263c'}]
            }
          ]
    });

    var marker_1 = new google.maps.Marker({
        position: {lat: my_locations["home"]["lat"], lng: my_locations["home"]["lng"]},
        map: map,
        shape: shape,
        title: "Home",
        animation: google.maps.Animation.BOUNCE,
        icon: marker_a,
        zIndex: my_locations["home"]["number"]
    });

    marker_1.addListener('click', function() {
        $("#mypage").show();
        $('.heading-1').html('Home');
        $('.def-loc').html('Location: Nampa, Idaho');
        $('.def-date').html('Date: 10/05/2016');

        $('#mycontent').html(`
             <div class="row">
                <div class="col-md-10 col-md-offset-1">
                    <h4>Where am I going?</h4>
                    <hr>
                    <p class="paragraph-font">I purchased a one way, first class ticket to Bangkok Thailand. The first class part is important; I am going to be a king at 30,000 feet. In all honesty it could very well be the highlight of the trip. I will be flying Korean Air from San Fran to Seoul. I have a brief 5 day stopover in Seoul before I contiue to Bangkok. After that the details get fuzzy.</p>
                </div>
             </div>
            <br>
            <div class="row">
            <div class="col-md-4 col-md-offset-1">
                <img src="https://www.micron.com/~/media/track-2-images/media-kit/high_res_hmc.jpg?la=en" class="picture-resize" style="height:300px;width:350px;">
            </div>
            <div class="col-md-6">
                <h4>How did I get here?</h4>
                <hr>
                <p class="paragraph-font">I was at Micron for over 3 years, and I enjoyed every bit of it. I worked on commodity DRAM when I first started. After a year or so our team was move over to HMC (a new, high bandwidth, specialty DRAM). HMC was the highlight of my time at Micron. The learning curve was steep, and the pace was fast, but I wouldn’t have wanted to work on anything else.</p>
                <p class="paragraph-font">In mid June Micron announced layoffs would be happening at the end of the month. Before the involuntary layoffs began they asked specific Micron locations for volunteers. Boise was one of the locations. Certain projects were canceled, and now seemed like an opportune time to make a change. I took the voluntary layoff and left Micron on September 1st 2016. </p>
            </div>
            </div>
            <br>
            `);
    });

    var marker_2 = new google.maps.Marker({
        position: {lat: my_locations["boi"]["lat"], lng: my_locations["boi"]["lng"]},
        map: map,
        shape: shape,
        title: "BOI Airport",
        icon: "http://chart.apis.google.com/chart?chst=d_map_pin_letter&chld=B|0000FF|FFFFFF",
        zIndex: my_locations["boi"]["number"]
      });
    marker_2.addListener('click', function() {
        $("#mypage").show();
        $('.heading-1').html('BOI Airport');
        $('.def-loc').html('Location: Boise, Idaho');
        $('.def-date').html('Date: 10/05/2016');
        $('#mycontent').html(`
            <div class="col-md-4 col-md-offset-1">
                <img src="https://www.instagram.com/p/BKlni6zgVzo/media/?size=m" class="picture-resize">
            </div>
            <div class="col-md-6">
                <p class="paragraph-font">To the left you see my baby, my prince, and what I am going to miss more than anything.</p>
            </div>
            `);
    });

    var marker1_to_2 = [{'lng': -116.4816, 'lat': 43.57329}, {'lng': -116.48205, 'lat': 43.5733}, {'lng': -116.48228, 'lat': 43.57327}, {'lng': -116.48364, 'lat': 43.57253}, {'lng': -116.48364, 'lat': 43.57419}, {'lng': -116.4836, 'lat': 43.57586}, {'lng': -116.4796, 'lat': 43.57582}, {'lng': -116.47356, 'lat': 43.57577}, {'lng': -116.47263, 'lat': 43.57577}, {'lng': -116.46432, 'lat': 43.57575}, {'lng': -116.45367, 'lat': 43.57573}, {'lng': -116.43473, 'lat': 43.5757}, {'lng': -116.43458, 'lat': 43.57568}, {'lng': -116.43426, 'lat': 43.57568}, {'lng': -116.43377, 'lat': 43.57567}, {'lng': -116.43377, 'lat': 43.57574}, {'lng': -116.43378, 'lat': 43.57635}, {'lng': -116.4338, 'lat': 43.58217}, {'lng': -116.43379, 'lat': 43.58494}, {'lng': -116.43376, 'lat': 43.58674}, {'lng': -116.43375, 'lat': 43.58745}, {'lng': -116.43368, 'lat': 43.58756}, {'lng': -116.43367, 'lat': 43.58883}, {'lng': -116.43368, 'lat': 43.58931}, {'lng': -116.43369, 'lat': 43.58948}, {'lng': -116.43377, 'lat': 43.59002}, {'lng': -116.43384, 'lat': 43.59073}, {'lng': -116.43392, 'lat': 43.59156}, {'lng': -116.43391, 'lat': 43.5922}, {'lng': -116.43391, 'lat': 43.59249}, {'lng': -116.43386, 'lat': 43.59253}, {'lng': -116.43382, 'lat': 43.59257}, {'lng': -116.43369, 'lat': 43.59271}, {'lng': -116.43352, 'lat': 43.59277}, {'lng': -116.43301, 'lat': 43.59281}, {'lng': -116.43288, 'lat': 43.59284}, {'lng': -116.43233, 'lat': 43.59288}, {'lng': -116.43073, 'lat': 43.59302}, {'lng': -116.42955, 'lat': 43.59311}, {'lng': -116.42849, 'lat': 43.59317}, {'lng': -116.42756, 'lat': 43.59319}, {'lng': -116.4199, 'lat': 43.59327}, {'lng': -116.41985, 'lat': 43.59328}, {'lng': -116.41958, 'lat': 43.59335}, {'lng': -116.41762, 'lat': 43.59335}, {'lng': -116.4137, 'lat': 43.59336}, {'lng': -116.41343, 'lat': 43.59336}, {'lng': -116.40049, 'lat': 43.59338}, {'lng': -116.39645, 'lat': 43.59334}, {'lng': -116.3945, 'lat': 43.59331}, {'lng': -116.39265, 'lat': 43.59331}, {'lng': -116.38841, 'lat': 43.59338}, {'lng': -116.3863, 'lat': 43.59338}, {'lng': -116.38062, 'lat': 43.59338}, {'lng': -116.37453, 'lat': 43.59338}, {'lng': -116.37134, 'lat': 43.59338}, {'lng': -116.36948, 'lat': 43.59342}, {'lng': -116.36731, 'lat': 43.59358}, {'lng': -116.36587, 'lat': 43.59372}, {'lng': -116.36398, 'lat': 43.59398}, {'lng': -116.36178, 'lat': 43.59439}, {'lng': -116.35967, 'lat': 43.59489}, {'lng': -116.35857, 'lat': 43.59518}, {'lng': -116.35738, 'lat': 43.59554}, {'lng': -116.35641, 'lat': 43.59581}, {'lng': -116.35587, 'lat': 43.59597}, {'lng': -116.35476, 'lat': 43.59627}, {'lng': -116.35413, 'lat': 43.59641}, {'lng': -116.35297, 'lat': 43.59665}, {'lng': -116.35191, 'lat': 43.59682}, {'lng': -116.34996, 'lat': 43.59706}, {'lng': -116.34896, 'lat': 43.59712}, {'lng': -116.34802, 'lat': 43.59717}, {'lng': -116.34217, 'lat': 43.59718}, {'lng': -116.33435, 'lat': 43.59717}, {'lng': -116.30208, 'lat': 43.59716}, {'lng': -116.29795, 'lat': 43.59713}, {'lng': -116.29613, 'lat': 43.59711}, {'lng': -116.29443, 'lat': 43.59703}, {'lng': -116.2941, 'lat': 43.59697}, {'lng': -116.29228, 'lat': 43.59679}, {'lng': -116.29144, 'lat': 43.59668}, {'lng': -116.29072, 'lat': 43.59656}, {'lng': -116.2897, 'lat': 43.59636}, {'lng': -116.28871, 'lat': 43.59612}, {'lng': -116.28495, 'lat': 43.59509}, {'lng': -116.28414, 'lat': 43.59483}, {'lng': -116.28352, 'lat': 43.59458}, {'lng': -116.28308, 'lat': 43.59436}, {'lng': -116.27976, 'lat': 43.59275}, {'lng': -116.27915, 'lat': 43.59241}, {'lng': -116.27503, 'lat': 43.59042}, {'lng': -116.27085, 'lat': 43.58842}, {'lng': -116.26862, 'lat': 43.58736}, {'lng': -116.26622, 'lat': 43.58621}, {'lng': -116.26099, 'lat': 43.58367}, {'lng': -116.253, 'lat': 43.57982}, {'lng': -116.24951, 'lat': 43.57813}, {'lng': -116.24409, 'lat': 43.57549}, {'lng': -116.23795, 'lat': 43.57258}, {'lng': -116.23734, 'lat': 43.57239}, {'lng': -116.23656, 'lat': 43.57218}, {'lng': -116.23607, 'lat': 43.57209}, {'lng': -116.23556, 'lat': 43.57202}, {'lng': -116.23458, 'lat': 43.57194}, {'lng': -116.2337, 'lat': 43.57192}, {'lng': -116.23225, 'lat': 43.57192}, {'lng': -116.22395, 'lat': 43.57197}, {'lng': -116.22194, 'lat': 43.57196}, {'lng': -116.22124, 'lat': 43.57193}, {'lng': -116.22021, 'lat': 43.57188}, {'lng': -116.2196, 'lat': 43.57183}, {'lng': -116.21952, 'lat': 43.57173}, {'lng': -116.21938, 'lat': 43.57169}, {'lng': -116.21896, 'lat': 43.57162}, {'lng': -116.21829, 'lat': 43.57147}, {'lng': -116.21617, 'lat': 43.57085}, {'lng': -116.21604, 'lat': 43.5708}, {'lng': -116.21593, 'lat': 43.57073}, {'lng': -116.21583, 'lat': 43.57065}, {'lng': -116.2159, 'lat': 43.57053}, {'lng': -116.21612, 'lat': 43.57027}, {'lng': -116.21646, 'lat': 43.57}, {'lng': -116.21673, 'lat': 43.56982}, {'lng': -116.21692, 'lat': 43.56974}, {'lng': -116.21714, 'lat': 43.56968}, {'lng': -116.21722, 'lat': 43.56966}, {'lng': -116.21747, 'lat': 43.56961}, {'lng': -116.21774, 'lat': 43.56959}, {'lng': -116.21797, 'lat': 43.56962}, {'lng': -116.21816, 'lat': 43.56967}, {'lng': -116.21836, 'lat': 43.56974}, {'lng': -116.21853, 'lat': 43.56983}, {'lng': -116.21863, 'lat': 43.5699}, {'lng': -116.21897, 'lat': 43.57029}, {'lng': -116.21927, 'lat': 43.57059}, {'lng': -116.21951, 'lat': 43.57072}, {'lng': -116.21972, 'lat': 43.5708}, {'lng': -116.22006, 'lat': 43.57086}, {'lng': -116.22264, 'lat': 43.57098}]
    var drive_path = new google.maps.Polyline({
              path: marker1_to_2,
              geodesic: true,
              strokeColor: '#FF0000',
              strokeOpacity: 1.0,
              strokeWeight: 2
    });
    drive_path.setMap(map);

    var marker_3 = new google.maps.Marker({
        position: {lat: my_locations["pdx"]["lat"], lng: my_locations["pdx"]["lng"]},
        map: map,
        shape: shape,
        title: "PDX Airport",
        icon: "http://chart.apis.google.com/chart?chst=d_map_pin_letter&chld=C|0000FF|FFFFFF",
        zIndex: my_locations["pdx"]["number"]
      });
    marker_3.addListener('click', function() {
        $("#mypage").show();
        $('.heading-1').html('PDX Airport');
        $('.def-loc').html('Location: Portland, Oregon');
        $('.def-date').html('Date: 10/05/2016');
        $('#mycontent').html(`
            <div class="col-md-6 col-md-offset-3">
                <p class="paragraph-font">Layover in Portland. Nothing exciting. Move on to San Fran and the greatest lounge on Earth.</p>
            </div>
            `);
    });
    var path = new google.maps.Polyline(pathOptions_flight);
    var start_point = new google.maps.LatLng(my_locations["boi"]["lat"], my_locations["boi"]["lng"]);
    var end_point = new google.maps.LatLng(my_locations["pdx"]["lat"], my_locations["pdx"]["lng"]);
    path.getPath().setAt(0, start_point);
    path.getPath().setAt(1, end_point);
    path.setMap(map);

    var marker_4 = new google.maps.Marker({
        position: {lat: my_locations["sfo"]["lat"], lng: my_locations["sfo"]["lng"]},
        map: map,
        shape: shape,
        title: "SFO Airport",
        icon: "http://chart.apis.google.com/chart?chst=d_map_pin_letter&chld=D|0000FF|FFFFFF",
        zIndex: my_locations["sfo"]["number"]
      });
    marker_4.addListener('click', function() {
        $("#mypage").show();
        $('.heading-1').html('SFO Airport');
        $('.def-loc').html('Location: San Francisco, California');
        $('.def-date').html('Date: 10/05/2016');
        $('#mycontent').html(`
            <div class="col-md-4 col-md-offset-1">
                <img src="#" class="picture-resize">
            </div>
            <div class="col-md-6">
                <p class="paragraph-font">Some Text Here</p>
            </div>
            `);
    });
    var path = new google.maps.Polyline(pathOptions_flight);
    var start_point = new google.maps.LatLng(my_locations["pdx"]["lat"], my_locations["pdx"]["lng"]);
    var end_point = new google.maps.LatLng(my_locations["sfo"]["lat"], my_locations["sfo"]["lng"]);
    path.getPath().setAt(0, start_point);
    path.getPath().setAt(1, end_point);
    path.setMap(map);
}


//var beaches = [
//    ['Bondi Beach', -33.890542, 151.274856, 4],
//    ['Coogee Beach', -33.923036, 151.259052, 5],
//    ['Cronulla Beach', -34.028249, 151.157507, 3],
//    ['Manly Beach', -33.80010128657071, 151.28747820854187, 2],
//    ['Maroubra Beach', -33.950198, 151.259302, 1]
//];
//
//var locations = ['7216 Lima Drive Nampa, ID, 83687']
//
//function initMap() {
//    var map = new google.maps.Map(document.getElementById('map'), {
//      zoom: 10,
//      center: {lat: -33.9, lng: 151.2}
//    });
//    setMarkers(map);
//    plane_connect(map);
////    var geocoder = new google.maps.Geocoder();
//}
//
//function setMarkers(map) {
//    var shape = {
//      coords: [1, 1, 1, 20, 18, 20, 18, 1],
//      type: 'poly'
//    };
//    for (var i = 0; i < beaches.length; i++) {
//      var beach = beaches[i];
//      var marker = new google.maps.Marker({
//        position: {lat: beach[1], lng: beach[2]},
//        map: map,
//        shape: shape,
//        title: beach[0],
//        zIndex: beach[3]
//      });
//    }
//}
//
//function plane_connect(map){
//    var flightPlanCoordinates = [
//      {lat: -33.890542, lng: 151.274856},
//      {lat: -33.950198, lng: 151.259302}
//    ];
//    var flightPath = new google.maps.Polyline({
//      path: flightPlanCoordinates,
//      geodesic: true,
//      strokeColor: '#FF0000',
//      strokeOpacity: 1.0,
//      strokeWeight: 2
//    });
//    flightPath.setMap(map);
//}

//function geocodeAddress(geocoder, address, myCallback) {
//    var address = address;
//    var latLng = '';
//    geocoder.geocode({'address': address}, function(results, status) {
//      if (status === 'OK') {
//        myCallback(results[0].geometry.location);
//      }
//      else {
//        alert('Geocode was not successful for the following reason: ' + status);
//      }
//    });
//}



