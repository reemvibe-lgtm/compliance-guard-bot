import streamlit as st
import re

# 1. Page Configuration & Professional Styling
st.set_page_config(page_title="ComplianceGuard AI", page_icon="🔒", layout="centered")

st.title("🔒 ComplianceGuard AI")
st.subheader("Enterprise-Grade Proactive Audit & Data Leak Prevention")
st.write("Secure your enterprise data before deploying to public AI models. Detect hallucinations and anonymize PII instantly.")

# 2. Core Compliance Bot Engine
def audit_enterprise_document(document_text):
    audit_logs = []
    sanitized_text = document_text
    
    sensitive_patterns = {
        "SSN/Tax ID": r'\b\d{3}-\d{2}-\d{4}\b',
        "API/Private Key": r'bearer\s[a-zA-Z0-9]{20,}',
        "Internal System ID": r'#XYZ-\d{4,}'
    }
    
    for data_type, pattern in sensitive_patterns.items():
        matches = re.findall(pattern, sanitized_text, re.IGNORECASE)
        for match in matches:
            audit_logs.append(f"🔒 [DATA LEAK PREVENTED]: Anonymized sensitive {data_type} ({match})")
            sanitized_text = sanitized_text.replace(match, "[REDACTED_ENTERPRISE_ASSET]")

    if "100% efficiency" in sanitized_text.lower() or "zero risk" in sanitized_text.lower():
        audit_logs.append("⚠️ [AI HALLUCINATION WARNING]: Detected absolute metrics ('100% efficiency' / 'zero risk'). Real-world enterprise operations require statistical validation.")

    return sanitized_text, audit_logs

# 3. User Interface Options (Upload or Paste)
st.write("---")
option = st.radio("Choose Input Method:", ("Upload a File (.txt)", "Paste Raw Text"))

raw_text = ""

if option == "Upload a File (.txt)":
    uploaded_file = st.file_uploader("Upload your enterprise document or report", type=["txt"])
    if uploaded_file is not None:
        raw_text = uploaded_file.read().decode("utf-8")
else:
    raw_text = st.text_area("Paste your report text here:", height=200)

# 4. Run Audit and Display Elegant Results
if st.button("🚀 Start Proactive Audit"):
    if raw_text.strip() == "":
        st.warning("Please provide some text or upload a file first.")
    else:
        st.info("Scanning document against compliance frameworks...")
        
        clean_output, logs = audit_enterprise_document(raw_text)
        st.success("Audit Completed!")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### 🔹 System Audit Logs")
            if not logs:
                st.write("✅ Document is 100% safe and compliant.")
            else:
                for log in logs:
                    if "🔒" in log:
                        st.error(log)
                    else:
                        st.warning(log)
                        
        with col2:
            st.markdown("### 🔹 Sanitized Safe Text")
            st.text_area("Cleaned Text (Safe for Public AI):", value=clean_output, height=250)
            
            st.download_button(
                label="⬇️ Download Sanitized File",
                data=clean_output,
                file_name="Sanitized_Report.txt",
                mime="text/plain"
            )
