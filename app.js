
function getDoors() {
  var ui_door = document.getElementsByName("ui_door");
  for(var i in ui_door) {
    if(ui_door[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}



function onClickedEstimatePrice() {
  console.log("Estimate price button clicked");
  var mileage = document.getElementById("mileage");
  var prod_year = document.getElementById("prod_year");
  var eng_vol = document.getElementById("engine_vol");
  var cylinder = document.getElementById("cylinder");
  var airbags = document.getElementById("airbags");
  var doors = getDoors();
  var manufacturer = document.getElementById("manufacturer");
  var model = document.getElementById("model");
  var category = document.getElementById("category");
  var leather_int = document.getElementById("leather_interior");
  var fuel_type = document.getElementById("fuel_type");
  var gearbox_type = document.getElementById("gearbox_type");
  var driver_wheels = document.getElementById("driver_wheels");
  var wheel = document.getElementById("wheel");
  var color = document.getElementById("color");
  var estPrice = document.getElementById("uiEstimatedPrice");

  var url = "http://127.0.0.1:5000/predict_car_price"; //Use this if you are NOT using nginx which is first 7 tutorials
  // var url = "/api/predict_home_price"; // Use this if  you are using nginx. i.e tutorial 8 and onwards

  $.post(url, {    
      mileage: parseFloat(mileage.value),
      prod_year: parseInt(prod_year.value),
      cylinders: parseFloat(cylinder.value),
      engine_vol: parseFloat(eng_vol.value),
      airbags: parseInt(airbags.value),
      doors: doors,
      manufacturer: manufacturer.value,
      model: model.value,
      category: category.value,
      leather_int: leather_int.value,
      fuel: fuel_type.value,
      gear_box: gearbox_type.value,
      drive_wheels: driver_wheels.value,
      wheel: wheel.value, 
      color: color.value
      
  },function(data, status) {
      console.log(data.estimated_price);
      estPrice.innerHTML = "<h2>$" + data.estimated_price.toString() + "</h2>";
      console.log(status);
  });
}

function onPageLoad() {
  console.log( "document loaded" );
  var url = "http://127.0.0.1:5000/get_manufacturer"; // Use this if you are NOT using nginx which is first 7 tutorials
  //var url = "/api/get_location_names"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
  $.get(url,function(data, status) {
      console.log("got response for get_manufacturer_names request");
      if(data) {
          var manufacturer_names = data.manufacturer;
          //var ui_manufacturer = document.getElementById("manufacturer");
          $('#manufacturer').empty();
          for(var i in manufacturer_names) {
              var opt = new Option(manufacturer_names[i]);
              $('#manufacturer').append(opt);
          }
      }
  });

  var url = "http://127.0.0.1:5000/get_model"; // Use this if you are NOT using nginx which is first 7 tutorials
  //var url = "/api/get_location_names"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
  $.get(url,function(data, status) {
      console.log("got response for get_model_names request");
      if(data) {
          var model_names = data.model;
          //var ui_manufacturer = document.getElementById("manufacturer");
          $('#model').empty();
          for(var i in model_names) {
              var opt = new Option(model_names[i]);
              $('#model').append(opt);
          }
      }
  });

  var url = "http://127.0.0.1:5000/get_category"; // Use this if you are NOT using nginx which is first 7 tutorials
  //var url = "/api/get_location_names"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
  $.get(url,function(data, status) {
      console.log("got response for get_category_names request");
      if(data) {
          var category_names = data.category;
          $('#category').empty();
          for(var i in category_names) {
              var opt = new Option(category_names[i]);
              $('#category').append(opt);
          }
      }
  });

  var url = "http://127.0.0.1:5000/get_leather_int"; // Use this if you are NOT using nginx which is first 7 tutorials
  //var url = "/api/get_location_names"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
  $.get(url,function(data, status) {
      console.log("got response for get_leather_int_names request");
      if(data) {
          var leather_int_names = data.leather_int;
          $('#leather_interior').empty();
          for(var i in leather_int_names) {
              var opt = new Option(leather_int_names[i]);
              $('#leather_interior').append(opt);
          }
      }
  });

  var url = "http://127.0.0.1:5000/get_fuel_type"; // Use this if you are NOT using nginx which is first 7 tutorials
  //var url = "/api/get_location_names"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
  $.get(url,function(data, status) {
      console.log("got response for get_fuel_type_names_names request");
      if(data) {
          var fuel_type_names = data.fuel_type;
          $('#fuel_type').empty();
          for(var i in fuel_type_names) {
              var opt = new Option(fuel_type_names[i]);
              $('#fuel_type').append(opt);
          }
      }
  });

  var url = "http://127.0.0.1:5000/get_gearbox_type"; // Use this if you are NOT using nginx which is first 7 tutorials
  //var url = "/api/get_location_names"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
  $.get(url,function(data, status) {
      console.log("got response for get_gearbox_type_names request");
      if(data) {
          var gearbox_type_names = data.gearbox_type;
          $('#gearbox_type').empty();
          for(var i in gearbox_type_names) {
              var opt = new Option(gearbox_type_names[i]);
              $('#gearbox_type').append(opt);
          }
      }
  });

  var url = "http://127.0.0.1:5000/get_driver_wheels"; // Use this if you are NOT using nginx which is first 7 tutorials
  //var url = "/api/get_location_names"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
  $.get(url,function(data, status) {
      console.log("got response for get_driver_wheels_names request");
      if(data) {
          var driver_wheels_names = data.driver_wheels;
          $('#driver_wheels').empty();
          for(var i in driver_wheels_names) {
              var opt = new Option(driver_wheels_names[i]);
              $('#driver_wheels').append(opt);
          }
      }
  });

  var url = "http://127.0.0.1:5000/get_wheel"; // Use this if you are NOT using nginx which is first 7 tutorials
  //var url = "/api/get_location_names"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
  $.get(url,function(data, status) {
      console.log("got response for get_wheel_names request");
      if(data) {
          var get_wheel_names = data.wheel;
          $('#wheel').empty();
          for(var i in get_wheel_names) {
              var opt = new Option(get_wheel_names[i]);
              $('#wheel').append(opt);
          }
      }
  });

  var url = "http://127.0.0.1:5000/get_color"; // Use this if you are NOT using nginx which is first 7 tutorials
  //var url = "/api/get_location_names"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
  $.get(url,function(data, status) {
      console.log("got response for get_color_names request");
      if(data) {
          var color_names = data.color;
          $('#color').empty();
          for(var i in color_names) {
              var opt = new Option(color_names[i]);
              $('#color').append(opt);
          }
      }
  });
}



window.onload = onPageLoad;