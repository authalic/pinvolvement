<script>
$(function () {
    var mymap = L.map('mapid').setView([40.70, -111.9], 12);

    // disable the input fields until the user clicks the "Place Point Marker" button 
    $(".form-control").attr('disabled', 'disabled');
    $("#submitBtn").hide();


    // when user clicks the Place Point Marker button, turn on the fields and enable the point place event
    $("#enableDraw").click(function () {
        $(".form-control").prop('disabled', false); // turn on the fields
        mymap.on('click', onMapClick); // turn on the listening event to draw the point
        $("#submitBtn").show();
    });


    // get the Mapbox tile layer 
    L.tileLayer(
        'https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
            attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
            maxZoom: 22,
            id: 'mapbox.streets',
            accessToken: 'pk.eyJ1IjoiYXV0aGFsaWMiLCJhIjoiSHppSDJlWSJ9.h8QdzKDNKE1p_XDuzIBoSg'
        }).addTo(mymap);

    // read the points from the json file, convert them to geojson, add to map

    // circle marker styling
    var geojsonMarkerOptions = {
        radius: 12,
        fillColor: "#ff7800",
        color: "#000",
        weight: 1,
        opacity: 1,
        fillOpacity: 0.8
    };

    function getMapPoints() {

        $.getJSON('http://localhost:8000/contact/api/contact', function (json) {

            // there is probably a more elegant way to do this...

            for (x in json) {

                if (json[x].coordinates) { // check if there is a spatial location for the object

                    feature = {};

                    // store the items in the "properties" object
                    properties = {};
                    properties["first_name"] = json[x].first_name;
                    properties["last_name"] = json[x].last_name;
                    properties["email"] = json[x].email;
                    properties["phone"] = json[x].phone;

                    // split out the lat/lon from the Coordinates string
                    var re = /\(([^)]+)\)/; // get everything between the parentheses
                    lon = parseFloat(re.exec(json[x].coordinates)[1].split(" ")[
                        0]); // split the string at the space, return the 1st part
                    lat = parseFloat(re.exec(json[x].coordinates)[1].split(" ")[
                        1]); // return the second part

                    feature.type = "Point";
                    feature.properties = properties;
                    feature.coordinates = [lon, lat]

                    var myStyle = {
                        "color": "#ff7800",
                        "weight": 5,
                        "opacity": 0.65
                    };

                    L.geoJSON(feature, {
                        pointToLayer: function (feature, latlng) {

                            newMarker = L.circleMarker(latlng, geojsonMarkerOptions);

                            // create the popup content here. Probably should be a separate function...

                            newMarker.bindPopup(feature.properties.first_name +
                                " " + feature.properties.last_name
                            );

                            return newMarker;
                        },

                    }).addTo(mymap);
                }
            }
        });

    }

    getMapPoints();

    // store the current coordinates of the placed marker
    var markerLocation;

    // obtain the marker's initial position
    function onMapClick(e) {
        markerLocation = e.latlng;

        $('#clickCoords').html("Your marker is at " + e.latlng);

        commentMarker = new L.marker(e.latlng, {
            draggable: true
        });

        mymap.addLayer(commentMarker);  // layer storing the dropped point.  Use this to remove the point later.
        mymap.off('click');
        commentMarker.on('move', onMarkerMove);
    };

    // update the marker's xy position when the marker is dragged
    function onMarkerMove(e) {
        markerLocation = e.latlng;
        $('#clickCoords').html("Your marker moved to " + e.latlng);
    };



    // convert the marker's lat/lon location to the format expected by Django

    function getPointCoordsText() {
        var droppedPoint = markerLocation;
        // ST_GeomFromText('POINT(-71.060316 48.432044)', 4326)
        // var wkt = "'SRID=4326;POINT(" + markerLocation.lng + " " + markerLocation.lat + ")'";

        var wkt = "POINT(" + droppedPoint.lng + " " + droppedPoint.lat + ")";

        return wkt;
    };



    // handle the form submit using jQuery AJAX

    $("#commentform").submit(function (event) {
        // stop form from submitting normally

        event.preventDefault();

        var coords = getPointCoordsText();

        $("#pointCoords").val(coords);

        $.ajax({
            method: "POST",
            url: "http://localhost:8000/contact/api/contact",
            data: $("#commentform").serialize(),
            success: function (e) {
                $("#commentform")[0].reset();
            },
            error: function (e) {
                alert("Failwhale: " + msg);
                return false;
            }
        });
        $('#clickCoords').html("<b>Successfully added to database</b>");
        // refresh the map here, somehow?  Reload the data?
        getMapPoints();
        mymap.removeLayer(commentMarker); 
    });
});
</script>