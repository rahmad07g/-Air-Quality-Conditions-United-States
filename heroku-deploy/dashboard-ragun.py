import streamlit as st
import pandas as pd 
import numpy as np 
import plotly.express as px
import plotly.graph_objects as go 
import matplotlib.pyplot as plt 
import seaborn as sns
from PIL import Image

#import seaborn as sns
DATE_COLUMN = 'date/time'
### hanya untuk loading RAW Data
data =pd.read_csv('Data.csv')

def load_data(nrows):
    data = pd.read_csv(data, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    return data

# Cleaning Data
subsetDataFrame = data[data['state_name'].isin(['Country Of Mexico', 'Canada','Guam','Virgin Islands','Puerto Rico'])]
data = data.drop(data.loc[data['state_name'].isin(['Country Of Mexico', 'Canada','Guam','Virgin Islands','Puerto Rico'])].index)

# untuk menampilkan visualisasi peta diperlukan kolom baru sebagai id untuk membedakan dari masing-masing states
state_codes = {
    'District Of Columbia' : 'DC','Mississippi': 'MS', 'Oklahoma': 'OK', 
    'Delaware': 'DE', 'Minnesota': 'MN', 'Illinois': 'IL', 'Arkansas': 'AR', 
    'New Mexico': 'NM', 'Indiana': 'IN', 'Maryland': 'MD', 'Louisiana': 'LA', 
    'Idaho': 'ID', 'Wyoming': 'WY', 'Tennessee': 'TN', 'Arizona': 'AZ', 
    'Iowa': 'IA', 'Michigan': 'MI', 'Kansas': 'KS', 'Utah': 'UT', 
    'Virginia': 'VA', 'Oregon': 'OR', 'Connecticut': 'CT', 'Montana': 'MT', 
    'California': 'CA', 'Massachusetts': 'MA', 'West Virginia': 'WV', 
    'South Carolina': 'SC', 'New Hampshire': 'NH', 'Wisconsin': 'WI',
    'Vermont': 'VT', 'Georgia': 'GA', 'North Dakota': 'ND', 
    'Pennsylvania': 'PA', 'Florida': 'FL', 'Alaska': 'AK', 'Kentucky': 'KY', 
    'Hawaii': 'HI', 'Nebraska': 'NE', 'Missouri': 'MO', 'Ohio': 'OH', 
    'Alabama': 'AL', 'Rhode Island': 'RI', 'South Dakota': 'SD', 
    'Colorado': 'CO', 'New Jersey': 'NJ', 'Washington': 'WA', 
    'North Carolina': 'NC', 'New York': 'NY', 'Texas': 'TX', 
    'Nevada': 'NV', 'Maine': 'ME'}
name = [data]
for i in name:
    i['state_code'] = i['state_name'].apply(lambda x : state_codes[x])

# Data untuk Visualisasi PETA
# Parameter PM
PM2_5 = data[(data['parameter_name']=='PM2.5 - Local Conditions')].groupby(['state_name','parameter_name','state_code'])['arithmetic_mean_average'].mean().reset_index().sort_values(by='arithmetic_mean_average', ascending=False)
PM10 = data[(data['parameter_name']=='PM10 Total 0-10um STP')].groupby(['state_name','parameter_name','state_code'])['arithmetic_mean_average'].mean().reset_index().sort_values(by='arithmetic_mean_average', ascending=False)
NO2 = data[(data['parameter_name']=='Nitrogen dioxide (NO2)')].groupby(['state_name','parameter_name','state_code'])['arithmetic_mean_average'].mean().reset_index().sort_values(by='arithmetic_mean_average', ascending=False)
Ozone = data[(data['parameter_name']=='Ozone')].groupby(['state_name','parameter_name','state_code'])['arithmetic_mean_average'].mean().reset_index().sort_values(by='arithmetic_mean_average', ascending=False)
CO = data[(data['parameter_name']=='Carbon monoxide')].groupby(['state_name','parameter_name','state_code'])['arithmetic_mean_average'].mean().reset_index().sort_values(by='arithmetic_mean_average', ascending=False)
SO2 = data[(data['parameter_name']=='Sulfur dioxide')].groupby(['state_name','parameter_name','state_code'])['arithmetic_mean_average'].mean().reset_index().sort_values(by='arithmetic_mean_average', ascending=False)

# Data Frame After and Before Covid
After_Covid = data[data['year']>=2019] # Query untuk After Covid
Before_Covid = data[(data['year']>=2015) &
                (data['year']<=2018)] # Query untuk Before Covid

# Membuat Dataframe untuk Klasifikasi After Covid
AF_PM2_5 = After_Covid[(After_Covid['parameter_name']=='PM2.5 - Local Conditions')].groupby(['state_name','parameter_name','state_code'])['arithmetic_mean_average'].mean().reset_index().sort_values(by='arithmetic_mean_average', ascending=False)
AF_PM10 = After_Covid[(After_Covid['parameter_name']=='PM10 Total 0-10um STP')].groupby(['state_name','parameter_name','state_code'])['arithmetic_mean_average'].mean().reset_index().sort_values(by='arithmetic_mean_average', ascending=False)
AF_NO2 = After_Covid[(After_Covid['parameter_name']=='Nitrogen dioxide (NO2)')].groupby(['state_name','parameter_name','state_code'])['arithmetic_mean_average'].mean().reset_index().sort_values(by='arithmetic_mean_average', ascending=False)
AF_Ozone = After_Covid[(After_Covid['parameter_name']=='Ozone')].groupby(['state_name','parameter_name','state_code'])['arithmetic_mean_average'].mean().reset_index().sort_values(by='arithmetic_mean_average', ascending=False)
AF_CO = After_Covid[(After_Covid['parameter_name']=='Carbon monoxide')].groupby(['state_name','parameter_name','state_code'])['arithmetic_mean_average'].mean().reset_index().sort_values(by='arithmetic_mean_average', ascending=False)
AF_SO2 = After_Covid[(After_Covid['parameter_name']=='Sulfur dioxide')].groupby(['state_name','parameter_name','state_code'])['arithmetic_mean_average'].mean().reset_index().sort_values(by='arithmetic_mean_average', ascending=False)

# Membuat Dataframe untuk Klasifikasi Before Covid
BF_PM2_5 = Before_Covid[(Before_Covid['parameter_name']=='PM2.5 - Local Conditions')].groupby(['state_name','parameter_name','state_code'])['arithmetic_mean_average'].mean().reset_index().sort_values(by='arithmetic_mean_average', ascending=False)
BF_PM10 = Before_Covid[(Before_Covid['parameter_name']=='PM10 Total 0-10um STP')].groupby(['state_name','parameter_name','state_code'])['arithmetic_mean_average'].mean().reset_index().sort_values(by='arithmetic_mean_average', ascending=False)
BF_NO2 = Before_Covid[(Before_Covid['parameter_name']=='Nitrogen dioxide (NO2)')].groupby(['state_name','parameter_name','state_code'])['arithmetic_mean_average'].mean().reset_index().sort_values(by='arithmetic_mean_average', ascending=False)
BF_Ozone = Before_Covid[(Before_Covid['parameter_name']=='Ozone')].groupby(['state_name','parameter_name','state_code'])['arithmetic_mean_average'].mean().reset_index().sort_values(by='arithmetic_mean_average', ascending=False)
BF_CO = Before_Covid[(Before_Covid['parameter_name']=='Carbon monoxide')].groupby(['state_name','parameter_name','state_code'])['arithmetic_mean_average'].mean().reset_index().sort_values(by='arithmetic_mean_average', ascending=False)
BF_SO2 = Before_Covid[(Before_Covid['parameter_name']=='Sulfur dioxide')].groupby(['state_name','parameter_name','state_code'])['arithmetic_mean_average'].mean().reset_index().sort_values(by='arithmetic_mean_average', ascending=False)

# Compare Before and After Covid
AF_Compare = After_Covid.groupby(['state_name','parameter_name','state_code'])['arithmetic_mean_average'].mean().reset_index().sort_values(by='arithmetic_mean_average', ascending=False)
BF_Compare = Before_Covid.groupby(['state_name','parameter_name','state_code'])['arithmetic_mean_average'].mean().reset_index().sort_values(by='arithmetic_mean_average', ascending=False)
AF_Compare = AF_Compare.rename(columns={"arithmetic_mean_average": "Mean AVG After Covid"})
BF_Compare = BF_Compare.rename(columns={"arithmetic_mean_average": "Mean AVG Before Covid"})
Perbandingan = pd.merge(BF_Compare,AF_Compare,)
Perbandingan['Perubahan'] =  Perbandingan['Mean AVG Before Covid'] - Perbandingan['Mean AVG After Covid'] 

# menghitung persentase kenaikan menggunakan looping 
def Kenaikan(AC,BC,SL):
  return (SL/BC)*(-100)
def Penurunan(AC,BC,SL):
  return (SL/BC)*(-100)
Persentase = []
for i in range(len(Perbandingan)):
  if Perbandingan['Perubahan'][i]>=0:
    Persentase.append(Kenaikan(Perbandingan['Mean AVG After Covid'][i],Perbandingan['Mean AVG Before Covid'][i],Perbandingan['Perubahan'][i]))
  elif Perbandingan['Perubahan'][i]<0:
    Persentase.append(Penurunan(Perbandingan['Mean AVG After Covid'][i],Perbandingan['Mean AVG Before Covid'][i],Perbandingan['Perubahan'][i]))
Perbandingan['Persentase'] = Persentase
Perbandingan.reset_index().sort_values(by='Persentase', ascending=False).tail(5)

# Perbandingan Secara Keseluruhan
General_AFC = Perbandingan.groupby(['parameter_name'])['Mean AVG After Covid'].mean().reset_index().sort_values(by='Mean AVG After Covid', ascending=False)
General_BFC = Perbandingan.groupby(['parameter_name'])['Mean AVG Before Covid'].mean().reset_index().sort_values(by='Mean AVG Before Covid', ascending=False)
General = pd.merge(General_BFC,General_AFC)
General['Perubahan'] =  General['Mean AVG Before Covid'] - General['Mean AVG After Covid'] 
General['Persentase'] =  (General['Perubahan']/General['Mean AVG Before Covid'])*-100 # dikarenakan mengukur pada tahun sebelum dan sesudah
General.sort_values(by='Persentase', ascending=True).head(6)

#Query untuk setiap kelompok
Visual1 = General.iloc[[3, 4, 5]].sort_values(by='Persentase', ascending=False)
Visual2 = General.iloc[[0, 1, 2]].sort_values(by='Persentase', ascending=False)

#Membuat dataframe baru untuk setiap parameter kualitas udara
I_PM2_5 = Perbandingan[Perbandingan['parameter_name']=='PM2.5 - Local Conditions']
I_PM10 = Perbandingan[Perbandingan['parameter_name']=='PM10 Total 0-10um STP']
I_NO2 = Perbandingan[Perbandingan['parameter_name']=='Nitrogen dioxide (NO2)']
I_Ozone = Perbandingan[Perbandingan['parameter_name']=='Ozone']
I_CO= Perbandingan[Perbandingan['parameter_name']=='Carbon monoxide']
I_SO2 = Perbandingan[Perbandingan['parameter_name']=='Sulfur dioxide']

# Top 5 and Bottom 5
TB5_PM25 = I_PM2_5.head(5).append(I_PM2_5.tail(5)).sort_values(by='Persentase', ascending=False)
TB5_PM10 = I_PM10.head(5).append(I_PM10.tail(5)).sort_values(by='Persentase', ascending=False)
TB5_NO2 = I_NO2.head(5).append(I_NO2.tail(5)).sort_values(by='Persentase', ascending=False)
TB5_Ozone = I_Ozone.head(5).append(I_Ozone.tail(5)).sort_values(by='Persentase', ascending=False)
TB5_CO = I_CO.head(5).append(I_CO.tail(5)).sort_values(by='Persentase', ascending=False)
TB5_SO2 = I_SO2.head(5).append(I_SO2.tail(5)).sort_values(by='Persentase', ascending=False)

#### Data Statistik
Tendency = data[data['parameter_name']=='Nitrogen dioxide (NO2)']
Tendency = Tendency[Tendency['state_name']=='Illinois']
T_NO2 = Tendency['arithmetic_mean_average']
# function untuk membuat central tendency dari setiap site yang terdiri atas median,mean,modus
T_NO2.mean()
T_NO2.median()
T_NO2.mode()

# Selectbox
selectbox = st.sidebar.selectbox(
    "Pilih Halaman",
    ("Visualisasi", "Statistical Analysis")
)   
if selectbox == "Visualisasi":
    st.title('Air Quality USA ')
    if st.checkbox ('Show Data'):
        st.subheader('Air Quality 1980 - 2022')
        st.write(data)

#interactivity 
    if st.checkbox ('Show Visualisasi Air Quality USA by States (1980-2022)'):
        st.subheader('Air Quality USA by States (1980-2022)')
        interactivity1 = st.selectbox (label="Pilih Parameter Air Quality", options =('PM 2.5 & PM 10','NO2','Ozone','CO','SO2'))
        st.write()
        # jika memilih PM 2.5 dan PM 10
        if interactivity1 == 'PM 2.5 & PM 10':
            # Visualisasi 1980-2022 PM 2.5
            fig1= go.Figure(data=go.Choropleth(
            locations=PM2_5['state_code'], # Spatial coordinates
            z = PM2_5['arithmetic_mean_average'].astype(float), # Data to be color-coded
            locationmode = 'USA-states', # set of locations match entries in `locations`
            colorscale = 'Reds',
            colorbar_title = "Micrograms/Cubic Meter (25 C)",
            text =PM2_5['state_name'],
            ))
            fig1.update_layout(
            geo_scope='usa', # limite map scope to USA
            )
            fig1.update_layout(height=600, width=800, title_text=f"1980 - 2022 Rata Rata Nilai: PM 2.5")
            st.plotly_chart(fig1)

            # Visualisasi 1980-2022 PM 10
            fig2= go.Figure(data=go.Choropleth(
            locations=PM10['state_code'], # Spatial coordinates
            z = PM10['arithmetic_mean_average'].astype(float), # Data to be color-coded
            locationmode = 'USA-states', # set of locations match entries in `locations`
            colorscale = 'Reds',
            colorbar_title = "Micrograms/Cubic Meter (LC))",
            text =PM10['state_name'],
            ))
            fig2.update_layout(
            geo_scope='usa', # limite map scope to USA
            )
            fig2.update_layout(height=600, width=800, title_text=f"1980 - 2022 Rata Rata Nilai: PM 10")
            st.plotly_chart(fig2)
            
        # jika memilih NO2
        elif interactivity1 == 'NO2':
            fig3= go.Figure(data=go.Choropleth(
            locations=NO2['state_code'], # Spatial coordinates
            z = NO2['arithmetic_mean_average'].astype(float), # Data to be color-coded
            locationmode = 'USA-states', # set of locations match entries in `locations`
            colorscale = 'Reds',
            colorbar_title = "Parts per billion",
            text =NO2['state_name'],
            ))
            fig3.update_layout(
            geo_scope='usa', # limite map scope to USA
            )
            fig3.update_layout(height=600, width=800, title_text=f"1980 - 2022 Rata Rata Nilai: NO2")
            st.plotly_chart(fig3)
            
        # jika memilih S02
        elif interactivity1 == 'SO2':
            fig4= go.Figure(data=go.Choropleth(
            locations=SO2['state_code'], # Spatial coordinates
            z = SO2['arithmetic_mean_average'].astype(float), # Data to be color-coded
            locationmode = 'USA-states', # set of locations match entries in `locations`
            colorscale = 'Reds',
            colorbar_title = "Parts per billion",
            text =SO2['state_name'],
            ))
            fig4.update_layout(
            geo_scope='usa', # limite map scope to USA
            )
            fig4.update_layout(height=600, width=800, title_text=f"1980 - 2022 Rata Rata Nilai: SO2")
            st.plotly_chart(fig4)
            

        # jika memilih Ozone 
        elif interactivity1 == 'Ozone':
            fig5= go.Figure(data=go.Choropleth(
            locations=Ozone['state_code'], # Spatial coordinates
            z = Ozone['arithmetic_mean_average'].astype(float), # Data to be color-coded
            locationmode = 'USA-states', # set of locations match entries in `locations`
            colorscale = 'Reds',
            colorbar_title = "Parts per million",
            text =Ozone['state_name'],
            ))
            fig5.update_layout(
            geo_scope='usa', # limite map scope to USA
            )
            fig5.update_layout(height=600, width=800, title_text=f"1980 - 2022 Rata Rata Nilai: Ozone")
            st.plotly_chart(fig5)

        # jika memilih CO
        elif interactivity1 == 'CO':
            fig6= go.Figure(data=go.Choropleth(
            locations=CO['state_code'], # Spatial coordinates
            z = CO['arithmetic_mean_average'].astype(float), # Data to be color-coded
            locationmode = 'USA-states', # set of locations match entries in `locations`
            colorscale = 'Reds',
            colorbar_title = "Parts per million",
            text =CO['state_name'],
            ))
            fig6.update_layout(
            geo_scope='usa', # limite map scope to USA
            )
            fig6.update_layout(height=600, width=800, title_text=f"1980 - 2022 Rata Rata Nilai: CO")
            st.plotly_chart(fig6);
        #interactivity = st.selectbox (label="Tampilkan Kualitas Udara Berdasarkan", options =('Parameter','Tahun'))

#interactivity 
    if st.checkbox ('Show Visualisasi Air Quality Pra Covid (2014-2018) & Pasca Covid (2019-2022)'):
        st.subheader('Air Quality Pra Covid (2014-2018) & Pasca Covid (2019-2022)')
        #interactivity 
        interactivity2 = st.selectbox (label="Pilih Parameter Air Quality", options =('PM 2.5','PM 10','NO2','Ozone','CO','SO2'))
        st.write()
        # jika memilih PM 2.5 
        if interactivity2 == 'PM 2.5':
            # Visualisasi Pra-Covid 2014-2018 PM 2.5
            fig1= go.Figure(data=go.Choropleth(
            locations=BF_PM2_5['state_code'], # Spatial coordinates
            z = BF_PM2_5['arithmetic_mean_average'].astype(float), # Data to be color-coded
            locationmode = 'USA-states', # set of locations match entries in `locations`
            colorscale = 'Reds',
            colorbar_title = "Micrograms/Cubic Meter (25 C)",
            text =BF_PM2_5['state_name'],
            ))
            fig1.update_layout(
            geo_scope='usa', # limite map scope to USA
            )
            fig1.update_layout(height=600, width=800, title_text=f"Periode Sebelum Covid (2015-2018) Rata Rata Nilai PM 2.5")
            st.plotly_chart(fig1)

            # Visualisasi Pasca Covid 2019-2022 PM 2.5
            fig2= go.Figure(data=go.Choropleth(
            locations=AF_PM2_5['state_code'], # Spatial coordinates
            z = AF_PM2_5['arithmetic_mean_average'].astype(float), # Data to be color-coded
            locationmode = 'USA-states', # set of locations match entries in `locations`
            colorscale = 'Reds',
            colorbar_title = "Micrograms/Cubic Meter (25 C)",
            text =AF_PM2_5['state_name'],
            ))
            fig2.update_layout(
            geo_scope='usa', # limite map scope to USA
            )
            fig2.update_layout(height=600, width=800, title_text=f"Periode Setelah Covid (2019-2022) Rata Rata Nilai PM 2.5")
            st.plotly_chart(fig2)

        elif interactivity2 == 'PM 10':
            # Visualisasi Pra-Covid 2014-2018 PM 10
            fig1= go.Figure(data=go.Choropleth(
            locations=BF_PM10['state_code'], # Spatial coordinates
            z = BF_PM10['arithmetic_mean_average'].astype(float), # Data to be color-coded
            locationmode = 'USA-states', # set of locations match entries in `locations`
            colorscale = 'Reds',
            colorbar_title = "Micrograms/Cubic Meter (LC)",
            text =BF_PM10['state_name'],
            ))
            fig1.update_layout(
            geo_scope='usa', # limite map scope to USA
            )
            fig1.update_layout(height=600, width=800, title_text=f"Periode Sebelum Covid (2015-2018) Rata Rata Nilai PM 10")
            st.plotly_chart(fig1)

            # Visualisasi Pasca-Covid 2019-2022 PM 10
            fig2= go.Figure(data=go.Choropleth(
            locations=AF_PM10['state_code'], # Spatial coordinates
            z = AF_PM10['arithmetic_mean_average'].astype(float), # Data to be color-coded
            locationmode = 'USA-states', # set of locations match entries in `locations`
            colorscale = 'Reds',
            colorbar_title = "Micrograms/Cubic Meter (LC)",
            text =AF_PM10['state_name'],
            ))
            fig2.update_layout(
            geo_scope='usa', # limite map scope to USA
            )
            fig2.update_layout(height=600, width=800, title_text=f"Periode Setelah Covid (2019-2022) Rata Rata Nilai PM 10")
            st.plotly_chart(fig2)

        elif interactivity2 == 'NO2':
            # Visualisasi Pra-Covid 2014-2018 NO2
            fig1= go.Figure(data=go.Choropleth(
            locations=BF_NO2['state_code'], # Spatial coordinates
            z = BF_NO2['arithmetic_mean_average'].astype(float), # Data to be color-coded
            locationmode = 'USA-states', # set of locations match entries in `locations`
            colorscale = 'Reds',
            colorbar_title = "Parts per billion",
            text =BF_NO2['state_name'],
            ))
            fig1.update_layout(
            geo_scope='usa', # limite map scope to USA
            )
            fig1.update_layout(height=600, width=800, title_text=f"Periode Sebelum Covid (2015-2018) Rata Rata Nilai NO2")
            st.plotly_chart(fig1)

            # Visualisasi Pasca-Covid 2019-2022 NO2
            fig2= go.Figure(data=go.Choropleth(
            locations=AF_NO2['state_code'], # Spatial coordinates
            z = AF_NO2['arithmetic_mean_average'].astype(float), # Data to be color-coded
            locationmode = 'USA-states', # set of locations match entries in `locations`
            colorscale = 'Reds',
            colorbar_title = "Parts per billion",
            text =AF_NO2['state_name'],
            ))
            fig2.update_layout(
            geo_scope='usa', # limite map scope to USA
            )
            fig2.update_layout(height=600, width=800, title_text=f"Periode Setelah Covid (2019-2022) Rata Rata Nilai NO2")
            st.plotly_chart(fig2)

        elif interactivity2 == 'Ozone':
            # Visualisasi Pra-Covid 2014-2018 Ozone
            fig1= go.Figure(data=go.Choropleth(
            locations=BF_Ozone['state_code'], # Spatial coordinates
            z = BF_Ozone['arithmetic_mean_average'].astype(float), # Data to be color-coded
            locationmode = 'USA-states', # set of locations match entries in `locations`
            colorscale = 'Reds',
            colorbar_title = "Parts per million",
            text =BF_Ozone['state_name'],
            ))
            fig1.update_layout(
            geo_scope='usa', # limite map scope to USA
            )
            fig1.update_layout(height=600, width=800, title_text=f"Periode Sebelum Covid (2015-2018) Rata Rata Nilai Ozone")
            st.plotly_chart(fig1)

            # Visualisasi Pasca-Covid 2019-2022 Ozone
            fig2= go.Figure(data=go.Choropleth(
            locations=AF_Ozone['state_code'], # Spatial coordinates
            z = AF_Ozone['arithmetic_mean_average'].astype(float), # Data to be color-coded
            locationmode = 'USA-states', # set of locations match entries in `locations`
            colorscale = 'Reds',
            colorbar_title = "Parts per million",
            text =AF_Ozone['state_name'],
            ))
            fig2.update_layout(
            geo_scope='usa', # limite map scope to USA
            )
            fig2.update_layout(height=600, width=800, title_text=f"Periode Setelah Covid (2019-2022) Rata Rata Nilai Ozone")
            st.plotly_chart(fig2)

        elif interactivity2 == 'CO':
            # Visualisasi Pra-Covid 2014-2018 CO
            fig1= go.Figure(data=go.Choropleth(
            locations=BF_CO['state_code'], # Spatial coordinates
            z = BF_CO['arithmetic_mean_average'].astype(float), # Data to be color-coded
            locationmode = 'USA-states', # set of locations match entries in `locations`
            colorscale = 'Reds',
            colorbar_title = "Parts per million",
            text =BF_CO['state_name'],
            ))
            fig1.update_layout(
            geo_scope='usa', # limite map scope to USA
            )
            fig1.update_layout(height=600, width=800, title_text=f"Periode Sebelum Covid (2015-2018) Rata Rata Nilai CO")
            st.plotly_chart(fig1)

            # Visualisasi Pasca-Covid 2019-2022 CO
            fig2= go.Figure(data=go.Choropleth(
            locations=AF_CO['state_code'], # Spatial coordinates
            z = AF_CO['arithmetic_mean_average'].astype(float), # Data to be color-coded
            locationmode = 'USA-states', # set of locations match entries in `locations`
            colorscale = 'Reds',
            colorbar_title = "Parts per million",
            text =AF_CO['state_name'],
            ))
            fig2.update_layout(
            geo_scope='usa', # limite map scope to USA
            )
            fig2.update_layout(height=600, width=800, title_text=f"Periode Setelah Covid (2019-2022) Rata Rata Nilai CO")
            st.plotly_chart(fig2)

        elif interactivity2 == 'SO2':
            # Visualisasi Pra-Covid 2014-2018 SO2
            fig1= go.Figure(data=go.Choropleth(
            locations=BF_SO2['state_code'], # Spatial coordinates
            z = BF_SO2['arithmetic_mean_average'].astype(float), # Data to be color-coded
            locationmode = 'USA-states', # set of locations match entries in `locations`
            colorscale = 'Reds',
            colorbar_title = "Parts per billion",
            text =BF_SO2['state_name'],
            ))
            fig1.update_layout(
            geo_scope='usa', # limite map scope to USA
            )
            fig1.update_layout(height=600, width=800, title_text=f"Periode Sebelum Covid (2015-2018) Rata Rata Nilai SO2")
            st.plotly_chart(fig1)

            # Visualisasi Pasca-Covid 2019-2022 SO2
            fig2= go.Figure(data=go.Choropleth(
            locations=AF_SO2['state_code'], # Spatial coordinates
            z = AF_SO2['arithmetic_mean_average'].astype(float), # Data to be color-coded
            locationmode = 'USA-states', # set of locations match entries in `locations`
            colorscale = 'Reds',
            colorbar_title = "Parts per billion",
            text =AF_SO2['state_name'],
            ))
            fig2.update_layout(
            geo_scope='usa', # limite map scope to USA
            )
            fig2.update_layout(height=600, width=800, title_text=f"Periode Setelah Covid (2019-2022) Rata Rata Nilai SO2")
            st.plotly_chart(fig2)

    if st.checkbox ('Show Bar Chart Air Quality'):
        st.subheader('Bar Chart')
        #interactivity 
        interactivity2 = st.selectbox (label="Visualisasi Kualitas Udara States-USA 2015-2022", options =('Compare All Parameter (After & Before Covid)','Compare (After & Before Covid) PM 10 by States',
        'Compare (After & Before Covid) PM 2.5 by States','Compare (After & Before Covid) NO2 by States','Compare (After & Before Covid) Ozone by States','Compare (After & Before Covid) CO by States',
        'Compare (After & Before Covid) SO2 by States'))
        st.write()
        # jika memilih Compare by parameter
        if interactivity2 == 'Compare All Parameter (After & Before Covid)':
            name = [Visual1,Visual2]
            label = ['(SO2,CO,Ozone)','(PM 2.5, PM 10, NO2)'] #label sesuai dengan jenis kualitas udara
            a = 0
            for i in name:
                fig = px.histogram(i, y = 'parameter_name', x = ['Mean AVG After Covid','Mean AVG Before Covid'], barmode = 'group', title =f"Comparisons of Air Quality {label[a]} By Mean Average ",)
                fig.data[0].text = round(i['Persentase'],2)
                fig.update_traces(textposition='outside', textfont_size=12)
                fig.update_layout(font_family="Rockwell",legend=dict(title=None, orientation="h", y=1, yanchor="bottom", x=0.5, xanchor="center"),height=500, width=800)
                a=a+1
                fig

        # jika memilih Compare PM 2.5
        if interactivity2 == 'Compare (After & Before Covid) PM 2.5 by States':
            fig = px.histogram(TB5_PM25, y = 'state_name', x = ['Mean AVG After Covid','Mean AVG Before Covid'], barmode = 'group', title =f"Top 5 & Bottom 5 Comparisons of Air Quality PM 2.5 By State (Micrograms/Cubic Meter (25 C))",)
            fig.data[0].text = round(TB5_PM25['Persentase'],2)
            fig.update_traces(textposition='outside', textfont_size=12)
            fig.update_layout(font_family="Rockwell",legend=dict(title=None, orientation="h", y=1, yanchor="bottom", x=0.5, xanchor="center"),height=500, width=700)
            fig

        # jika memilih Compare PM 10
        if interactivity2 == 'Compare (After & Before Covid) PM 10 by States':
            fig = px.histogram(TB5_PM10, y = 'state_name', x = ['Mean AVG After Covid','Mean AVG Before Covid'], barmode = 'group', title =f"Top 5 & Bottom 5 Comparisons of Air Quality PM 10 By State Micrograms/Cubic Meter (LC))",)
            fig.data[0].text = round(TB5_PM10['Persentase'],2)
            fig.update_traces(textposition='outside', textfont_size=12)
            fig.update_layout(font_family="Rockwell",legend=dict(title=None, orientation="h", y=1, yanchor="bottom", x=0.5, xanchor="center"),height=500, width=700)
            fig

        # jika memilih Compare N02
        if interactivity2 == 'Compare (After & Before Covid) NO2 by States':
            fig = px.histogram(TB5_NO2, y = 'state_name', x = ['Mean AVG After Covid','Mean AVG Before Covid'], barmode = 'group', title =f"Top 5 & Bottom 5 Comparisons of Air Quality NO2 By State (Parts per billion))",)
            fig.data[0].text = round(TB5_NO2['Persentase'],2)
            fig.update_traces(textposition='outside', textfont_size=12)
            fig.update_layout(font_family="Rockwell",legend=dict(title=None, orientation="h", y=1, yanchor="bottom", x=0.5, xanchor="center"),height=500, width=700)
            fig

        # jika memilih Compare Ozone
        if interactivity2 == 'Compare (After & Before Covid) Ozone by States':
            fig = px.histogram(TB5_Ozone, y = 'state_name', x = ['Mean AVG After Covid','Mean AVG Before Covid'], barmode = 'group', title =f"Top 5 & Bottom 5 Comparisons of Air Quality Ozone By State (Parts per million)",)
            fig.data[0].text = round(TB5_Ozone['Persentase'],2)
            fig.update_traces(textposition='outside', textfont_size=12)
            fig.update_layout(font_family="Rockwell",legend=dict(title=None, orientation="h", y=1, yanchor="bottom", x=0.5, xanchor="center"),height=500, width=700)
            fig

        # jika memilih Compare CO
        if interactivity2 == 'Compare (After & Before Covid) CO by States':
            fig = px.histogram(TB5_CO, y = 'state_name', x = ['Mean AVG After Covid','Mean AVG Before Covid'], barmode = 'group', title =f"Top 5 & Bottom 5 Comparisons of Air Quality CO By State (Parts per million)",)
            fig.data[0].text = round(TB5_CO['Persentase'],2)
            fig.update_traces(textposition='outside', textfont_size=12)
            fig.update_layout(font_family="Rockwell",legend=dict(title=None, orientation="h", y=1, yanchor="bottom", x=0.5, xanchor="center"),height=500, width=700)
            fig

        # jika memilih Compare SO2
        if interactivity2 == 'Compare (After & Before Covid) SO2 by States':
            fig = px.histogram(TB5_SO2, y = 'state_name', x = ['Mean AVG After Covid','Mean AVG Before Covid'], barmode = 'group', title =f"Top 5 & Bottom 5 Comparisons of Air Quality SO2 By State (Parts per billion)",)
            fig.data[0].text = round(TB5_SO2['Persentase'],2)
            fig.update_traces(textposition='outside', textfont_size=12)
            fig.update_layout(font_family="Rockwell",legend=dict(title=None, orientation="h", y=1, yanchor="bottom", x=0.5, xanchor="center"),height=500, width=700)
            fig




elif selectbox == "Statistical Analysis":
    st.title('Analisis Statistik')
    '''
    Analisis statistik ini bertujuan untuk apakah penurunan/perubahan Kualitas Udara dengan parameter Nitrogen dioxide (NO2) yang terjadi setelah pasca covid merupakan penurunan tertinggi di State Illinois dan memiliki perbedaan signifikan dengan Nilai Kualitas Udara dengan rata-rata rentang periode 42 tahun terakhir (1980-2022).
    '''

    '''Adapun Tahapan Pertama yang dilakukan adalah Menghitung **Central Tendency**'''
    '''**Central Tendency** terdiri atas **mean,median dan modus**, nilai ketiga variable tersebut dapat dicari jika suatu kolom **memiliki attribute/dtype dengan value = numerik**, dan jika didalam attribute tersebut merupakan **"non numerik/string"** maka **hanya dapat dicarinya modusnya**. '''
    ''' Didapatkan Central Tendency dimana :
    **Mean  :  27.73,**
    **Median:  27.43, Dan**
    **Modus :  17.24**'''

    '''**Distribusi Data**
    '''
    image = Image.open('01.png')
    st.image(image, caption='Distribusi Data')
    '''1. Mayoritas kumpulan data berada pada tengah-tengah histogram, merepresentasikan bahwa data terindikasi terdistribusi normal''' 
    '''2. Mean lebih besar > median, mencirikan right-skewed namun dengan jarak yang sangat berdekatan artinya dapat juga terindikasi normal distribusion'''
    '''3. Histogram diatas menggambarkan terkait kepadatan/density data dimana terdapat sedikit gaps antara data yang terlihat pada histogram diatas
    **Jika dilihat berdasarkan informasi diatas, terindikasi normal-distribution, dikarenakan nilai antara median dan meannya tidak jauh berbeda**'''

    '''**Nilai Kurtosis dan Skewness**
    Berdasarkan Hasil Analisa didapatkan :'''
    '''**Skewness: 0.40806625079156356, Kurtosis: -0.08196501186333593**'''
    '''**Jika Berdasarkan analisa menggunakan nilai skewness dan kurtosis, data pada parameter Nitrogen dioxide (NO2) menunjukan terdistribusi normal dikarenakan nilai skewenessnya yang berada pada rentang -0.5 dan 0.5 dan menunjukan data tersebut simetris**'''
    image2 = Image.open('02.png')
    st.image(image2, caption='Visualisasi Distribusi Normal')

    image3 = Image.open('03.png')
    st.image(image3, caption='Whisker Box Plot')

    '''**Berdasarkan Visualisasi Box Plot , tidak terdapat outlier pada data tersebut sehingga tidak perlu dilakukan penghilangan outlier pada data tersebut, dikarenakan distribusinya normal**'''
    '''**Hypothesis Testing**'''

    '''Pada bagian ini akan dilakukan uji hipotesis untuk mengetahui **apakah penurunan/perubahan Kualitas Udara dengan parameter Nitrogen dioxide (NO2) yang terjadi setelah pasca covid merupakan penurunan tertinggi di State Illinois dan memiliki perbedaan signifikan dengan Nilai Kualitas Udara dengan rata-rata rentang periode 42 tahun terakhir (1980-2022)** menggunakan two sample t-test dengan significant threshold sebesar 0.05.
    Karena negara bagian Illinois merupakan salah satu negara bagian dengan tingkat Kualitas Udara Tertinggi Pencemarannya maka terutama pada Kualitas Udara terkait Nitrogen dioxide (NO2) maka hipotesisnya adalah :'''
    '''**H0: μ == 27.73178493317029 (Periode Keseluruhan)** Penurunan tidak signifikan'''
    '''**H1: μ != 27.73178493317029**  Penurunan signifikan'''

    '''Didapatkan p-value sejumlah 6.697254555317157e-28, dimana p-value < 0.05 maka H0 ditolak. Berdasarkan hasil tersebut menunjukan bahwa terdapat perbedaan signifikan antara penurunan Nitrogen dioxide (NO2) setelah covid dibandingkan dengan historical rata-rata periode keseluruhan 1980-2022'''
    
