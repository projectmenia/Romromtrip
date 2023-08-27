import streamlit as st
import pandas as pd

# Load Excel data from GitHub repository
excel_url = 'https://github.com/projectmenia/Romromtrip/blob/3e24a04a23a993148c4c38f0edeff3d254a19f81/ram-rom.xlsx'
df = pd.read_excel(excel_url,engine='openpyxl')

# Video Pop-up
video_url = 'https://github.com/projectmenia/Romromtrip/raw/main/rom-rom-bhaiyo-system-paad-denge-deepak-kalal-meme-template-1280-ytshorts.savetube.me.mp4'
video_button_clicked = st.button("RomRom bhaiyo Click here")
if video_button_clicked:
    st.video(video_url)

# Main App
st.title("Travel Planner App")

# Date Selection
min_date = df['Date'].min()
max_date = df['Date'].max()
selected_date = st.date_input("Select a date", min_value=min_date, max_value=max_date)

# Filter data based on selected date
selected_data = df[df['Date'] == selected_date]

# Display information
if not selected_data.empty:
    st.write(f"Date: {selected_date}")
    st.write(f"Source: {selected_data['source'].values[0]}")
    st.write(f"Destination: {selected_data['destination'].values[0]}")
    st.write(f"Mode of Travel: {selected_data['mode'].values[0]}")
    st.write(f"Where to Stay: {selected_data['where_to_stay'].values[0]}")
    # Add more information as needed

    # Display map if location data is available (assuming 'latitude' and 'longitude' columns)
    if 'latitude' in selected_data.columns and 'longitude' in selected_data.columns:
        st.map(selected_data[['latitude', 'longitude']])

    # Display budget information
    st.write(f"Budget: {selected_data['BUDGET'].values[0]}")
else:
    st.write("No information available for the selected date.")

# You can add more interactive elements, styling, and enhancements as needed
