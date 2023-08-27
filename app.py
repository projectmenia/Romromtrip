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
        font-size: 24px;
        font-weight: bold;
        color: #4e6bff;
        margin-top: 20px;
    }
    .trip-details {
        font-size: 16px;
        background-color: #f7f7f7;
        padding: 10px;
        border-radius: 5px;
        box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);
        margin-top: 10px;
    }
    .details-item {
        margin-bottom: 5px;
        color: #333333;
    }
    .budget {
        font-size: 20px;
        font-weight: bold;
        margin-top: 20px;
        color: #ff2e63;
    }
    .emoji {
        font-size: 18px;
        margin-right: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Main App
st.title("RomRom Trip Planner")

# Video Pop-up
video_url = 'https://github.com/projectmenia/Romromtrip/raw/main/rom-rom-bhaiyo-system-paad-denge-deepak-kalal-meme-template-1280-ytshorts.savetube.me.mp4'
video_button_clicked = st.button("RomRom bhaiyo Click here")
if video_button_clicked:
    st.video(video_url, start_time=0, format="video/mp4")

# Date Selection
if not df.empty:
    unique_dates = df['Date'].dt.strftime("%d %B %Y").unique()
    selected_date = st.selectbox("Select RomRom Trip Date", unique_dates, index=0)

    if selected_date != "Select RomRom Trip Date":
        st.markdown("---")  # Add separator line

        # Filter data based on selected date
        selected_data = df[df['Date'].dt.strftime("%d %B %Y") == selected_date]

        # Display information with improved styling
        if not selected_data.empty:
            st.markdown(f'<p class="selected-date">Selected Date: {selected_date}</p>', unsafe_allow_html=True)
            for index, row in selected_data.iterrows():
                expander = st.beta_expander(
                    f"📅 {row['Date']}, 🏞️ {row['destination']}",
                    expanded=True
                )
                with expander:
                    st.markdown(f"**Source:** {row['source']}")
                    st.markdown(f"**Mode:** {row['mode']} ({row['mode_value']})")
                    st.markdown(f"**Where to Stay:** {row['where_to_stay']}")
                    st.markdown(f"**Places to Visit:** {row['places_to_visit']}")
                    st.markdown(f"**Total Budget at Destination:** {row['BUDGET']}")

        else:
            st.warning("No information available for the selected date.")
