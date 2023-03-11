import numpy as np
import pandas as pd
import streamlit as st
import time
import base64
st.set_page_config(layout="wide")

#backgroung image
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: fit
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('images/background.png')  

c1 = st.container()
c2 = st.container()
with c1:
    st.markdown("<h1 style='text-align: center; color: #16FF00; font-size: 100px; font-family:cursive'><b>RAIN METER</b></h1>", unsafe_allow_html=True)
    st.markdown('''<p style='text-align: center; color: black; font-size: 15px'> Rain Meter is a web app which has 
      a Machine Learning model running at the back. The purpose of developing this app is to 
      predict whether it will rain the next day or not. This model is based on the Rain Prediction
      in Australia dataset. More than 80% of Australia has an annual rainfall of less than 
      600 mm which is less among the all continents other than Antartica which recieves less 
      rainfall. A place inland near Lake Eyre would only receive 81 mm of rain annually. The 
      average annual rainfall in the Australian desert is low, ranging from 81 to 250 mm. 
      Thunderstorms are relatively common in the region, with an annual average of 15 to 20 
      thunderstorms. The southern parts of Australia get the usual westerly winds and 
      rain-bearing cold fronts that come when high–pressure systems move towards northern 
      Australia during winter. Cold snaps may bring frosts inland, though temperatures near the
      coast are mild or near mild all year round. Summers in southern Australia are generally 
      dry and hot with coastal sea breezes. During a lengthy dry spell, hot and dry winds from 
      the interior can cause bushfires in some southern and eastern states, though most commonly
      Victoria and New South Wales. The tropical areas of northern Australia have a wet summer 
      because of the monsoon. During "the wet", typically October to April, humid north-westerly
       winds bring showers and thunderstorms. Occasionally, tropical cyclones can bring heavy 
       rainfall to tropical coastal regions, which is also likely to reach further inland.</p> ''', unsafe_allow_html=True)
