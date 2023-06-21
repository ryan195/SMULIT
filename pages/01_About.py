import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu

st.set_page_config(page_title="LegalEase - About Us", page_icon = "👨🏻‍⚖️", layout = "centered", initial_sidebar_state = "auto")
st.sidebar.title("LegalEase")
#st.sidebar.image("assets/pp_logo2.jpg", use_column_width=True)

# Use the following line to include your style.css file
#st.markdown('<style>' + open('style.css').read() + '</style>', unsafe_allow_html=True)

st.subheader("About Us!")

harry = Image.open("assets/harry.jpg")
brendan = Image.open("assets/brendan.jpg")
#vanessa = Image.open("assets/vanessa.jpg")
ryan = Image.open("assets/ryan.jpg")

selected_options = ["Overview", "Summary", "Our Team", "References"]
selected = st.selectbox("Which section would you like to read?", options = selected_options)
st.write("Current selection:", selected)
if selected == "Overview":
    st.subheader("Overview")
    st.markdown("""
    **Overall Theme: Bridging the Tech-Law Divide**

    **Chosen Theme and Statement: Hybrid Working - Mental Health**

    Problem Statement: Fully remote work arrangements during the pandemic has led to many lawyers feeling burnt out. This was in part due to the lack of social interaction and the subsequent feelings of isolation, alongside the blurring of lines between rest and work. How might we then utilise technology to mitigate such risks and help lawyers with their mental health when it comes to hybrid working arrangements?

    """)

elif selected == "Summary":
    st.subheader("Summary")
    st.markdown("""
    For SMU-LIT Hackathon 2023, we have chosen the theme of Hybrid Working, which requires us to ideate an application to support the mental health of lawyers working in hybrid arrangements.

    To address this problem statement, we have come up with *LegalEase*, *TBD*.
    
    **Inspiration**

    TBD

    **What it does**

    TBD

    **How we built it**

    We used Streamlit, HTML and CSS as our front-end for our web application, and utilised the OpenAI API as well as Firebase for our back-end.

    **What makes our solution stand out**

    TBD

    **Some key challenges we faced**

    A key issue that we've faced is the transition from our typical skillset of HTML/CSS/Javascript to Streamlit, as we wanted to fully utilise the OpenAI API for easier facilitation of the back-end. In addition, we were also new to utilising Firebase to store user data for our login system, to track user history of previous queries using our app.

    **Built with**

    `Firebase` `Python` `Streamlit` `HTML` `CSS` `OpenAI API`

    Github repo: TBD

    """)

elif selected == "Our Team":
    st.subheader("Our Team")
    with st.container():
        image_column, text_column = st.columns((1.5,5))
        with image_column:
            st.image(harry)
        with text_column:
            st.subheader("Harry Chang")
            st.write("*Data Science and Analytics*")
            st.markdown("""
            Role: Front-end, Branding Assets, Copywriting

            `Python` `HTML` `CSS` `Streamlit` `R` `Java` `Figma`
            """)
    with st.container():
        image_column, text_column = st.columns((1.5,5))
        with image_column:
            st.image(brendan)
        with text_column:
            st.subheader("Brendan Cheong")
            st.write("*Business Analytics and Economics*")
            st.markdown("""
            Role: Front-end, Back-end

            `Python` `HTML` `CSS` `Streamlit` `Javascript` `React`
            """)
    with st.container():
        image_column, text_column = st.columns((1.5,5))
        with image_column:
            #st.image(vanessa)
            st.empty()
        with text_column:
            st.subheader("Tay Yong Jun")
            st.write("*Law*")
            st.markdown("""
            Role: Legal Advisor

            """)
    with st.container():
        image_column, text_column = st.columns((1.5,5))
        with image_column:
            st.image(ryan)
        with text_column:
            st.subheader("Ryan Tan")
            st.write("*Business Analytics*")
            st.markdown("""
            Role: Back-end

            `CPP` `Java` `Python` `HTML` `CSS` `Javascript` `Streamlit` `Firebase`
            """)

elif selected == "References":
    st.subheader("References")
    st.markdown("""
            - Streamlit API Documentation: https://docs.streamlit.io/ 

            - OpenAI API Documentation: https://openai.com/blog/openai-api 
            """)

st.write("*Copyright © 2023 TPJC - Harry, Brendan, Yong Jun, Ryan*") 

