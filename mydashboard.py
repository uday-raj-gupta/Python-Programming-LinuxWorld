import matplotlib.pyplot  as plt
import streamlit as st
import pandas as pd
import time
st.title("Streamlit app of VGU")
st.text("Welcome to our Dashboard")
st.header("i am a Header")
st.write("You can Write", 10+5)
name = st.text_input("Enter Your Name : ")

age = st.number_input("Enter Your Age : ")
st.write("Your name is: ", name , "Your age is: ",age)
st.selectbox("Enter Your Course : ", ["BCA" , "BTECH", " MCA", "BBA"])
if st.button("Click ME"):
    st.success("clicked Button")
file = st.file_uploader("Upload Your File")
if file:
    content = file.read()
    print("File Uploaded Sucessfully...")

data = {"Name" :["TOM", "Jack","POP","Harry"] , "Marks" : [10,20,30,10]}
df =pd.DataFrame(data)
st.dataframe(df)

data = pd.DataFrame({
    "Marks" : [10,20,30,10]
})
st.line_chart(data)
st.bar_chart(data)

subject = ["Python", "C++", "JAVA"]
marks = [20,10,4]

fig , ax = plt.subplots()
ax.pie(marks, labels=subject, autopct='%1.1f%%')
st.pyplot(fig)
### GOLU 
st.sidebar.title("Navigation Menu")
st.sidebar.button("Home")
st.sidebar.button("Profile")
st.sidebar.button("Settings")

#piyush
df_csv = df.to_csv().encode('utf-8')
st.download_button("Download Data", df_csv, "data.csv")

#rahul
yt_link = "https://www.youtube.com/watch?v=PfImf8N5vVE&list=RDPfImf8N5vVE&start_radio=1"
st.video(yt_link)

#mee

with st.expander("What is Streamlit?"):
    st.write("Streamlit is a Python library for building web apps easily.")

