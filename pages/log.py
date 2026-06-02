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
                     st.success("Thanking forSignup")
                     st.snow()
              else:
                     st.error("Your password is incorrect")
           


with t2:
       with st.form("SignIn"):
              t1=st.text_input("👤Username")
              t2=st.text_input("🔒Password",type="password")
              t3=st.text_area("Address")
              t4=st.selectbox("Course",["B.sc IT","B.sc CA","B.sc CS"])
              t5=st.date_input("Dob")
              t6=st.text_input("Mobile Number")
              t7=st.file_uploader("Upload your picture")
              t8=st.radio("Gender",["F","M"])
              t9=st.slider("Age",16,28)
              st.write("Languages known")
              st.checkbox("Hindi")
              st.checkbox("English")
              st.checkbox("Nagpuri")
              t10=live_photo=st.camera_input("Upload Your Live Picture")
              count= random.randrange(1,100)
              str1="img"
              str1=str1+str(count)+".jpg"
              if t10 :
                     with open(str1,"wb") as f:
                            f.write(live_photo.getvalue())

         
              if st.form_submit_button("SignIn"):
                     my.insert_one({"username":t1,"password":t2,"address":t3,"course":t4,"dob":str(t5),"mobile number":t6,"Gender":t8,"age":t9,"phtot": str1})
              if not t1 or not t2 or not t3 or not t4 or not t5 or not t6 or not t7 or not t8 or not t9 or not  t10:
                        st.error("Fill The Fields!!!")
              else:
                     st.success("Done...")


    


    
