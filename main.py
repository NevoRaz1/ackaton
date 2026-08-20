import streamlit as st
st.set_page_config(
    page_title="ממשק של כיתת  אקסטרא",
    page_icon="67",
    layout="centered")
st.markdown("""
    <style>
    .stApp {
        direction: rtl;
        text-align: right;
    }
    label, .stTextInput, .stSelectbox {
        direction: rtl;
        text-align: right;
    }
    .main-title {
        text-align: center;
        font-size: 2.5rem;
        font-weight: 700;
        color: #1E293B;
        margin-bottom: 0.5rem;
    }
    .sub-title {
        text-align: center;
        font-size: 1.2rem;
        color: #64748B;
        margin-bottom: 2rem;
    }
    div.stButton > button {
        width: 100%;
        height: 70px;
        font-size: 20px !important;
        font-weight: 600 !important;
        border-radius: 12px !important;
        border: 2px solid #3B82F6 !important;
        background-color: #EFF6FF !important;
        color: #1D4ED8 !important;
        transition: all 0.3s ease !important;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.05) !important;
    }
    div.stButton > button:hover {
        background-color: #3B82F6 !important;
        color: white !important;
        transform: translateY(-2px);
        box-shadow: 0px 6px 15px rgba(59, 130, 246, 0.3) !important;
    }
    </style>
""", unsafe_allow_html=True)
st.markdown('<div class="main-title">ברוכים הבאים למערכת</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">בחר אחת מהאפשרויות הבאות כדי להמשיך</div>', unsafe_allow_html=True)

if 'selected_option' not in st.session_state:
    st.session_state.selected_option = None
_, col1, col2, _ = st.columns([1, 2, 2, 1])
with col1:
    if st.button("יצירת שיעור"):
        st.session_state.selected_option = "option1"
with col2:
    if st.button("כניסה לשיעור"):
        st.session_state.selected_option = "option2"
st.markdown("<br>", unsafe_allow_html=True)
if st.session_state.selected_option == "option1":
    st.success("בחרת באפשרות הראשונה!")
    with st.form("create_lesson_form"):
        st.markdown("<h3 style='text-align: center;'>יצירת שיעור</h3>", unsafe_allow_html=True)
        teacher_name = st.text_input("שם המורה")
        password = st.text_input("סיסמא", type="password")
        lesson_name = st.text_input("שם שיעור")
        lesson_code = st.text_input("קוד שיעור ")
        duration = st.text_input("משך השיעור")
        nispah = st.text_input("נספחים")
        
        submitted = st.form_submit_button("צור שיעור")
        if submitted:
            if not teacher_name or not lesson_code or not duration or not password:
                st.error("נא למלא את כל השדות")
            else:
                st.success("השיעור נוצר ")
elif st.session_state.selected_option == "option2":
    st.success("בחרת באפשרות השנייה!")
    with st.form("join_lesson_form"):
        st.markdown("<h3 style='text-align: center;'>כניסה לשיעור</h3>", unsafe_allow_html=True)
        teacher_name = st.text_input("שם המורה")
        lesson_code = st.text_input("קוד שיעור")
        password = st.text_input("סיסמה ", type="password")
        identity = st.selectbox("את/ה מורה או תלמיד/ה:",options=["student", "teacher"],)
        submitted = st.form_submit_button("התחבר")
        if submitted:
            if not teacher_name or not lesson_code or not password:
                st.error("נא למלא את כל השדות")
            else:
                st.success("התחברת בהצלחה")