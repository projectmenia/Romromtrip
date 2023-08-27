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

# Display summary of travel plans
if not df.empty:
    st.write("Upcoming Travel Plans:")

    # Group by date and display travel details for each date
    grouped = df.groupby('Date')
    for date, group in grouped:
        st.write(f"Date: {date}")
        for index, row in group.iterrows():
            st.write(f"  - Mode of Travel: {row['mode']}")
            st.write(f"  - Source: {row['source']}")
            st.write(f"  - Destination: {row['destination']}")
            
        st.write("----")  # Separate different dates
else:
    st.write("No travel plans available.")
