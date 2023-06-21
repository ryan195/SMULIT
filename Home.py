import streamlit as st
import pyrebase
import requests

st.set_page_config(page_title="LegalEase - Home", page_icon = "👨🏻‍⚖️", layout = "centered", initial_sidebar_state = "auto")

firebaseConfig = {
  "apiKey": "AIzaSyASBQQV0tcGclITfO20afhXkvyNw37PE1M",
  "authDomain": "smulit-e8993.firebaseapp.com",
  "projectId": "smulit-e8993",
  "storageBucket": "smulit-e8993.appspot.com",
  "messagingSenderId": "681105847463",
  "appId": "1:681105847463:web:03f6b7989a8dcb56b29782",
  "databaseURL" : "https://smulit-e8993-default-rtdb.asia-southeast1.firebasedatabase.app/"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()


# Authentication
authenticate = st.sidebar.selectbox('Login/Signup', ['Login', 'Signup'])

if authenticate == 'Signup':
    email = st.sidebar.text_input('Enter your email address')
    password = st.sidebar.text_input('Enter your password', type = 'password')
    name = st.sidebar.text_input('Enter your Name')
    submit = st.sidebar.button('Log In')


    if submit :
        user = auth.create_user_with_email_and_password(email, password)
        st.success('Your account has successfully been created!')
       
        #Signing the user and create a user variable
        user = auth.sign_in_with_email_and_password(email, password)
        db.child(user['localId']).child("Handle").set(name)
        db.child(user['localId']).child("ID").set(user['localId'])
        st.title("Hi, " + name)
        st.info('Login successful')




if authenticate == 'Login' :
    email = st.sidebar.text_input('Enter your email address')
    password = st.sidebar.text_input('Enter your password', type = 'password')
    submit = st.sidebar.button('Log In')
    if submit :
        try: 
            user = auth.sign_in_with_email_and_password(email, password)
            username = db.child(user['localId']).child("Handle").get()
            st.session_state.name = username
            st.session_state.user = user
            if user is not None :
                st.session_state.authenticated = True
            st.success("Successfully signed in")
        except Exception as e : 
                st.info(e)
        else :    
            st.write("Welcome")