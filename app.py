import streamlit as st

st.set_page_config(
    page_title="Resume Improvement Suggestions",
    page_icon="📄",
    layout="centered"
)

st.markdown("""
<style>

/* Main background */
.stApp {
    background: linear-gradient(135deg, #c7d2fe, #fbcfe8);
}

/* Main title */
h1 {
    text-align: center;
    color: #312e81 !important;
    font-size: 38px;
    font-weight: bold;
}

/* Subtitle */
.subtitle {
    text-align: center;
    color: #4338ca;
    font-size: 18px;
    margin-bottom: 25px;
}

/* Labels */
label {
    color: #312e81 !important;
    font-weight: bold !important;
}

/* Text input */
.stTextInput input {
    background-color: #ede9fe !important;
    color: #1e1b4b !important;
    border: 2px solid #8b5cf6 !important;
    border-radius: 10px !important;
}

/* Text area */
.stTextArea textarea {
    background-color: #ede9fe !important;
    color: #1e1b4b !important;
    border: 2px solid #8b5cf6 !important;
    border-radius: 10px !important;
}

/* File uploader */
[data-testid="stFileUploader"] {
    background-color: #ede9fe !important;
    border: 2px solid #8b5cf6 !important;
    border-radius: 12px !important;
    padding: 10px !important;
}

/* File uploader text */
[data-testid="stFileUploader"] * {
    color: #312e81 !important;
}

/* Button */
.stButton > button {
    width: 100%;
    background-color: #7c3aed !important;
    color: white !important;
    border: none !important;
    border-radius: 10px !important;
    padding: 12px !important;
    font-size: 18px !important;
    font-weight: bold !important;
}

.stButton > button:hover {
    background-color: #6d28d9 !important;
}

/* Success message */
[data-testid="stAlert"] {
    border-radius: 10px;
}

/* Suggestions */
.suggestion-box {
    background-color: #e0e7ff;
    color: #1e1b4b;
    padding: 20px;
    border-radius: 15px;
    border-left: 6px solid #7c3aed;
    margin-top: 20px;
}

</style>
""", unsafe_allow_html=True)


# Title
st.title("📄 Resume Improvement Suggestions")

st.markdown(
    '<div class="subtitle">Improve your resume with simple and useful suggestions</div>',
    unsafe_allow_html=True
)


# Name
name = st.text_input("👤 Enter your name")

# Resume
resume = st.file_uploader(
    "📄 Upload your resume",
    type=["pdf", "docx", "txt"]
)

# Job role
job_role = st.text_input(
    "💼 Enter your target job role"
)

# Skills
skills = st.text_area(
    "🛠️ Enter your skills",
    height=100
)


# Button
if st.button("✨ Get Improvement Suggestions"):

    if name == "" or resume is None or job_role == "" or skills == "":
        st.error("❌ Please fill all the fields.")

    else:
        st.success("✅ Resume uploaded successfully!")

        st.markdown("""
        <div class="suggestion-box">

        <h3>💡 Resume Improvement Suggestions</h3>

        <p>✅ Add a clear career objective.</p>
        <p>✅ Highlight skills related to your target job.</p>
        <p>✅ Add your academic and personal projects.</p>
        <p>✅ Mention relevant certifications.</p>
        <p>✅ Use clear and professional language.</p>
        <p>✅ Check grammar and spelling.</p>
        <p>✅ Keep the resume simple and well organized.</p>

        </div>
        """, unsafe_allow_html=True)