import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu
import pandas as pd
import matplotlib.pyplot as plt


legalease = Image.open("assets/LegalEase.jpg")

st.set_page_config(page_title="LegalEase - Mood Tracker", page_icon = "👨🏻‍⚖️", layout = "centered", initial_sidebar_state = "auto")
#st.sidebar.title("LegalEase")
st.sidebar.image(legalease)

st.header("LegalEase")
st.subheader("Mood Tracker")
st.write("*Track your daily mood and visualize your mood trends over time.*")

# Create a DataFrame to store mood data
mood_data = pd.DataFrame(columns=["Date", "Mood"])

# Input form to track mood
date = st.date_input("Date")
mood = st.slider("Mood (1-10)", 1, 10)

# Add mood data to DataFrame
if st.button("Add Mood"):
    mood_data = mood_data.append({"Date": date, "Mood": mood}, ignore_index=True)
    st.success("Mood added successfully!")

# Display mood data table
st.subheader("Mood Data")
st.dataframe(mood_data)

# Display mood trends over time
st.subheader("Mood Trends Over Time")
if not mood_data.empty:
    mood_data["Date"] = pd.to_datetime(mood_data["Date"])
    mood_data.set_index("Date", inplace=True)
    mood_data.sort_index(inplace=True)
    plt.figure(figsize=(10, 6))
    plt.plot(mood_data.index, mood_data["Mood"])
    plt.xlabel("Date")
    plt.ylabel("Mood")
    plt.title("Mood Trends")
    st.pyplot(plt)
else:
    st.info("Add mood data to visualize trends.")