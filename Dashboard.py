import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Proyek Akhir Analisis Data Dhafindra')
st.text('Selamat datang di Dashboard laporan Proyek Akhir Analisis Data Dhafindra.')

st.header('Dataset')
df = pd.read_csv('day.csv')
st.dataframe(data=df, width=900, height=300)
st.caption('Bike Sharing Dataset')

st.header('Pertanyaan Bisnis')
st.markdown('''
    1. Apakah jumlah sepeda yang disewa lebih banyak di hari libur atau di hari kerja?
    2. Pada Bulan apa sepeda paling banyak di sewa?
    ''')

tab1, tab2, tab3= st.tabs(["Data Wrangling", "Exploratory Data Analysis", "Visualization & Explanatory Analysis"])

with tab1:
    st.header('Data Wrangling')
    st.subheader('Gathering Data')
    st.subheader('Assessing Data')
    st.subheader('Cleaning Data')

with tab2:
    st.header('Exploratory Data Analysis')
    tab21, tab22, tab23= st.tabs(["Korelasi Data", "Jumlah Penyewaan Berdasarkan Tipe Hari", "Jumlah Penyewaan Berdasarkan Bulan"])

    with tab21:
        st.subheader('Korelasi data setelah dibersihkan')
        # Memilih kolom yang numerik saja
        numeric_columns = df.select_dtypes(include=['int64', 'float64']).columns

        # Hitung korelasi kolom-kolom tersebut
        corr = df[numeric_columns].corr()
        
        # Buat Heatmap korelasi tersebut
        plt.figure(figsize=(10, 8))
        sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
        plt.title('Correlation Heatmap')
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()  # Display the heatmap in Streamlit

    with tab22:
        # Kelompokkan data berdasarkan 'workingday' dan hitung jumlah 'cnt' dari setiap kelompok
        cnt_by_workingday = df.groupby('workingday')['cnt'].sum()

        st.write(cnt_by_workingday)

    with tab23:
        # Konversi dteday menjadi datetime
        # Ini dilakukan karena kita hanya akan melihat banyak sewaan berdasarkan bulan
        df['dteday'] = pd.to_datetime(df['dteday'])

        #Ambil bulan dari 'dteday'
        df['month'] = df['dteday'].dt.month

        # Melihat jumlah total sewaan di setiap bulan
        monthly_cnt = df.groupby('month')['cnt'].sum()
        st.write(monthly_cnt)




with tab3:
    st.header('Visualization & Explanatory Analysis')
    st.subheader('Pertanyaan 1')
    # Group data by 'workingday' and calculate the sum of 'cnt'
    cnt_by_workingday = df.groupby('workingday')['cnt'].sum()

    # Create a Streamlit app
    st.text('Jumlah Penyewaan Berdasarkan Hari Kerja')
    st.bar_chart(cnt_by_workingday)

    st.subheader('Pertanyaan 2')
    # Konversi dteday menjadi datetime
    df['dteday'] = pd.to_datetime(df['dteday'])

    # Ambil bulan dari 'dteday'
    df['month'] = df['dteday'].dt.month

    monthly_cnt = df.groupby('month')['cnt'].sum()

    # Create a Streamlit app
    st.text('Jumlah Total Berdasarkan Bulan')
    st.line_chart(monthly_cnt)


st.header('Conclusion')
st.markdown('''
            - Conclusion Pertanyaan 1:
                sepeda jauh lebih banyak disewa pada hari kerja dibandingkan hari libur.

            - Conclusion Pertanyaan 2:
                penyewaan sepeda paling banyak terjadi di bulan ke-7 atau bulan Juli.
            ''')
