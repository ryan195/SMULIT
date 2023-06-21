import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu

st.set_page_config(page_title="LegalEase - Resources", page_icon = "👨🏻‍⚖️", layout = "centered", initial_sidebar_state = "auto")
st.sidebar.title("LegalEase")

st.subheader("Resources")

st.write("*Feeling burnt out and need help? Here are some mental health resources to get you started!*")

st.write("*Sort the below into cards + images*")

st.markdown("""

Law Society of Singapore: The Law Society offers various support services for lawyers, including a Lawyers' Assistance Programme (LAP) which provides confidential counseling and support. They also have a Wellness Programme that focuses on promoting mental well-being within the legal profession. https://www.lawsociety.org.sg/the-law-society/support-schemes/ 

Samaritans of Singapore (SOS): SOS is a non-profit organization that provides emotional support and crisis intervention services. They have a 24-hour helpline (1800-221-4444) that offers a listening ear and guidance to individuals who are in distress.

Singapore Association of Mental Health (SAMH): SAMH provides a range of mental health services, including counseling and support groups. They offer individual counseling services, as well as group therapy programs that can help lawyers connect with others who may be facing similar challenges.

National Addictions Management Service (NAMS): NAMS is a specialized service under the Institute of Mental Health (IMH) that focuses on the management and treatment of addictions. If a lawyer is struggling with substance abuse or addiction-related issues, NAMS can provide assessment, counseling, and treatment options.

Employee Assistance Program (EAP): Some law firms in Singapore offer Employee Assistance Programs that provide confidential counseling and support services for their employees. Lawyers can inquire within their organizations to see if such a program exists.


""")