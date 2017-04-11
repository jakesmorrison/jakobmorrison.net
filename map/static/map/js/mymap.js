var map;
var geocoder;
var locationDictionary;
var longLat = [];

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

function create_map(lD){
    locationDictionary = lD;
    var script = document.createElement("script");
    script.type = "text/javascript";
    script.id = "googleMaps"
    script.src = "https://maps.googleapis.com/maps/api/js?key=AIzaSyBUBP8yy2VTKSfllFyMKmh89_e5PiTCUo0&callback=init_map";
    document.body.appendChild(script);
}

function init_map() {
    map = new google.maps.Map(document.getElementById('map'), {
      zoom: 3,
      center: {lat: 40, lng: 180},
    });
    for(i=0; i<locationDictionary.length; i++){
        add_marker(locationDictionary[i]["long"],locationDictionary[i]["lat"],locationDictionary[i]["label"],locationDictionary[i]["index"])
    }

};

function add_marker(long,lat,label,index){
    var marker = new google.maps.Marker({
        position: {lat: lat, lng: long},
        map: map,
        title: label,
        label: {
            text: (index+1).toString(),
            color: 'black',
        },
        zIndex: 1
    });
}
// Promises Example Dont Delete

//var geocoder = new google.maps.Geocoder();
//for(i=0; i<locationDictionary.length; i++){
//    $.when(geocodeAddress(geocoder,locationDictionary[i]["location"],i)).done(
//    function(data){
//        lat = data["lat"];
//        long = data["long"];
//        index = data["index"];
//        add_marker(long,lat,locationDictionary[index]["label"],index);
//    })
//}


//function geocodeAddress(geocoder, address, index) {
//    var deferred = $.Deferred();
//    geocoder.geocode( { 'address': address}, function(results, status) {
//        if (status == google.maps.GeocoderStatus.OK) {
//            var latitude = results[0].geometry.location.lat();
//            var longitude = results[0].geometry.location.lng();
//            console.log(locationDictionary[index]["label"]);
//            deferred.resolve({"long": results[0].geometry.location.lng(), "lat":results[0].geometry.location.lat(),"index":index});
//        }
//        else{
//            console.log(status);
//        }
//    });
//    return deferred.promise();
//}



//
//var my_locations = {
//	"home": {"lat": 43.5734736,"lng": -116.4817242, "number": 1},
//	"boi": {"lat": 43.5658231,"lng": -116.222316},
//	"pdx": {"lat": 45.58976939999999,"lng": -122.5950942},
//	"sfo": {"lat": 37.6213129,"lng": -122.3789554},
//	"icn": {"lat": 37.4601908,"lng": 126.438507},
//	"hos1": {"lat": 37.523839,"lng": 126.8890157},
//    "bkk": {"lat": 13.690022,"lng": 100.6931919},
//};
//
//
//var pathOptions_flight = {
//    geodesic: true,
//    strokeColor: 'blue',
//    strokeOpacity: 1.0,
//    strokeWeight: 2
//};
//
//function initMap() {
//    var map = new google.maps.Map(document.getElementById('map'), {
//      zoom: 10,
//      center: {lat: 37.5319765, lng: 126.7224727},
////      styles: [
////            {elementType: 'geometry', stylers: [{color: '#242f3e'}]},
////            {elementType: 'labels.text.stroke', stylers: [{color: '#242f3e'}]},
////            {elementType: 'labels.text.fill', stylers: [{color: '#746855'}]},
////            {
////              featureType: 'administrative.locality',
////              elementType: 'labels.text.fill',
////              stylers: [{color: '#d59563'}]
////            },
////            {
////              featureType: 'poi',
////              elementType: 'labels.text.fill',
////              stylers: [{color: '#d59563'}]
////            },
////            {
////              featureType: 'poi.park',
////              elementType: 'geometry',
////              stylers: [{color: '#263c3f'}]
////            },
////            {
////              featureType: 'poi.park',
////              elementType: 'labels.text.fill',
////              stylers: [{color: '#6b9a76'}]
////            },
////            {
////              featureType: 'road',
////              elementType: 'geometry',
////              stylers: [{color: '#38414e'}]
////            },
////            {
////              featureType: 'road',
////              elementType: 'geometry.stroke',
////              stylers: [{color: '#212a37'}]
////            },
////            {
////              featureType: 'road',
////              elementType: 'labels.text.fill',
////              stylers: [{color: '#9ca5b3'}]
////            },
////            {
////              featureType: 'road.highway',
////              elementType: 'geometry',
////              stylers: [{color: '#746855'}]
////            },
////            {
////              featureType: 'road.highway',
////              elementType: 'geometry.stroke',
////              stylers: [{color: '#1f2835'}]
////            },
////            {
////              featureType: 'road.highway',
////              elementType: 'labels.text.fill',
////              stylers: [{color: '#f3d19c'}]
////            },
////            {
////              featureType: 'transit',
////              elementType: 'geometry',
////              stylers: [{color: '#2f3948'}]
////            },
////            {
////              featureType: 'transit.station',
////              elementType: 'labels.text.fill',
////              stylers: [{color: '#d59563'}]
////            },
////            {
////              featureType: 'water',
////              elementType: 'geometry',
////              stylers: [{color: '#17263c'}]
////            },
////            {
////              featureType: 'water',
////              elementType: 'labels.text.fill',
////              stylers: [{color: '#515c6d'}]
////            },
////            {
////              featureType: 'water',
////              elementType: 'labels.text.stroke',
////              stylers: [{color: '#17263c'}]
////            }
////          ]
//    });
//
//    var marker_1 = new google.maps.Marker({
//        position: {lat: my_locations["home"]["lat"], lng: my_locations["home"]["lng"]},
//        map: map,
//        shape: shape,
//        title: "Home",
//        animation: google.maps.Animation.DROP,
//        icon: marker_a,
//        zIndex: my_locations["home"]["number"]
//    });
//
//    marker_1.addListener('click', function() {
//        $("#mypage").show();
//        $('.heading-1').html('Home');
//        $('.def-loc').html(' <i class="fa fa-location-arrow" aria-hidden="true"></i> Nampa, Idaho');
//        $('.def-date').html('<i class="fa fa-calendar" aria-hidden="true"></i> 10/05/2016');
//
//        $('#mycontent').html(`
//             <div class="row">
//                <div class="col-md-10 col-md-offset-1 col-xs-10 col-xs-offset-1">
//                    <h4 class="heading-4">What am I doing?</h4>
//                    <hr>
//                    <p class="paragraph-font">I purchased a one way, first class ticket to Bangkok Thailand. The first class part is important; I am going to be a king at 30,000 feet. In all honesty it could very well be the highlight of the trip. I will be flying Korean Air from San Fran to Seoul. I have a brief 5 day stopover in Seoul before I contiue to Bangkok. After that the details get fuzzy.</p>
//                </div>
//             </div>
//            <br>
//            <div class="row">
//                <h4 class="heading-4">How did I get to this point?</h4>
//                <hr>
//                <div class="col-md-6 col-xs-10 col-xs-offset-1">
//                    <p class="paragraph-font">I was at Micron for over 3 years. I worked on commodity DRAM when I first started. After a year or so our team was moved over to HMC (a new, high bandwidth, specialty DRAM). HMC was the highlight of my time at Micron. The learning curve was steep, and the pace was fast, but I wouldn’t have wanted to work on anything else.</p>
//                    <p class="paragraph-font">In mid June Micron announced layoffs would be happening at the end of the month. Before the involuntary layoffs began they asked specific Micron locations for volunteers. Boise was one of the locations. My project was canceled the day before the layoffs were announced, so now seemed like an opportune time to make a change. I took the voluntary layoff and left Micron on September 1st 2016. </p>
//                </div>
//                <div class="col-md-4 col-md-offset-0 col-xs-10 col-xs-offset-1">
//                    <img src="https://www.micron.com/~/media/track-2-images/media-kit/high_res_hmc.jpg?la=en" class="picture-resize" style="width:300px;">
//                </div>
//            </div>
//            <br>
//            `);
//    });
//
//    var marker_2 = new google.maps.Marker({
//        position: {lat: my_locations["boi"]["lat"], lng: my_locations["boi"]["lng"]},
//        map: map,
//        shape: shape,
//        title: "BOI Airport",
//        animation: google.maps.Animation.DROP,
//        icon: marker_b,
//        zIndex: my_locations["boi"]["number"]
//      });
//    marker_2.addListener('click', function() {
//        $("#mypage").show();
//        $('.heading-1').html('BOI Airport');
//        $('.def-loc').html(' <i class="fa fa-location-arrow" aria-hidden="true"></i> Boise, Idaho');
//        $('.def-date').html('<i class="fa fa-calendar" aria-hidden="true"></i> 10/05/2016');
//        $('#mycontent').html(`
//            <div class="row">
//                <h4 class="heading-4">Beginning</h4>
//                <hr>
//                <div class="col-md-6 col-xs-10 col-xs-offset-1">
//                    <p class="paragraph-font"><b>Quick flight to Portland. A few things of note.</b></p>
//                    <ul>
//                        <li><p class="paragraph-font">Samsung Galaxy S7s are not allowed to be powered on or plugged in during flights.</p></li>
//                        <li><p class="paragraph-font">I listened to the first episode of a new podcast called, "Buffering the Vampire Slayer". For those of you who are out of the loop this is a, "Buffy the Vampire Slayer" rewatch podcast. I would like to put a friend of mine on a brief early morning blast. She laughed and called me a dork for listening to this podcast. Well let me just say you are wrong and Buffy is awesome. I am sure she will eat her words after I tell her the podcast was entertaining, and will probably provoke me to start rewatching Buffy again.</p></li>
//                        <li><p class="paragraph-font">New idea! Instead of a travel blog how about I alternatively write a review/analysis blog about my experience listening to a podcast about two people reviewing/analyzing "Buffy the Vampire Slayer". If I were in the blog game for the clicks I would absolutely do that. Nothing is hotter right now than powerful women, vampires and late 90s nostalgia. </p></li>
//                    </ul>
//                </div>
//                <div class="col-md-4 col-md-offset-0 col-xs-10 col-xs-offset-1">
//                    <img src="http://ist3-2.filesor.com/pimpandhost.com/1/1/2/0/112024/3/i/L/Q/3iLQ4/Buffy.The.Vampire.Slayer.S05.jpg" style="width:300px;" class="picture-resize" >
//                </div>
//            </div>
//            `);
//        });
//
//    var marker1_to_2 = [{'lng': -116.4816, 'lat': 43.57329}, {'lng': -116.48205, 'lat': 43.5733}, {'lng': -116.48228, 'lat': 43.57327}, {'lng': -116.48364, 'lat': 43.57253}, {'lng': -116.48364, 'lat': 43.57419}, {'lng': -116.4836, 'lat': 43.57586}, {'lng': -116.4796, 'lat': 43.57582}, {'lng': -116.47356, 'lat': 43.57577}, {'lng': -116.47263, 'lat': 43.57577}, {'lng': -116.46432, 'lat': 43.57575}, {'lng': -116.45367, 'lat': 43.57573}, {'lng': -116.43473, 'lat': 43.5757}, {'lng': -116.43458, 'lat': 43.57568}, {'lng': -116.43426, 'lat': 43.57568}, {'lng': -116.43377, 'lat': 43.57567}, {'lng': -116.43377, 'lat': 43.57574}, {'lng': -116.43378, 'lat': 43.57635}, {'lng': -116.4338, 'lat': 43.58217}, {'lng': -116.43379, 'lat': 43.58494}, {'lng': -116.43376, 'lat': 43.58674}, {'lng': -116.43375, 'lat': 43.58745}, {'lng': -116.43368, 'lat': 43.58756}, {'lng': -116.43367, 'lat': 43.58883}, {'lng': -116.43368, 'lat': 43.58931}, {'lng': -116.43369, 'lat': 43.58948}, {'lng': -116.43377, 'lat': 43.59002}, {'lng': -116.43384, 'lat': 43.59073}, {'lng': -116.43392, 'lat': 43.59156}, {'lng': -116.43391, 'lat': 43.5922}, {'lng': -116.43391, 'lat': 43.59249}, {'lng': -116.43386, 'lat': 43.59253}, {'lng': -116.43382, 'lat': 43.59257}, {'lng': -116.43369, 'lat': 43.59271}, {'lng': -116.43352, 'lat': 43.59277}, {'lng': -116.43301, 'lat': 43.59281}, {'lng': -116.43288, 'lat': 43.59284}, {'lng': -116.43233, 'lat': 43.59288}, {'lng': -116.43073, 'lat': 43.59302}, {'lng': -116.42955, 'lat': 43.59311}, {'lng': -116.42849, 'lat': 43.59317}, {'lng': -116.42756, 'lat': 43.59319}, {'lng': -116.4199, 'lat': 43.59327}, {'lng': -116.41985, 'lat': 43.59328}, {'lng': -116.41958, 'lat': 43.59335}, {'lng': -116.41762, 'lat': 43.59335}, {'lng': -116.4137, 'lat': 43.59336}, {'lng': -116.41343, 'lat': 43.59336}, {'lng': -116.40049, 'lat': 43.59338}, {'lng': -116.39645, 'lat': 43.59334}, {'lng': -116.3945, 'lat': 43.59331}, {'lng': -116.39265, 'lat': 43.59331}, {'lng': -116.38841, 'lat': 43.59338}, {'lng': -116.3863, 'lat': 43.59338}, {'lng': -116.38062, 'lat': 43.59338}, {'lng': -116.37453, 'lat': 43.59338}, {'lng': -116.37134, 'lat': 43.59338}, {'lng': -116.36948, 'lat': 43.59342}, {'lng': -116.36731, 'lat': 43.59358}, {'lng': -116.36587, 'lat': 43.59372}, {'lng': -116.36398, 'lat': 43.59398}, {'lng': -116.36178, 'lat': 43.59439}, {'lng': -116.35967, 'lat': 43.59489}, {'lng': -116.35857, 'lat': 43.59518}, {'lng': -116.35738, 'lat': 43.59554}, {'lng': -116.35641, 'lat': 43.59581}, {'lng': -116.35587, 'lat': 43.59597}, {'lng': -116.35476, 'lat': 43.59627}, {'lng': -116.35413, 'lat': 43.59641}, {'lng': -116.35297, 'lat': 43.59665}, {'lng': -116.35191, 'lat': 43.59682}, {'lng': -116.34996, 'lat': 43.59706}, {'lng': -116.34896, 'lat': 43.59712}, {'lng': -116.34802, 'lat': 43.59717}, {'lng': -116.34217, 'lat': 43.59718}, {'lng': -116.33435, 'lat': 43.59717}, {'lng': -116.30208, 'lat': 43.59716}, {'lng': -116.29795, 'lat': 43.59713}, {'lng': -116.29613, 'lat': 43.59711}, {'lng': -116.29443, 'lat': 43.59703}, {'lng': -116.2941, 'lat': 43.59697}, {'lng': -116.29228, 'lat': 43.59679}, {'lng': -116.29144, 'lat': 43.59668}, {'lng': -116.29072, 'lat': 43.59656}, {'lng': -116.2897, 'lat': 43.59636}, {'lng': -116.28871, 'lat': 43.59612}, {'lng': -116.28495, 'lat': 43.59509}, {'lng': -116.28414, 'lat': 43.59483}, {'lng': -116.28352, 'lat': 43.59458}, {'lng': -116.28308, 'lat': 43.59436}, {'lng': -116.27976, 'lat': 43.59275}, {'lng': -116.27915, 'lat': 43.59241}, {'lng': -116.27503, 'lat': 43.59042}, {'lng': -116.27085, 'lat': 43.58842}, {'lng': -116.26862, 'lat': 43.58736}, {'lng': -116.26622, 'lat': 43.58621}, {'lng': -116.26099, 'lat': 43.58367}, {'lng': -116.253, 'lat': 43.57982}, {'lng': -116.24951, 'lat': 43.57813}, {'lng': -116.24409, 'lat': 43.57549}, {'lng': -116.23795, 'lat': 43.57258}, {'lng': -116.23734, 'lat': 43.57239}, {'lng': -116.23656, 'lat': 43.57218}, {'lng': -116.23607, 'lat': 43.57209}, {'lng': -116.23556, 'lat': 43.57202}, {'lng': -116.23458, 'lat': 43.57194}, {'lng': -116.2337, 'lat': 43.57192}, {'lng': -116.23225, 'lat': 43.57192}, {'lng': -116.22395, 'lat': 43.57197}, {'lng': -116.22194, 'lat': 43.57196}, {'lng': -116.22124, 'lat': 43.57193}, {'lng': -116.22021, 'lat': 43.57188}, {'lng': -116.2196, 'lat': 43.57183}, {'lng': -116.21952, 'lat': 43.57173}, {'lng': -116.21938, 'lat': 43.57169}, {'lng': -116.21896, 'lat': 43.57162}, {'lng': -116.21829, 'lat': 43.57147}, {'lng': -116.21617, 'lat': 43.57085}, {'lng': -116.21604, 'lat': 43.5708}, {'lng': -116.21593, 'lat': 43.57073}, {'lng': -116.21583, 'lat': 43.57065}, {'lng': -116.2159, 'lat': 43.57053}, {'lng': -116.21612, 'lat': 43.57027}, {'lng': -116.21646, 'lat': 43.57}, {'lng': -116.21673, 'lat': 43.56982}, {'lng': -116.21692, 'lat': 43.56974}, {'lng': -116.21714, 'lat': 43.56968}, {'lng': -116.21722, 'lat': 43.56966}, {'lng': -116.21747, 'lat': 43.56961}, {'lng': -116.21774, 'lat': 43.56959}, {'lng': -116.21797, 'lat': 43.56962}, {'lng': -116.21816, 'lat': 43.56967}, {'lng': -116.21836, 'lat': 43.56974}, {'lng': -116.21853, 'lat': 43.56983}, {'lng': -116.21863, 'lat': 43.5699}, {'lng': -116.21897, 'lat': 43.57029}, {'lng': -116.21927, 'lat': 43.57059}, {'lng': -116.21951, 'lat': 43.57072}, {'lng': -116.21972, 'lat': 43.5708}, {'lng': -116.22006, 'lat': 43.57086}, {'lng': -116.22264, 'lat': 43.57098}]
//    var drive_path = new google.maps.Polyline({
//              path: marker1_to_2,
//              geodesic: true,
//              strokeColor: '#FF0000',
//              strokeOpacity: 1.0,
//              strokeWeight: 2
//    });
//    drive_path.setMap(map);
//
//    var marker_3 = new google.maps.Marker({
//        position: {lat: my_locations["pdx"]["lat"], lng: my_locations["pdx"]["lng"]},
//        map: map,
//        shape: shape,
//        title: "PDX Airport",
//        animation: google.maps.Animation.DROP,
//        icon: marker_c,
//        zIndex: my_locations["pdx"]["number"]
//      });
//    marker_3.addListener('click', function() {
//        $("#mypage").show();
//        $('.heading-1').html('PDX Airport');
//        $('.def-loc').html(' <i class="fa fa-location-arrow" aria-hidden="true"></i> Portland, Oregon');
//        $('.def-date').html('<i class="fa fa-calendar" aria-hidden="true"></i> 10/05/2016');
//        $('#mycontent').html(`
//            <div class="row">
//                <h4 class="heading-4">26 Minutes in Portland</h4>
//                <hr>
//                <div class="col-md-10 col-md-offset-1 col-xs-10 col-xs-offset-1">
//                <p class="paragraph-font" style="text-align:center;">Layover in Portland. Nothing exciting. Move on to San Fran and the greatest lounge on Earth.</p>
//            </div>
//            <br>
//            `);
//    });
//    var path = new google.maps.Polyline(pathOptions_flight);
//    var start_point = new google.maps.LatLng(my_locations["boi"]["lat"], my_locations["boi"]["lng"]);
//    var end_point = new google.maps.LatLng(my_locations["pdx"]["lat"], my_locations["pdx"]["lng"]);
//    path.getPath().setAt(0, start_point);
//    path.getPath().setAt(1, end_point);
//    path.setMap(map);
//
//    var marker_4 = new google.maps.Marker({
//        position: {lat: my_locations["sfo"]["lat"], lng: my_locations["sfo"]["lng"]},
//        map: map,
//        shape: shape,
//        title: "SFO Airport",
//        animation: google.maps.Animation.DROP,
//        icon: marker_d,
//        zIndex: my_locations["sfo"]["number"]
//      });
//    marker_4.addListener('click', function() {
//        $("#mypage").show();
//        $('.heading-1').html('SFO Airport');
//        $('.def-loc').html(' <i class="fa fa-location-arrow" aria-hidden="true"></i> San Francisco, California');
//        $('.def-date').html('<i class="fa fa-calendar" aria-hidden="true"></i> 10/05/2016');
//                $('#mycontent').html(`
//            <div class="row">
//                <h4 class="heading-4">Centurion Lounge</h4>
//                <hr>
//                <div class="col-md-6 col-xs-10 col-xs-offset-1">
//                    <p class="paragraph-font">Objectively the best airport lounge available. Delicious food. Open bar. You are also allowed up to two guest. My previous guest were my brother and mother; I miss sharing the free food and drinks with them. This lounge is available to anyone with the American Express Platinum Card. Boom! Get it (jk wait for the 100K offer to float around again). </p>
//                </div>
//                <div class="col-md-4 col-md-offset-0 col-xs-10 col-xs-offset-1">
//                    <img src="http://thehustleblog.com/blog/wp-content/uploads/2014/01/American-Express-Platinum.jpg" class="picture-resize" style="width:300px;">
//                </div>
//            </div>
//            <br>
//            <div class="row">
//                <h4 class="heading-4">Breakfast</h4>
//                <hr>
//                <div class="col-md-6 col-xs-10 col-xs-offset-1">
//                    <p class="paragraph-font"></p>
//                </div>
//                <div class="col-md-4 col-md-offset-0 col-xs-10 col-xs-offset-1">
//                    <img id="image_1" class="picture-resize" style="width:300px;">
//                </div>
//            </div>
//            <br>
//            <div class="row">
//                <h4 class="heading-4">Lunch</h4>
//                <hr>
//                <div class="col-md-6 col-xs-10 col-xs-offset-1">
//                    <p class="paragraph-font"></p>
//                </div>
//                <div class="col-md-4 col-md-offset-0 col-xs-10 col-xs-offset-1">
//                    <img id="image_2" class="picture-resize" style="width:300px;">
//                </div>
//            </div>
//
//            `);
//            $("#image_1").attr("src", image_1);
//            $("#image_2").attr("src", image_2);
//
//    });
//    var path = new google.maps.Polyline(pathOptions_flight);
//    var start_point = new google.maps.LatLng(my_locations["pdx"]["lat"], my_locations["pdx"]["lng"]);
//    var end_point = new google.maps.LatLng(my_locations["sfo"]["lat"], my_locations["sfo"]["lng"]);
//    path.getPath().setAt(0, start_point);
//    path.getPath().setAt(1, end_point);
//    path.setMap(map);
//
//
//    var marker_5 = new google.maps.Marker({
//        position: {lat: my_locations["icn"]["lat"], lng: my_locations["icn"]["lng"]},
//        map: map,
//        shape: shape,
//        title: "ICN Airport",
//        animation: google.maps.Animation.BOUNCE,
//        icon: marker_e,
//        zIndex: my_locations["icn"]["number"]
//      });
//    marker_5.addListener('click', function() {
//        $("#mypage").show();
//        $('.heading-1').html('ICN Airport');
//        $('.def-loc').html(' <i class="fa fa-location-arrow" aria-hidden="true"></i>Incheon, South Korea');
//        $('.def-date').html('<i class="fa fa-calendar" aria-hidden="true"></i> 10/06/2016');
//                $('#mycontent').html(`
//            <div class="row">
//                <h4 class="heading-4">Centurion Lounge</h4>
//                <hr>
//                <div class="col-md-6 col-xs-10 col-xs-offset-1">
//                    <p class="paragraph-font">Objectively the best airport lounge available. Delicious food. Open bar. You are also allowed up to two guest. My previous guest were my brother and mother; I miss sharing the free food and drinks with them. This lounge is available to anyone with the American Express Platinum Card. Boom! Get it (jk wait for the 100K offer to float around again). </p>
//                </div>
//                <div class="col-md-4 col-md-offset-0 col-xs-10 col-xs-offset-1">
//                    <img src="http://thehustleblog.com/blog/wp-content/uploads/2014/01/American-Express-Platinum.jpg" class="picture-resize" style="width:300px;">
//                </div>
//            </div>
//            <br>
//            <div class="row">
//                <h4 class="heading-4">Breakfast</h4>
//                <hr>
//                <div class="col-md-6 col-xs-10 col-xs-offset-1">
//                    <p class="paragraph-font"></p>
//                </div>
//                <div class="col-md-4 col-md-offset-0 col-xs-10 col-xs-offset-1">
//                    <img id="image_1" class="picture-resize" style="width:300px;">
//                </div>
//            </div>
//            <br>
//            <div class="row">
//                <h4 class="heading-4">Lunch</h4>
//                <hr>
//                <div class="col-md-6 col-xs-10 col-xs-offset-1">
//                    <p class="paragraph-font"></p>
//                </div>
//                <div class="col-md-4 col-md-offset-0 col-xs-10 col-xs-offset-1">
//                    <img id="image_2" class="picture-resize" style="width:300px;">
//                </div>
//            </div>
//
//            `);
//            $("#image_1").attr("src", image_1);
//            $("#image_2").attr("src", image_2);
//
//    });
//    var path = new google.maps.Polyline(pathOptions_flight);
//    var start_point = new google.maps.LatLng(my_locations["sfo"]["lat"], my_locations["sfo"]["lng"]);
//    var end_point = new google.maps.LatLng(my_locations["icn"]["lat"], my_locations["icn"]["lng"]);
//    path.getPath().setAt(0, start_point);
//    path.getPath().setAt(1, end_point);
//    path.setMap(map);
//
//
//
//
//}
//
//
//
//
//
//
////var beaches = [
////    ['Bondi Beach', -33.890542, 151.274856, 4],
////    ['Coogee Beach', -33.923036, 151.259052, 5],
////    ['Cronulla Beach', -34.028249, 151.157507, 3],
////    ['Manly Beach', -33.80010128657071, 151.28747820854187, 2],
////    ['Maroubra Beach', -33.950198, 151.259302, 1]
////];
////
////var locations = ['7216 Lima Drive Nampa, ID, 83687']
////
////function initMap() {
////    var map = new google.maps.Map(document.getElementById('map'), {
////      zoom: 10,
////      center: {lat: -33.9, lng: 151.2}
////    });
////    setMarkers(map);
////    plane_connect(map);
//////    var geocoder = new google.maps.Geocoder();
////}
////
////function setMarkers(map) {
////    var shape = {
////      coords: [1, 1, 1, 20, 18, 20, 18, 1],
////      type: 'poly'
////    };
////    for (var i = 0; i < beaches.length; i++) {
////      var beach = beaches[i];
////      var marker = new google.maps.Marker({
////        position: {lat: beach[1], lng: beach[2]},
////        map: map,
////        shape: shape,
////        title: beach[0],
////        zIndex: beach[3]
////      });
////    }
////}
////
////function plane_connect(map){
////    var flightPlanCoordinates = [
////      {lat: -33.890542, lng: 151.274856},
////      {lat: -33.950198, lng: 151.259302}
////    ];
////    var flightPath = new google.maps.Polyline({
////      path: flightPlanCoordinates,
////      geodesic: true,
////      strokeColor: '#FF0000',
////      strokeOpacity: 1.0,
////      strokeWeight: 2
////    });
////    flightPath.setMap(map);
////}
//
////function geocodeAddress(geocoder, address, myCallback) {
////    var address = address;
////    var latLng = '';
////    geocoder.geocode({'address': address}, function(results, status) {
////      if (status === 'OK') {
////        myCallback(results[0].geometry.location);
////      }
////      else {
////        alert('Geocode was not successful for the following reason: ' + status);
////      }
////    });
////}
//
//
//
