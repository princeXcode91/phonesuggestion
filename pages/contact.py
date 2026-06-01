import streamlit as st

import pymongo
import random
import time

conn = pymongo.MongoClient('''mongodb://127.0.0.1:27017/?directConnection
                           =true&serverSelectionTimeoutMS=2000&appName=mongosh
                           +2.8.3''')

mydb = conn["ojt2"]

my = mydb["student"]
p = st.progress(0)

for i in range(100):
       p.progress(i+1,"Loading")
       time.sleep(0.02)
       p.empty()
       
st.title("Welcome to the web world journey  using python")

st.write("Any doubt or questions Contact me .")
    
with st.form("contact_form"):
       name = st.text_input("Name")
       user_email = st.text_input("Email")
       message = st.text_area("Your Message")
       send_btn = st.form_submit_button("Send Message")
       if send_btn:
              if name and user_email and message:
                     st.success(f"Thank you, {name}! Your message has been sent successfully.")
              else:
                     st.error("Please fill in all the details before sending.")
