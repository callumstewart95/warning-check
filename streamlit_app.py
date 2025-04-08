import streamlit as st
import re
import pandas as pd

# Warning descriptions
WARNING_CODES = {
    "P1": "Contains discriminatory language which some may find offensive",
    "P2": "Contains discriminatory content which some may find offensive",
    "P3": "Contains discriminatory language and content some may find offensive",
    "V1": "This programme/ film contains some violent scenes",
    "V2": "This programme/ film contains prolonged violent scenes",
    "V3": "This programme/ film contains graphic violent scenes",
    "V4": "This programme/ film contains scenes of sexual violence",
    "L1": "This programme/ film contains some strong language",
    "L2": "This programme/ film contains strong language",
    "L3": "This programme/ film contains very strong language",
    "LA": "This programme/ film contains adult humour",
    "D1": "This programme/ film contains some scenes which some viewers may find upsetting",
    "D2": "This programme/ film contains scenes which some viewers may find upsetting",
    "D3": "This programme/ film contains scenes which some viewers may find disturbing",
    "S1": "This programme/ film contains some scenes of a sexual nature",
    "S2": "This programme/ film contains scenes of a sexual nature",
    "S3": "This programme/ film contains explicit sexual scenes",
    "RFI": "This programme/ film contains scenes of Repetitive Flashing Images",
    "T1": "This programme/film deals with Suicide",
    "T2": "This programme/film deals with Self-Harm",
    "T3": "This programme/film deals with Sexual Abuse",
    "T4": "This programme/film deals with Eating Disorders"
}

# Prioritized phrases to avoid false matches
PRIORITY_PATTERNS = [
    ("L3", "very strong language"),
    ("L1", "some strong language"),
    ("L2", "strong language"),
    ("LA", "adult humour"),
    ("P3", "discriminatory language and content"),
    ("P1", "discriminatory language"),
    ("P2", "discriminatory content"),
    ("V4", "scenes of sexual violence"),
    ("V3", "graphic violent scenes"),
    ("V2", "prolonged violent scenes"),
    ("V1", "some violent scenes"),
    ("D3", "scenes which some viewers may find disturbing"),
    ("D1", "some scenes which some viewers may find upsetting"),
    ("D2", "scenes which some viewers may find upsetting"),
    ("S3", "explicit sexual scenes"),
    ("S1", "some scenes of a sexual nature"),
    ("S2", "scenes of a sexual nature"),
    ("RFI", "repetitive flashing images"),
    ("T3", "deals with sexual abuse"),
    ("T1", "deals with suicide"),
    ("T2", "deals with self-harm"),
    ("T4", "deals with eating disorders"),
]

def detect_warnings_precise(text):
    found = set()
    clean_text = text.lower()

    for code, phrase in PRIORITY_PATTERNS:
        if phrase in clean_text and code not in found:
            found.add(code)

    return [(code, WARNING_CODES[code]) for code in found]

# Streamlit UI
st.set_page_config(page_title="EBU STL Batch Warning Scanner", layout="wide")
st.title("🎬 EBU STL Warning Checker")

uploaded_files = st.file_uploader("Upload STL files", type=["stl"], accept_multiple_files=True)

results = []

if uploaded_files:
    st.subheader("🔎 Scan Summary")

    for file in uploaded_files:
        content = file.read().decode(errors="ignore")
        found = detect_warnings_precise(content)

        if found:
            for code, desc in found:
                results.append({
                    "Filename": file.name,
                    "Warning Code": code,
                    "Description": desc
                })
        else:
            results.append({
                "Filename": file.name,
                "Warning Code": "None",
                "Description": "No warnings found"
            })

    df = pd.DataFrame(results)
    st.dataframe(df, use_container_width=True)

    # CSV download
    csv = df.to_csv(index=False)
    st.download_button("📥 Download CSV Report", data=csv, file_name="stl_warnings_report.csv", mime="text/csv")

else:
    st.info("Upload one or more `.stl` files to begin.")
