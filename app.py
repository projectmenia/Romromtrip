import streamlit as st
import pandas as pd

# Load Excel data from GitHub repository
excel_url = "https://raw.githubusercontent.com/projectmenia/Romromtrip/main/ram-rom%20%281%29.xlsx"
df = pd.read_excel(excel_url, engine="openpyxl")  # Load the Excel data

# Define custom CSS style
st.markdown(
    """
    <style>
    .selected-date {
        font-size: 28px;
        font-weight: bold;
        color: #4e6bff;
        margin-top: 20px;
    }
    .trip-details {
        font-size: 18px;
        margin-top: 10px;
    }
    .details-item {
        margin-bottom: 5px;
    }
    .budget {
        font-size: 22px;
        font-weight: bold;
        margin-top: 20px;
        color: #ff2e63;
    }
    .emoji {
        font-size: 28px;
        margin-right: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Main App
st.title("RomRom Trip Planner")

# Create a placeholder to display content conditionally
content_placeholder = st.empty()

# Initialize selected_date to 'Select RomRom Trip Date'
selected_date = 'Select RomRom Trip Date'

# Button to play the video
video_button_clicked = st.button("▶️ Watch RomRom Video")

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
    selected_date = st.selectbox("Select RomRom Trip Date", unique_dates, index=0 if selected_date == 'Select RomRom Trip Date' else None)

    if selected_date:
        st.markdown("<hr>", unsafe_allow_html=True)  # Add separator line

        if selected_date == 'Select RomRom Trip Date':
            total_budget_all_dates = df['BUDGET'].sum()
            st.markdown(f'<p class="budget">Total Budget for All Dates: {total_budget_all_dates} 💰</p>', unsafe_allow_html=True)
        else:
            # Filter data based on selected date
            selected_data = df[df['Date'].dt.strftime("%d %B %Y") == selected_date]

            # Display information with improved styling
            if not selected_data.empty:
                st.markdown(f'<p class="selected-date">Selected Date: {selected_date} 🗓️</p>', unsafe_allow_html=True)
                for index, row in selected_data.iterrows():
                    st.markdown(f'<div class="trip-details">'
                                f'<p class="details-item">Source: {row["source"]} 🚀</p>'
                                f'<p class="details-item">Destination: {row["destination"]} 🌴</p>'
                                f'<p class="details-item">Mode: {row["mode"]} 🚂</p>'
                                f'<p class="details-item">Mode Value: {row["mode_value"]} 🚉</p>'
                                f'<p class="details-item">Where to Stay: {row["where_to_stay"]} 🏨</p>'
                                f'<p class="details-item">Places to Visit: {row["places_to_visit"]} 🏖️</p>'
                                f'<p class="details-item">Total Budget at Destination: {row["BUDGET"]} 💰</p>'
                                f'</div>', unsafe_allow_html=True)
            else:
                st.warning("No information available for the selected date.")
