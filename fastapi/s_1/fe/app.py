import streamlit  as st 
import requests
t1,t2=st.tabs(["Login","Register"])

with t2:
    with st.form("R form"):
        n=st.text_input("Name",placeholder="Enter name here")
        e=st.text_input("Email",placeholder="Enter Email here")
        a=st.number_input("Age",min_value=18)
        ph=st.text_input("PhNumber",placeholder="Enter ph number here")
        p=st.text_input("Password",placeholder="Enter Password here",type="password")
        c_p=st.text_input("Confirm_Password",placeholder="Enter Password Again here",type="password")
        sks=st.text_input("Skills",placeholder="ex -- python, react, sql")
        btn_r=st.form_submit_button("Register")
        if btn_r:
            new_stud={
                "name":n,
                "email":e,
                "age":a ,
                "ph_number":ph,
                "password":p,
                "c_password":c_p,
                "skills":sks
            }

            res=requests.post("http://127.0.0.1:8000/register",json=new_stud)

            if res.status_code ==200:
                st.write(res.json())
            elif res.status_code == 422:
                st.write(res.json())


