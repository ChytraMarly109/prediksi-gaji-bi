1  import streamlit as st
2  import joblib 
3  import numpy as np
4
5  # Membuat model regresi linear yang sudah disimpan
6  lin_reg_loaded = joblib.load('lin_reg_model.joblib')
7 
8  # Judul aplikasi
9  st.title("Prediksi Gaji Berdasarkan Lama Bekerja")
10 
11 # Input tahun pengalaman kerja
12 years_exprerience = st.number_input("Masukkan jumlah tahun bekerja:", min_value=0.0, step=0.1)
13 
14 # Prediksi gaji
15 if st.button("Prediksi Gaji"):
16	gaji = lin_reg_loaded.predict([[years_experience]])
17	st.write(f"Gaji seseorang setelah bekerja selama {years_experience} tahun adalah ${gaji[0]:,.2f}")
