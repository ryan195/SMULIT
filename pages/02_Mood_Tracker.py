import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu

legalease = Image.open("assets/LegalEase.jpg")

st.set_page_config(page_title="LegalEase - Mood Tracker", page_icon = "👨🏻‍⚖️", layout = "centered", initial_sidebar_state = "auto")
#st.sidebar.title("LegalEase")
st.sidebar.image(legalease)

st.header("LegalEase")
st.subheader("Mood Tracker")