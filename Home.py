import streamlit as st

st.set_page_config(page_title="StudyLM", page_icon="📘", layout="wide")

# --- SKY BLUE + CENTERED UI ---
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #38bdf8, #0ea5e9);
}

/* Center everything */
.main {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}

/* Title */
.title {
    font-size: 64px;
    font-weight: 800;
    color: white;
    text-align: center;
    margin-top: 80px;
}

/* Subtitle */
.subtitle {
    font-size: 20px;
    color: white;
    text-align: center;
    margin-bottom: 40px;
    opacity: 0.95;
}

/* Feature cards */
.feature {
    background: white;
    padding: 18px;
    border-radius: 14px;
    text-align: center;
    font-weight: 600;
    box-shadow: 0 6px 20px rgba(0,0,0,0.15);
    transition: 0.2s;
}

.feature:hover {
    transform: translateY(-5px);
}

/* Button */
.stButton > button {
    background: #0284c7;
    color: white;
    border-radius: 10px;
    padding: 12px 28px;
    font-size: 18px;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

# --- TOP FEATURES (ROW 1) ---
col1, col2, col3 = st.columns([1,2,1])

with col1:
    st.markdown('<div class="feature">📘 Learn<br><small>Understand your material</small></div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="feature">🧠 Key Ideas<br><small>Quick summaries</small></div>', unsafe_allow_html=True)

# --- CENTER TITLE ---
st.markdown('<div class="title">📘 StudyLM</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Your AI assistant for smarter learning</div>', unsafe_allow_html=True)

# --- BOTTOM FEATURES (ROW 2) ---
col4, col5, col6 = st.columns([1,2,1])

with col4:
    st.markdown('<div class="feature">🎯 Practice<br><small>Test yourself</small></div>', unsafe_allow_html=True)

with col6:
    st.markdown('<div class="feature">⚡ Exam Cram<br><small>Revise fast</small></div>', unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# --- CTA BUTTON ---
col_btn1, col_btn2, col_btn3 = st.columns([2,1,2])

with col_btn2:
    if st.button("🚀 Get Started"):
        st.switch_page("pages/Study.py")
