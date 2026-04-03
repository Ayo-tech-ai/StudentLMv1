import streamlit as st

st.set_page_config(page_title="StudyLM", page_icon="📘", layout="wide")

# --- SKY BLUE LANDING UI ---
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #38bdf8, #0ea5e9);
    text-align: center;
}
.title {
    font-size: 60px;
    font-weight: bold;
    color: white;
    margin-top: 100px;
}
.subtitle {
    font-size: 20px;
    color: white;
    margin-bottom: 40px;
}
.feature {
    background: white;
    padding: 20px;
    border-radius: 12px;
    margin: 10px;
    font-weight: bold;
}
.stButton > button {
    background: #0284c7;
    color: white;
    border-radius: 10px;
    padding: 10px 20px;
    font-size: 18px;
}
</style>
""", unsafe_allow_html=True)

# --- TITLE ---
st.markdown('<div class="title">📘 StudyLM</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Your AI-powered study companion</div>', unsafe_allow_html=True)

# --- FEATURES ---
col1, col2, col3, col4 = st.columns(4)

col1.markdown('<div class="feature">📘 Learn<br><small>Understand your material</small></div>', unsafe_allow_html=True)
col2.markdown('<div class="feature">🧠 Key Ideas<br><small>Quick summaries</small></div>', unsafe_allow_html=True)
col3.markdown('<div class="feature">🎯 Practice<br><small>Test yourself</small></div>', unsafe_allow_html=True)
col4.markdown('<div class="feature">⚡ Exam Cram<br><small>Revise fast</small></div>', unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# --- BUTTON ---
if st.button("🚀 Get Started"):
    st.switch_page("pages/Study.py")
