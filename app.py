import streamlit as st
import pandas as pd

# Load Excel data from GitHub repository
excel_url = "https://raw.githubusercontent.com/projectmenia/Romromtrip/main/ram-rom%20%281%29.xlsx"
df = pd.read_excel(excel_url, engine="openpyxl")  # Load the Excel data

# Main App
st.title("Interactive Travel App")

# Create a placeholder to display content conditionally
content_placeholder = st.empty()

# Button to play the video
video_button_clicked = st.button("RomRom bhaiyo Click here")

if video_button_clicked:
    video_url = 'https://github.com/projectmenia/Romromtrip/raw/main/rom-rom-bhaiyo-system-paad-denge-deepak-kalal-meme-template-1280-ytshorts.savetube.me.mp4'
    st.video(video_url)

    # Add a button to proceed after video ends
    see_trip_button = st.button("See your RomRom trip")
    if see_trip_button:
        content_placeholder.empty()  # Clear the video content

        # Date Selection
        if not df.empty:
            unique_dates = df['Date'].dt.strftime("%d %B %Y").unique()
            selected_date = st.selectbox("Select a date", unique_dates)

            if selected_date:
                # Filter data based on selected date
                selected_data = df[df['Date'].dt.strftime("%d %B %Y") == selected_date]

                # Display information
                if not selected_data.empty:
                    st.write(f"Selected Date: {selected_date}")
                    for index, row in selected_data.iterrows():
                        st.write(f"  - Source: {row['source']}")
                        st.write(f"  - Place: {row['destination']}")
                        st.write(f"  - Mode: {row['mode']} - Budget: {row['BUDGET']}")
                        st.write("----")  # Separate different travel details
                else:
                    st.write("No information available for the selected date.")
            else:
                st.write("Please select a date.")
