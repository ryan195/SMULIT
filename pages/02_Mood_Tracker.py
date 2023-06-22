import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu
import pandas as pd
import matplotlib.pyplot as plt
from nltk.sentiment import SentimentIntensityAnalyzer



legalease = Image.open("assets/LegalEase.jpg")

st.set_page_config(page_title="LegalEase - Mood Tracker", page_icon = "👨🏻‍⚖️", layout = "centered", initial_sidebar_state = "auto")
#st.sidebar.title("LegalEase")
st.sidebar.image(legalease)

st.header("LegalEase")
st.subheader("Mood Tracker with Journal")
st.write("*Track your daily mood, journal entries, and visualize mood trends over time!*")

# Create a DataFrame to store mood and journal data
data = pd.DataFrame(columns=["Date", "Mood", "Journal"])

# Input form to track mood and journal entry
date = st.date_input("Date")
mood = st.slider("Mood (1-10)", 1, 10)
journal = st.text_area("Journal Entry")

# Add mood and journal data to DataFrame
if st.button("Add Entry"):
    data = data.append({"Date": date, "Mood": mood, "Journal": journal}, ignore_index=True)
    st.success("Entry added successfully!")

# Display mood and journal data table
st.subheader("Mood and Journal Entries")
st.dataframe(data)

# Perform sentiment analysis on journal entries
if not data.empty:
    sid = SentimentIntensityAnalyzer()
    data["Sentiment Score"] = data["Journal"].apply(lambda x: sid.polarity_scores(x)["compound"])
    st.subheader("Sentiment Analysis of Journal Entries")
    st.dataframe(data[["Date", "Journal", "Sentiment Score"]])

# Display mood trends over time
st.subheader("Mood Trends Over Time")
if not data.empty:
    data["Date"] = pd.to_datetime(data["Date"])
    data.set_index("Date", inplace=True)
    data.sort_index(inplace=True)
    plt.figure(figsize=(10, 6))
    plt.plot(data.index, data["Mood"])
    plt.xlabel("Date")
    plt.ylabel("Mood")
    plt.title("Mood Trends")
    st.pyplot(plt)
else:
    st.info("Add mood data to visualize trends.")