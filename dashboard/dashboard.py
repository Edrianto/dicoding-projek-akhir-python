import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import path

dir = path.Path(__file__).abspath()
sys.path.append(dir.parent.parent)

path_to_dataset = "./workspaces/dicoding-projek-akhir-python/dashboard/day.csv"

df_day = pd.read_csv(path_to_dataset, delimiter=",")

def daily_rentals():    
    st.header('Daily Rentals')

    fig, ax = plt.subplots(figsize=(16, 8))
    ax.plot(
        df_day["instant"],
        df_day["cnt"],
        marker='o', 
        linewidth=2,
        color="#90CAF9"
    )
    ax.tick_params(axis='y', labelsize=20)
    ax.tick_params(axis='x', labelsize=15)
    
    st.pyplot(fig)

def max_count_per_year():
    st.header('Max count per year')

    fig, ax = plt.subplots()

    sns.barplot(x="yr", y="cnt", data=df_day)

    labels = [item.get_text() for item in ax.get_xticklabels()]
    labels[0] = '2011'
    labels[1] = '2012'

    ax.set_ylabel("Rental Count")
    ax.set_xlabel("Year")
    ax.set_xticklabels(labels)

    st.pyplot(fig)

def holiday_rentals():
    st.header('Effect of holiday on rental count')

    fig, ax = plt.subplots()

    sns.barplot(x="holiday", y="cnt", data=df_day)

    labels = [item.get_text() for item in ax.get_xticklabels()]
    labels[0] = 'Normal day'
    labels[1] = 'Holiday'

    ax.set_ylabel("Rental Count")
    ax.set_xticklabels(labels)

    st.pyplot(fig)

st.title('-= Analisis Bike Sharing Dataset =-')
daily_rentals()
max_count_per_year()
holiday_rentals()
