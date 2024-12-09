import streamlit as st
import pandas as pd

# Load the dataset
st.title("Smart Parking System")
data = pd.read_csv('Dataset/parking_sensor_data.csv')

# Display basic information
st.write("### Parking Sensor Data")
st.write(data)

# Filter the data based on user input
status = st.selectbox("Select parking status", ("Present", "Unoccupied"))
filtered_data = data[data["Status_Description"] == status]

# Display filtered data
st.write(f"### Parking Spaces with status '{status}'")
st.write(filtered_data)
