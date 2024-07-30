import streamlit as st
import pickle
import pandas as pd
import matplotlib.pyplot as plt

st.title('Prediksi Curah Hujan')

#input
Bulan1 = st.number_input ('Curah Hujan Bulan Pertama', value=0)

Bulan2 = st.number_input ('Curah Hujan Bulan Kedua', value=0)

Bulan3 = st.number_input ('Curah Hujan Bulan Ketiga', value=0)

Tahun = st.number_input ('Tahun')

#code untuk prediksi 
prediksi = ''

#button prediksi
if st.button('Prediksi'):

   prediction = (Bulan1+Bulan2+Bulan3) / 3

   if prediction < 50 :
    hasil_prediksi = 'Curah Hujan Rendah'
   elif prediction == 50:
    hasil_prediksi = 'Curah Hujan Sedang'
   elif prediction >= 50:
    hasil_prediksi = 'Curah Hujan Tinggi'
   else :
    hasil_prediksi = 'Input Error'

   st.write(f"Prediksi: {hasil_prediksi}")
else:
   st.write("Klik Tombol 'Prediksi' untuk Melihat Hasil.")