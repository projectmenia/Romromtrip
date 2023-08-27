import streamlit as st
import pandas as pd

# Load Excel data from GitHub repository
excel_url = "https://raw.githubusercontent.com/projectmenia/Romromtrip/main/ram-rom%20%281%29.xlsx"
df = pd.read_excel(excel_url, engine="openpyxl")  # Load the Excel data

# Video Pop-up
video_url = 'https://github.com/projectmenia/Romromtrip/raw/main/rom-rom-bhaiyo-system-paad-denge-deepak-kalal-meme-template-1280-ytshorts.savetube.me.mp4'
video_button_clicked = st.button("RomRom bhaiyo Click here")
if video_button_clicked:
    st.video(video_url)

# Main App
st.title("Travel Planner App")

# Display information
if not df.empty:
    for index, row in df.iterrows():
        st.write(f"Date: {row['Date']}")
        st.write(f"Source: {row['source']}")
        st.write(f"Destination: {row['destination']}")
        st.write(f"Mode of Travel: {row['mode']}")
        
        # Check if 'where_to_stay' column exists before accessing it
        if 'where_to_stay' in df.columns:
            st.write(f"Where to Stay: {row['where_to_stay']}")
        
        # Add more information as needed

        # Display map if location data is available (assuming 'latitude' and 'longitude' columns)
        if 'latitude' in df.columns and 'longitude' in df.columns:
            st.map(df[['latitude', 'longitude']])

        # Display budget information
        st.write(f"Budget: {row['BUDGET']}")

    st.write("End of data.")
else:
    st.write("No information available.")
