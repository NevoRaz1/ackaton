import uuid
import streamlit as st

if st.button("Create call link"):
    room = f"streamlit-{uuid.uuid4().hex[:12]}"   # random hard to guess room name
    st.session_state.meet_url = f"https://meet.jit.si/{room}"

if st.session_state.get("meet_url"):
    st.link_button("join the call", st.session_state.meet_url)