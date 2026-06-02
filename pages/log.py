import streamlit as st

import pymongo
import random
import time

conn = pymongo.MongoClient('''mongodb+srv://princebarnwal030_db_user:W0v9Y5WmE6BJo68F@cluster0.nw4zkbv.mongodb.net/?appName=Cluster0''')

mydb = conn["ojt2"]

my = mydb["student"]
p = st.progress(0)

for i in range(100):
       p.progress(i+1,"Loading")
       time.sleep(0.02)
       p.empty()      

t1,t2=st.tabs(["signin", "signup"])
with t1:
       with st.form(key="login_form"):
              username=st.text_input("Userlogin 👨‍💼")
              password=st.text_input("🔑 Password ",type="password" )
              confirm=st.text_input("Confirm Password ", type = "password")              

              st.checkbox("Agree Terms")
              if st.form_submit_button("Sign In"):
                     my.insert_one({"userlogin ":username, "password":password})
                     
                     st.switch_page("pages/contact.py")
              if password == confirm:
                     st.success("Thanking for Signup")
                     st.snow()
              else:
                  st.error("Your password is incorrect")

with t2:
       with st.form("SignIn"):
              t1=st.text_input("👤Username")
              t2=st.text_input("🔒Password",type="password")
              
              t3=st.date_input("Date of Birth")
              t4=st.text_input("Mobile Number") 
              t5=st.radio("Gender",["Female","Male"])
                      
              if st.form_submit_button("SignIn"):
                  my.insert_one({"username":t1,"password":t2,"dob":str(t3),"mobile number":t4,"Gender":t5"})
              if not t1 or not t2 or not t3 or not t4 or not t5 :
                  st.error("Fill The Fields!!!")
              else:
                  st.success("Done...")


    


    
