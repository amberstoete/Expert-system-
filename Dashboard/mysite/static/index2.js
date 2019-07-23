//This is the JS Django uses
//var myPolygon;
function initialize() {
  var address = 'Amsterdam';
  var geocoder = new google.maps.Geocoder();
  geocoder.geocode({
    'address': address
  }, function(results, status) {
    if (status == google.maps.GeocoderStatus.OK) {
      var Lat = results[0].geometry.location.lat();
      var Lng = results[0].geometry.location.lng();
    } else {
      alert("Something got wrong " + status);
    }

  // Map Center
  var myLatLng = new google.maps.LatLng(Lat, Lng);
  // // General Options
  var mapOptions = {
    zoom: 16,
    center: myLatLng,
    mapTypeId: google.maps.MapTypeId.RoadMap
  };
  var map = new google.maps.Map(document.getElementById('map-canvas'),mapOptions);
  // Polygon Coordinates
  var triangleCoords = [
    new google.maps.LatLng(Lat, Lng),
    new google.maps.LatLng(Lat + 0.002, Lng),
    new google.maps.LatLng(Lat + 0.002, Lng + 0.003),
    new google.maps.LatLng(Lat, Lng + 0.003)
  ];

  // Styling & Controls
  var polygons = ["Lastage","Plantage", "Wallen", "Oost", "West", "Noord"];
  var colours = ["gold", "red", "teal", "blue", "orange", "purple"];
  var arrayLength = polygons.length;

  b = [];

  for (var i = 0; i < arrayLength; i++) { // Creating all the arrays
  polygons[i] = new google.maps.Polygon({
    paths: triangleCoords,
    draggable: true, // turn off if it gets annoying
    editable: true,
    strokeColor: colours[i],
    strokeOpacity: 0.8,
    strokeWeight: 2,
    fillColor: colours[i],
    fillOpacity: 0.45
  });
  // console.log(polygons[i])
  // b.push(polygons[i])
  polygons[i].setMap(map)

  //google.maps.event.addListener(myPolygon, "dragend", getPolygonCoords);
  google.maps.event.addListener(myPolygon.getPath(), "insert_at", getPolygonCoords);
  //google.maps.event.addListener(myPolygon.getPath(), "remove_at", getPolygonCoords);
  google.maps.event.addListener(myPolygon.getPath(), "set_at", getPolygonCoords);
}

//Display Coordinates below map
function getPolygonCoords() {
  var len = myPolygon.getPath().getLength();
  var htmlStr = "";
  for (var i = 0; i < len; i++) {
    htmlStr += "new google.maps.LatLng(" + myPolygon.getPath().getAt(i).toUrlValue(5) + "), ";
    //Use this one instead if you want to get rid of the wrap > new google.maps.LatLng(),
    //htmlStr += "" + myPolygon.getPath().getAt(i).toUrlValue(5);
  }
  document.getElementById('info').innerHTML = htmlStr;
}
function copyToClipboard(text) {
  window.prompt("Copy to clipboard: Ctrl+C, Enter", text);
}
}
}
