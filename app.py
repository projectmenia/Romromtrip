import streamlit as st
import pandas as pd

# Load Excel data from GitHub repository
excel_url = "https://raw.githubusercontent.com/projectmenia/Romromtrip/main/ram-rom%20%281%29.xlsx"
df = pd.read_excel(excel_url, engine="openpyxl")  # Load the Excel data

# Main App
st.title("RomRom Trip Planner")

# Create a placeholder to display content conditionally
content_placeholder = st.empty()

# Initialize selected_date to 'Select RomRom Trip Date'
selected_date = 'Select RomRom Trip Date'

# Button to play the video
video_button_clicked = st.button("Watch RomRom Video")

if video_button_clicked:
    video_url = 'https://github.com/projectmenia/Romromtrip/raw/main/rom-rom-bhaiyo-system-paad-denge-deepak-kalal-meme-template-1280-ytshorts.savetube.me.mp4'
    st.video(video_url)

    content_placeholder.empty()  # Clear the video content

    # Reset the selected date to default after video is played
    selected_date = 'Select RomRom Trip Date'

# Date Selection
if not df.empty:
    unique_dates = df['Date'].dt.strftime("%d %B %Y").unique()
    unique_dates = ['Select RomRom Trip Date'] + list(unique_dates)  # Add 'Select RomRom Trip Date' option
    selected_date = st.selectbox("Select a date", unique_dates, index=0 if selected_date == 'Select RomRom Trip Date' else None)

    if selected_date:
        st.markdown("---")  # Add separator line

        if selected_date == 'Select RomRom Trip Date':
            total_budget_all_dates = df['BUDGET'].sum()
            st.write(f"**Total Budget for All Dates:** {total_budget_all_dates}")
        else:
            # Filter data based on selected date
            selected_data = df[df['Date'].dt.strftime("%d %B %Y") == selected_date]

            # Display information
            if not selected_data.empty:
                st.write(f"**Selected Date:** {selected_date}")
                for index, row in selected_data.iterrows():
                    st.markdown(f"**Source:** {row['source']}")
                    st.markdown(f"**Destination:** {row['destination']}")
                    st.markdown(f"**Mode:** {row['mode']} - **Mode Value:** {row['mode_value']}")
                    st.markdown(f"**Where to Stay:** {row['where_to_stay']}")
                    st.markdown(f"**Places to Visit:** {row['places_to_visit']}")
                    st.markdown(f"**Total Budget at Destination:** {row['BUDGET']}")
                    st.markdown("---")  # Add separator line
            else:
                st.warning("No information available for the selected date.")
