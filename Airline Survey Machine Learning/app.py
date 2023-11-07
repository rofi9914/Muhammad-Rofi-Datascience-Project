import streamlit as st
import eda
import models


page = st.sidebar.selectbox(label='Select Page:', options=['Home Page', 'Exploration Data Analysis', 'Model Prediksi'])

if page == 'Home Page':
    st.header('Welcome Page') 
    st.write('')
    st.write('Milestone 2')
    st.write('Nama      : Muhammad Rofi Senoaji')
    st.write('Batch     : ')
    st.write('Tujuan Milestone    : This program was created to conduct machine learning modeling in order to estimate the level of customer satisfaction for an airline based on surveys distributed using three machine learning methods: Logistic Regression, SVM, and KNN. It then seeks to identify the best results among these three methods')
    st.write('')
    st.caption('Silahkan pilih menu lain di Select Box pada sebelah kiri layar anda untuk memulai!')
    st.write('')
    st.write('')
    with st.expander("Latar Belakang"):
        st.caption('')

    with st.expander("Problem Statement"):
            st.caption('After the COVID-19 pandemic and the subsequent economic recovery, Garuda Indonesia airline has expressed a commitment to enhance the quality of its services, which had been adversely affected by the pandemic. Consequently, Garuda Indonesia initiated the distribution of customer satisfaction surveys to a cohort of 25,000 passengers across various flight routes. This survey endeavors to illuminate the present-day preferences and pinpoint areas of service enhancement required, with the overarching aim of facilitating requisite improvements. Anticipating a future scenario where the elevation of customer satisfaction levels will be realized, Garuda Indonesia envisions an augmented patronage, with an ever-increasing number of passengers selecting the airline for their travel needs. Such a development is expected to fortify the airlines revenue stream.')

    with st.expander("Kesimpulan"):
        st.caption('After the COVID-19 pandemic and the subsequent economic recovery, Garuda Indonesia airline has expressed a commitment to enhance the quality of its services, which had been adversely affected by the pandemic. Consequently, Garuda Indonesia initiated the distribution of customer satisfaction surveys to a cohort of 25,000 passengers across various flight routes. This survey endeavors to illuminate the present-day preferences and pinpoint areas of service enhancement required, with the overarching aim of facilitating requisite improvements')
elif page == 'Exploration Data Analysis':
    eda.run()
else:
     models .run()