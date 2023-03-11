import numpy as np
import pandas as pd
import streamlit as st
import pickle
from PIL import Image
import base64

st.set_page_config(layout="wide")

loaded_model = pickle.load(open('random_forest_classifier.sav','rb'))

def rain_prediction(input_data):
    input_data_nparr = np.asarray(input_data,dtype=object)
    input_data_reshaped = input_data_nparr.reshape(1,-1)
    data = input_data_reshaped
    rain_prediction = loaded_model.predict(data)
    return rain_prediction[0]

def autoplay_audio(file_path: str):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <audio autoplay="true">
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
        st.markdown(
            md,
            unsafe_allow_html=True,
        )

def main() :
     
    st.title("Predictor")

    location = ('Adelaide', 'Albany', 'Albury', 'AliceSprings', 'BadgerysCreek', 'Ballarat', 'Bendigo', 'Brisbane', 'Cairns', 'Canberra', 'Cobar', 'CoffsHarbour', 'Dartmoor', 'Darwin', 'GoldCoast', 'Hobart', 'Katherine', 'Launceston', 'Melbourne', 'MelbourneAirport', 'Mildura', 'Moree', 'MountGambier', 'MountGinini', 'Newcastle', 'Nhil', 'NorahHead', 'NorfolkIsland', 'Nuriootpa', 'PearceRAAF', 'Penrith', 'Perth', 'PerthAirport', 'Portland', 'Richmond', 'Sale', 'SalmonGums', 'Sydney', 'SydneyAirport', 'Townsville', 'Tuggeranong', 'Uluru', 'WaggaWagga', 'Walpole', 'Watsonia', 'Williamtown', 'Witchcliffe', 'Wollongong', 'Woomera')
    location_options = list(range(len(location)))
    windir = ('E', 'ENE', 'ESE', 'N', 'NE', 'NNE', 'NNW', 'NW', 'S', 'SE', 'SSE', 'SSW', 'SW', 'W', 'WNW', 'WSW')
    windir_options = list(range(len(windir)))
    rain = ('No','Yes')
    rain_options = list(range(len(rain)))

    rc11, rc12 = st.columns(2)
    with rc11:
        loc = st.selectbox("Location", location_options, format_func=lambda x: location[x])
        Location = loc
    with rc12:
        Rainfall = st.number_input(label="Rainfall",step=0.2,format="%.2f")

    rc21, rc22, rc23, rc24 = st.columns(4)
    with rc21:
        wind = st.selectbox("WindGustDir", windir_options, format_func=lambda x: windir[x])
        WindGustDir = int(wind)
    with rc22:
        WindGustSpeed = float(st.text_input(label="WindGustSpeed", value=0))
    with rc23:
        Evaporation = float(st.text_input(label="Evaporation", value=0))
    with rc24:
        Sunshine = float(st.text_input(label="Sunshine", value=0))

    rc31, rc32, rc33, rc34 = st.columns(4)
    with rc31:
        MinTemp = float(st.text_input(label="MinTemp", value=0))
    with rc32:
        Temp9am = float(st.text_input(label="Temp9am", value=0))
    with rc33:
        Temp3pm = float(st.text_input(label="Temp3pm", value=0))
    with rc34:
        MaxTemp = float(st.text_input(label="MaxTemp", value=0))


    rc41, rc42, rc43, rc44 = st.columns(4)
    with rc41:
        WindSpeed9am = float(st.text_input(label="WindSpeed9am", value=0))
    with rc42:
        wind9 = st.selectbox("WindDir9am", windir_options, format_func=lambda x: windir[x])
        WindDir9am = int(wind9)
    with rc43:
        WindSpeed3pm = float(st.text_input(label="WindSpeed3pm", value=0))
    with rc44:
        wind3 = st.selectbox("WindDir3pm", windir_options, format_func=lambda x: windir[x])
        WindDir3pm = int(wind3)


    rc51, rc52, rc53, rc54 = st.columns(4)
    with rc51:
        Humidity9am = float(st.text_input(label="Humidity9am", value=0))
    with rc52:
        Humidity3pm = float(st.text_input(label="Humidity3pm", value=0))
    with rc53:
        Pressure9am = float(st.text_input(label="Pressure9am", value=0))/1075
    with rc54:
        Pressure3pm = float(st.text_input(label="Pressure3pm", value=0))/1075


    rc61, rc62, rc63 = st.columns(3)
    with rc61:
        Cloud9am = float(st.text_input(label="Cloud9am", value=0))
    with rc62:
        Cloud3pm = float(st.text_input(label="Cloud3pm", value=0))
    with rc63:
        raint = st.selectbox("RainToday", rain_options, format_func=lambda x: rain[x])
        RainToday = int(raint)
    ####################################################################################################
    prediction = 999
    if st.button("Predict"):
        prediction = rain_prediction([  MinTemp,
                                        MaxTemp,
                                        Rainfall,
                                        Evaporation,
                                        Sunshine,
                                        WindGustSpeed,
                                        WindSpeed9am,
                                        WindSpeed3pm,
                                        Humidity9am,
                                        Humidity3pm,      
                                        Pressure9am,       
                                        Pressure3pm,       
                                        Cloud9am,         
                                        Cloud3pm,          
                                        Temp9am,         
                                        Temp3pm,          
                                        Location,          
                                        WindGustDir,      
                                        WindDir9am,      
                                        WindDir3pm,       
                                        RainToday       ])
    
    rained = Image.open('images/rained.jpg')
    sunny = Image.open('images/sunny.jpg')
    sunny_rainy = Image.open('images/sunny_rainy.jpg')

    if(prediction == 1):
        autoplay_audio("Audio/rained.mp3")
        st.success("It's Rainy Day")
        st.image(rained, caption='Rainy Day',width=1400)
        st.snow()
    elif(prediction == 0):
        autoplay_audio("Audio/sunnyday.mp3")
        st.success("It's Sunny Day")
        st.image(sunny, caption='Sunny Day',width=1400)
        st.balloons()
    else :
        st.image(sunny_rainy, caption='Sunny or Rainy', width=700)

    Location

if __name__ == '__main__':
    main()