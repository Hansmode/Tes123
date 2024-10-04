import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
@st.cache_data
def load_data():
    return pd.read_csv("https://raw.githubusercontent.com/Hansmode/T2B/refs/heads/main/day.csv")

# Main function
def main():
    st.title("Bike Sharing Data Visualization")

    # Load the data
    customers_df = load_data()

    # Data cleaning
    customers_df.drop_duplicates(inplace=True)

    # Visualization 1: Average bike rentals by season
    st.subheader('Rata-rata Jumlah Peminjam Sepeda Berdasarkan Season')
    avg_rentals_season = customers_df.groupby(by="season")["cnt"].mean().reset_index()

    fig1, ax1 = plt.subplots(figsize=(10, 6))
    sns.barplot(x="season", y="cnt", data=avg_rentals_season, palette="coolwarm", ax=ax1)
    ax1.set_title('Rata-rata Jumlah Peminjam Sepeda Berdasarkan Season', fontsize=14)
    ax1.set_xlabel('Season', fontsize=12)
    ax1.set_ylabel('Rata-rata Jumlah Peminjam', fontsize=12)
    ax1.set_xticklabels(['1', '2', '3', '4'])
    ax1.grid(True)

    st.pyplot(fig1)

    # Visualization 2: Total registered users by year
    st.subheader('Total Peminjam Terdaftar Berdasarkan Tahun')
    total_registered_year = customers_df.groupby(by="yr")["registered"].sum().reset_index()

    fig2, ax2 = plt.subplots(figsize=(10, 6))
    sns.barplot(x='yr', y='registered', data=total_registered_year, palette='coolwarm', ax=ax2)
    ax2.set_title('Total Peminjam Terdaftar Berdasarkan Tahun', fontsize=16)
    ax2.set_xlabel('Tahun', fontsize=12)
    ax2.set_ylabel('Total Peminjam Terdaftar', fontsize=12)

    st.pyplot(fig2)

if __name__ == "__main__":
    main()
