import pickle ,json
import numpy as np
import warnings
warnings.filterwarnings('ignore')


model = None
json_data = None
car_names= None
drive_wheel  =None
engine_type =None
fuel_system =None
fuel_type = None
asp_type = None


def predict_price(symboling,doornumber,wheelbase,carlength,carwidth,carheight,cylindernumber,enginesize,boreratio,stroke,compressionratio,horsepower,citympg,highwaympg,normalized_peakrpm,normalized_curbweight,fuel_tp,asp_tp,drive,engine,fuel_stm,cars):
    try:
        drive_index = json_data.index(drive.lower())
        engine_index = json_data.index(engine.lower())
        fuel_index = json_data.index(fuel_stm.lower())
        car_index = json_data.index(cars.lower())
        fuel_type_index = json_data.index(fuel_tp.lower())
        asp_type_index = json_data.index(asp_tp.lower())

    except:
        car_index = -1
        drive_index = -1
        engine_index = -1
        fuel_index = -1
        fuel_type_index = -1
        asp_type_index = -1


    X = np.zeros(len(json_data))

    X[0] = symboling
    X[1] = doornumber
    X[2]= wheelbase
    X[3]= carlength
    X[4] = carwidth
    X[5] = carheight
    X[6] = cylindernumber
    X[7] = enginesize
    X[8] = boreratio
    X[9] = stroke
    X[10] = compressionratio
    X[11] = horsepower
    X[12] = citympg
    X[13] = highwaympg
    X[14] = normalized_peakrpm
    X[15] = normalized_curbweight



    if car_index >=0 and drive_index >=0 and engine_index>=0 and fuel_index>=0 and fuel_type_index>=0 and asp_type_index>=0:
        X[car_index] = 1
        X[drive_index] = 1
        X[engine_index] = 1
        X[fuel_index] = 1
        X[fuel_type_index] = 1
        X[asp_type_index] = 1

    return round((model.predict([X])[0]),2)



def extract():
    global json_data
    global model
    global car_names
    global drive_wheel
    global engine_type
    global fuel_system
    global fuel_type
    global asp_type

    with open('myapp/model.pickle','rb') as f:
        model = pickle.load(f)
    with open('myapp/columns.json') as f:
        json_data = json.load(f)['data_columns']

    fuel_type = json_data[16:18]
    asp_type = json_data[18:20]
    drive_wheel = json_data[20:23]
    engine_type = json_data[23:29]
    fuel_system = json_data[29:36] 
    car_names = json_data[36:]


def carbrand():
    return [drive_wheel,engine_type,fuel_system,car_names,fuel_type,asp_type]


if __name__=="__main__":
    extract()
    print(carbrand())
    # print(engine_type)
    # print(fuel_system)
    # print(car_names)
    # print(predict_price(3,2,88.6,168.8,64.1,48.8,4,130,3.47,2.68,9,111,21,27,0.262318066,0.014530711,"gas","turbo","rwd","dohc","mpfi","bmw"))
    
