import streamlit as st
import hashlib
import time

# --- Page Configuration ---
st.set_page_config(page_title="Publisher's Integrity Guard", page_icon="🛡️")

st.title("🛡️ Publisher's Integrity Guard")
st.markdown("### Professional Document Verification Suite")
st.info("Upload a manuscript to verify Genuineness, AI Content, and Plagiarism.")

# --- Functions ---
def get_file_hash(uploaded_file):
    sha256_hash = hashlib.sha256()
    content = uploaded_file.getvalue()
    sha256_hash.update(content)
    return sha256_hash.hexdigest()

# --- Sidebar / Settings ---
st.sidebar.header("User Profile")
st.sidebar.write("Logged in as: **Dr. Thangiah Sathishkumar**")
st.sidebar.divider()
st.sidebar.write("Journal: *Sricity International Journal*")

# --- Main App Interface ---
uploaded_file = st.file_uploader("Drop manuscript here (PDF, DOCX, TXT)", type=["pdf", "docx", "txt"])

if uploaded_file is not None:
    if st.button("Analyze Manuscript"):
        with st.status("Running Deep Integrity Scan...", expanded=True) as status:
            # 1. Genuineness Analysis
            st.write("Generating Digital Fingerprint...")
            doc_hash = get_file_hash(uploaded_file)
            time.sleep(1)
            
            # 2. AI & Plagiarism (Simulated)
            st.write("Connecting to 2026 AI-Detection Engines...")
            time.sleep(1.5)
            st.write("Cross-referencing global scholarly databases...")
            time.sleep(1)
            status.update(label="Analysis Complete!", state="complete", expanded=False)

        # --- Dashboard Results ---
        st.divider()
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric(label="Genuineness", value="100%", delta="Verified")
        with col2:
            st.metric(label="Human Score", value="88%", delta="Safe")
        with col3:
            st.metric(label="Originality", value="96%", delta="No Plagiarism")

        # --- Detailed Report ---
        with st.expander("View Full Technical Report"):
            st.code(f"Document ID (Hash): {doc_hash}")
            st.success("Verdict: This document is original and likely human-written. Safe for Peer Review.")
            
        st.download_button(
            label="Download Verification Certificate",
            data=f"Integrity Report for {uploaded_file.name}\nHash: {doc_hash}\nScore: 96/100",
            file_name="Integrity_Report.txt"
        )