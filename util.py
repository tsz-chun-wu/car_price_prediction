import json
import pickle
import pandas as pd
import numpy as np

__locations = None
__data_columns = None
__rf_model = None
__category = None
__keather_int = None
__fuel_type = None
__gear_box_type = None
__driver_wheels = None
__wheel = None
__color = None

# scelar transformation function
__transform = None
__inverse_transform = None

num_vars = ['Prod. year', 'Mileage', 'Engine volume', 'Cylinders', 'Airbags', 'Price', 'Doors']
#num_vars = [x.lower() for x in num_vars]




def predict_price(manufacturer, model, prod_year, category, leather_int, fuel, engine_vol, mileage, cylinders, gear_box, drive_wheels, doors, wheel, color, airbags):
    input_df = pd.read_csv('input_df.csv')
    #input_df.columns = input_df.columns.str.lower()
    input_df[num_vars] = [prod_year,mileage,engine_vol,cylinders,airbags,0, doors]
    input_df[manufacturer] = 1
    input_df[model] = 1
    input_df[category] = 1
    input_df[leather_int] = 1
    input_df[fuel] = 1
    input_df[gear_box] = 1
    input_df[drive_wheels] = 1
    input_df[wheel] = 1
    input_df[color] = 1

    #print(input_df)
    input_df[num_vars] = __transform(input_df[num_vars])
    y_pred = __rf_model.predict(input_df.drop('Price', axis = 1))
    
    input_df['Price'] = y_pred
    input_df[num_vars] = __inverse_transform(input_df[num_vars])

    return int(input_df['Price'])   
   
    
def get_manufacturer_names():
    return __manufacturer

def get_model_names():
    return __model

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

def load_saved_artifacts():
    print('loading saved artifacts...start')
    global __rf_model
    global __transform
    global __inverse_transform
    
    global __data_columns
    
    global __locations 
    global __data_columns 
    global __manufacturer
    global __model 
    global __category 
    global __leather_int 
    global __fuel_type
    global __gear_box_type 
    global __driver_wheels 
    global __wheel 
    global __color 
    cum_sum_category_len = [7, 67, 1448, 1459, 1461, 1468, 1472, 1475, 1477, 1493];
    with open('columns.json','r') as f:
        __data_columns = json.load(f)['data_cols']
        __manufacturer = __data_columns[cum_sum_category_len[0]:cum_sum_category_len[1]]
        __model = __data_columns[cum_sum_category_len[1]:cum_sum_category_len[2]]
        __category = __data_columns[cum_sum_category_len[2]:cum_sum_category_len[3]]
        __leather_int = __data_columns[cum_sum_category_len[3]:cum_sum_category_len[4]]
        __fuel_type = __data_columns[cum_sum_category_len[4]:cum_sum_category_len[5]]
        __gear_box_type = __data_columns[cum_sum_category_len[5]:cum_sum_category_len[6]]
        __driver_wheels = __data_columns[cum_sum_category_len[6]:cum_sum_category_len[7]]
        __wheel = __data_columns[cum_sum_category_len[7]:cum_sum_category_len[8]]
        __color = __data_columns[cum_sum_category_len[8]:cum_sum_category_len[9]]

        #print(__data_columns)
    with open('car.pickle','rb') as f:
        __rf_model = pickle.load(f)
    with open('transform.pickle','rb') as f:
        __transform = pickle.load(f)
    with open('inv_transform.pickle','rb') as f:
        __inverse_transform = pickle.load(f)
        
    print('artifactrs loaded')
        
if __name__ == '__main__':
    
    load_saved_artifacts()
    #print(get_gearbox_type_names())
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
    
    print(predict_price(manufacturer,model, prod_year,  category,  leather_int,  fuel,engine_vol,  mileage,   cylinders,   gear_box,   drive_wheels, doors,  wheel,  color, airbags))