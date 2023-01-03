from flask import Flask, request, jsonify
import util
app = Flask(__name__)



@app.route('/get_manufacturer')
def get_manufacturer():
    response = jsonify({
        'manufacturer': util.get_manufacturer_names()
        })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response


@app.route('/get_model')
def get_model():
    response = jsonify({
        'model': util.get_model_names()
        })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/get_category')
def get_category():
    response = jsonify({
        'category': util.get_category_names()
        })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/get_leather_int')
def get_leather_int():
    response = jsonify({
        'leather_int': util.get_leather_int_names()
        })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/get_fuel_type')
def get_fuel_type():
    response = jsonify({
        'fuel_type': util.get_fuel_type_names()
        })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/get_gearbox_type')
def get_gearbox_type():
    response = jsonify({
        'gearbox_type': util.get_gearbox_type_names()
        })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/get_driver_wheels')
def get_driver_wheels():
    response = jsonify({
        'driver_wheels': util.get_driver_wheels_names()
        })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/get_wheel')
def get_wheel():
    response = jsonify({
        'wheel': util.get_wheel_names()
        })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/get_color')
def get_color():
    response = jsonify({
        'color': util.get_color_names()
        })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response
'''
def get_category_names():
    return __category

def get_leather_int_names():
    return __leather_int

def get_fuel_type_names():
    return __fuel_type

def get_gearbox_type_names():
    return __gear_box_type

def get_driver_wheels_names():
    return __driver_wheels

def get_wheel_names():
    return __wheel

def get_color_names():
    return __color

'''
@app.route('/hello')
def hello():
    return 'Hi!'

@app.route('/predict_car_price', methods = ['POST'])
def predict_car_price():
    
    manufacturer = request.form['manufacturer']
    model = request.form['model']
    prod_year = int(request.form['prod_year'])
    category  = request.form['category']
    leather_int = request.form['model']
    fuel = request.form['fuel']
    engine_vol = float(request.form['engine_vol'])
    mileage = float(request.form['mileage'])
    cylinders = float(request.form['cylinders'])
    gear_box = request.form['gear_box']
    drive_wheels = request.form['drive_wheels']
    doors = int(request.form['doors'])
    wheel = request.form['wheel']
    color = request.form['color']
    airbags = int(request.form['airbags'])
    '''
    manufacturer = 'LEXUS'
    model = 'RX 450'
    prod_year = 2010
    category  = 'Jeep'
    leather_int = 'Yes'
    fuel = 'Hybrid'
    engine_vol = 3.5
    mileage = 18600
    cylinders = 6.0
    gear_box = 'Automatic'
    drive_wheels = '4x4'
    doors = 4
    wheel = 'Left wheel'
    color = 'Silver'
    airbags = 12
    '''
    response = jsonify({
            'estimated_price': util.predict_price(manufacturer,model, prod_year,  category,  leather_int,  fuel,engine_vol,  mileage,   cylinders,   gear_box,   drive_wheels, doors,  wheel,  color, airbags)
        })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
if __name__ == "__main__":
    print('Starting Python Flash Server For Car Price Prediction...')
    util.load_saved_artifacts()
    #predict_car_price()
    app.run()
