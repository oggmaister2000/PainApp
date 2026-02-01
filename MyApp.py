import streamlit as st
from datetime import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

st.title("🩺 Pain Tracker (Google Drive)")

# --- Slider + Notes ---
pain = st.slider("Pain level (0–10)", 0, 10)
notes = st.text_area("Notes (optional)")

# --- Save button ---
if st.button("Save entry"):
    # Google Sheets authentication
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name(
        "service_account.json",  # Make sure your JSON file is here
        scope
    )
    client = gspread.authorize(creds)

    # Open your specific Google Sheet
    sheet = client.open_by_key("1k_xWxkti05a8sGoGfBtzIYfk2S7rHW8tyI-ShzQdYbY").sheet1

    # Append a new row
    row = [datetime.now().strftime("%Y-%m-%d %H:%M:%S"), pain, notes]
    sheet.append_row(row)

    st.success("Entry saved to Google Drive ✅")

# --- Optional: show all previous entries ---
st.subheader("Your previous entries")
try:
    sheet_data = sheet.get_all_records()
    if sheet_data:
        df = pd.DataFrame(sheet_data)
        st.dataframe(df)
except Exception as e:
    st.info("No entries yet or failed to load.")
