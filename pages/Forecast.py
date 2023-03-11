import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import time

st.set_page_config(layout="wide")
st.title("Overall Stats")
@st.cache_data
def read_data():
    data = pd.read_csv("weatherAUS.csv")
    data['Date'] = pd.to_datetime(data['Date'])
    data['year'] = data['Date'].dt.year
    data['month'] = data['Date'].dt.month
    data['day'] = data['Date'].dt.day
    return data
data = read_data()
@st.cache_data
def stats():
    '''
    Shows the overall stats of ranifall, Mintemp and maxtemp from 2007 to 2017.
    '''
    hrc1, hrc2 = st.columns(2)
    with hrc1:
        st.bar_chart(data.groupby("year")['MinTemp'].mean())
    with hrc2:
        st.bar_chart(data.groupby("year")['MaxTemp'].mean())
    st.line_chart(data.groupby("year")["Rainfall"].mean())

def plot_stats(Location, year):
    
    location_df = data.loc[data["Location"] == Location]
    f1 = location_df.loc[location_df['year'] == int(year)]
    year_df = f1.groupby('month').mean()
    rc11, rc12 = st.columns(2)
    with rc11:
        st.line_chart(year_df["Rainfall"])
    with rc12:
        st.line_chart(year_df["WindGustSpeed"])

    rc21, rc22 = st.columns(2)
    with rc21:
        st.line_chart(year_df["WindSpeed9am"])
    with rc22:
        st.line_chart(year_df["WindSpeed3pm"])

    rc31, rc32 = st.columns(2)
    with rc31:
        st.line_chart(year_df["MinTemp"])
    with rc32:
        st.line_chart(year_df["MaxTemp"])

    rc41, rc42 = st.columns(2)
    with rc41:
        st.line_chart(year_df["Temp9am"])
    with rc42:
        st.line_chart(year_df["Temp3pm"])

    rc51, rc52 = st.columns(2)
    with rc51:
        st.line_chart(year_df["Humidity9am"])
    with rc52:
        st.line_chart(year_df["Humidity3pm"])

    rc61, rc62 = st.columns(2)
    with rc61:
        st.line_chart(year_df["Pressure9am"])
    with rc62:
        st.line_chart(year_df["Pressure3pm"])

    rc71, rc72 = st.columns(2)
    with rc71:
        st.line_chart(year_df["Cloud9am"])
    with rc72:
        st.line_chart(year_df["Cloud3pm"])


def main():
    stats()

    location_ = ('Adelaide', 'Albany', 'Albury', 'AliceSprings', 'BadgerysCreek', 'Ballarat', 'Bendigo', 'Brisbane', 'Cairns', 'Canberra', 'Cobar', 'CoffsHarbour', 'Dartmoor', 'Darwin', 'GoldCoast', 'Hobart', 'Katherine', 'Launceston', 'Melbourne', 'MelbourneAirport', 'Mildura', 'Moree', 'MountGambier', 'MountGinini', 'Newcastle', 'Nhil', 'NorahHead', 'NorfolkIsland', 'Nuriootpa', 'PearceRAAF', 'Penrith', 'Perth', 'PerthAirport', 'Portland', 'Richmond', 'Sale', 'SalmonGums', 'Sydney', 'SydneyAirport', 'Townsville', 'Tuggeranong', 'Uluru', 'WaggaWagga', 'Walpole', 'Watsonia', 'Williamtown', 'Witchcliffe', 'Wollongong', 'Woomera')
    year = ('2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017')
    
    st.subheader("Stats by Location and Year")
    rc11, rc12 = st.columns(2)
    with rc11:
        loca = st.selectbox("Location", location_)
    with rc12:
        Year = st.selectbox("Year", year)
    if st.button("Predict"):
        plot_stats(loca, Year)

if __name__ == '__main__':
    main()
