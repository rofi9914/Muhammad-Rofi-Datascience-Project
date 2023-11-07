import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from phik.report import plot_correlation_matrix
from PIL import Image

#membuat function untuk nantinya dipanggil di app.py
def run():
    st.title('Welcome to Explaration Data Analysis')
#Memanggil data csv 
    df = pd.read_csv("D:\\Hacktiv8\\Phase1\\Milestone\\Refrence\\survey_kepuasan_pelanggan.csv")

#menampilakn 5 data teratas
    st.table(df.head(5))


#menampilakn phik matrix
    st.title('Correlation matrix')
    image = Image.open('charts1.png')
    st.image(image, caption='figure 1')

#menampilkan penjelasan 
    with st.expander('Explanation'):
        st.caption('- Variables such as 'departure/arrival_time_convenience,' 'gate_location,' 'departure_delay_in_minutes,' and 'arrival_delay_in_minutes' exert a significant influence on the level of customer satisfaction. 
                   - Conversely, variables 'class' and 'online_boarding' do not appear to have a discernible impact on passenger satisfaction.
                   - Consequently, I intend to remove the 'class' and 'online_boarding' columns from the dataset.
                   - I will also remove the 'customer_type' column from the dataset, as the assessment of passenger air travel frequency on a specific airline is a subjective evaluation'
                   ) 




