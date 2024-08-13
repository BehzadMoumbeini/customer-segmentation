import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# import the data
data = pd.read_csv('../segmented_customers.csv')


# Sidebar for cluster selection
cluster_choice = st.sidebar.selectbox('Select Cluster', data['Cluster'].unique())


# Filter data by selected cluster
filtered_data = data[data['Cluster'] == cluster_choice]


# Display selected data
st.write(f"Displaying data for Cluster {cluster_choice}")
st.write(filtered_data)


# Pairplot of the selected cluster
st.write("Pairplot of the selected cluster")
sns.pairplot(filtered_data.drop(['CustomerID'], axis=1), palette='Set2')
st.pyplot(plt)


