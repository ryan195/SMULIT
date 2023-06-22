import streamlit as st
from PIL import Image


legalease = Image.open("assets/LegalEase.jpg")

st.set_page_config(page_title="LegalEase - Home", page_icon = "👨🏻‍⚖️", layout = "centered", initial_sidebar_state = "auto")
#st.sidebar.title("LegalEase")
st.sidebar.image(legalease)

st.header("LegalEase")
st.subheader("Home")
st.write("*Empowering lawyers in hybrid work environments with mental health support & optimal task scheduling*")

st.write("*Copyright © 2023 TPJC - Harry, Brendan, Yong Jun, Ryan*") 