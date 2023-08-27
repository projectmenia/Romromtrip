import streamlit as st
import pandas as pd

# Load Excel data from GitHub repository
excel_url = "https://raw.githubusercontent.com/projectmenia/Romromtrip/main/ram-rom%20%281%29.xlsx"
df = pd.read_excel(excel_url, engine="openpyxl")  # Load the Excel data

# Video Pop-up (autoplay)
video_url = 'https://github.com/projectmenia/Romromtrip/raw/main/rom-rom-bhaiyo-system-paad-denge-deepak-kalal-meme-template-1280-ytshorts.savetube.me.mp4'
st.video(video_url, start_time=0)  # Set start_time=0 to autoplay

# Main App
st.title("Interactive Travel App")

# Date Selection
if not df.empty:
    unique_dates = df['Date'].dt.strftime("%d %B %Y").unique()
    selected_date = st.selectbox("Select a date", unique_dates)

    # Filter data based on selected date
    selected_data = df[df['Date'].dt.strftime("%d %B %Y") == selected_date]

    # Display information
    if not selected_data.empty:
        st.write(f"Selected Date: {selected_date}")
        for index, row in selected_data.iterrows():
            st.write(f"  - Source: {row['source']}")
            st.write(f"  - Destination: {row['destination']}")
            st.write(f"  - Mode of Travel: {row['mode']}")
            st.write(f"  - Budget: {row['BUDGET']}")
            st.write("----")  # Separate different travel details
    else:
        st.write("No information available for the selected date.")
else:
    st.write("No travel plans available.")
