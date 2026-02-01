import streamlit as st
import pandas as pd
from datetime import datetime
from pathlib import Path

st.title("🩺 Pain Tracker")

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)
DATA_FILE = DATA_DIR / "pain_log.csv"

st.subheader("Log your pain")

pain = st.slider("Pain level (0 = none, 10 = worst)", 0, 10)
notes = st.text_area("Notes (optional)")

if st.button("Save entry"):
    entry = pd.DataFrame([{
        "timestamp": datetime.now(),
        "pain": pain,
        "notes": notes
    }])

    if DATA_FILE.exists():
        entry.to_csv(DATA_FILE, mode="a", header=False, index=False)
    else:
        entry.to_csv(DATA_FILE, index=False)

    st.success("Entry saved ✅")
