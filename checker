import streamlit as st
import re

# Define codes and their full descriptions
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

# Phrase fragments (lowercase) to help fuzzy match descriptions
WARNING_PATTERNS = {
    "P1": "discriminatory language",
    "P2": "discriminatory content",
    "P3": "discriminatory language and content",
    "V1": "some violent scenes",
    "V2": "prolonged violent scenes",
    "V3": "graphic violent scenes",
    "V4": "scenes of sexual violence",
    "L1": "some strong language",
    "L2": "strong language",  # fallback if L1 not matched
    "L3": "very strong language",
    "LA": "adult humour",
    "D1": "some scenes which some viewers may find upsetting",
    "D2": "scenes which some viewers may find upsetting",
    "D3": "scenes which some viewers may find disturbing",
    "S1": "some scenes of a sexual nature",
    "S2": "scenes of a sexual nature",
    "S3": "explicit sexual scenes",
    "RFI": "repetitive flashing images",
    "T1": "deals with suicide",
    "T2": "deals with self-harm",
    "T3": "deals with sexual abuse",
    "T4": "deals with eating disorders"
}

def detect_warnings_in_text(text):
    found = []
    for code, phrase in WARNING_PATTERNS.items():
        if re.search(re.escape(phrase), text, re.IGNORECASE):
            found.append((code, WARNING_CODES[code]))
    return found

# Streamlit UI
st.set_page_config(page_title="EBU STL Warning Checker", layout="wide")
st.title("🔍 EBU STL Warning Code Scanner")

uploaded_files = st.file_uploader("Upload one or more STL files", type=["stl"], accept_multiple_files=True)

if uploaded_files:
    st.subheader("📋 Scan Results")

    for file in uploaded_files:
        content = file.read().decode(errors="ignore")

        warnings_found = detect_warnings_in_text(content)

        with st.expander(f"📄 {file.name}"):
            if warnings_found:
                st.success(f"{len(warnings_found)} warning(s) found:")
                for code, desc in warnings_found:
                    st.markdown(f"- **{code}** — {desc}")
            else:
                st.info("✅ No warnings found.")

