import pickle
import numpy as np
import streamlit as st

model = pickle.load(open('bank.sav', 'rb'))

st.title('Prediksi Tawaran Pinjaman')
col1, col2, col3 = st.columns(3)

with col1:
    ID = st.number_input('ID Nasabah')
    Income = st.number_input('Pendapatan')
    CCAvg = st.number_input('Rata-rata Pengeluaran Menggunakan Kartu Kredit ($000)')
    Securities_Account = st.number_input('Keamanan Akun (0: Tidak; 1: Ya)')
    CreditCard = st.number_input('Kartu Kredit (0: Tidak; 1: Ya)')


with col2:
    Age = st.number_input('Usia')
    ZIP_Code = st.number_input('Kode Pos')
    Education = st.number_input('Pendidikan (1: Sarjana; 2: Lulus; 3: Tingkat Lanjut/Profesional)')
    CD_Accoount = st.number_input('Deposito (0: Tidak; 1: Ya)')

with col3:
    Experience = st.number_input('Lama Tahun Bekerja')
    Family = st.number_input('Jumlah Keluarga')
    Mortgage = st.number_input('Angsuran KPR (jika ada)($000)')
    Online = st.number_input('M-Banking (0: Tidak; 1: Ya)')

predik = ''
if st.button('Hasil Prediksi'):
    predik = model.predict([[Age, Experience, Income, ZIP_Code, Family, CCAvg, Education, Mortgage]])

    if(predik[0] == 1):
        predik = 'Nasabah menerima tawaran pinjaman personal'
    else:
        predik = 'Nasabah tidak menerima tawaran pinjaman personal'
st.success(predik)