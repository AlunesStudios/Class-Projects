import streamlit as st
Length = st.number_input("Enter the length of your rectangle.", min_value=0.00)
Breadth = st.number_input("Enter the breadth of your rectangle.", min_value=0.00)
if st.button("Check shape."):
    if Length == Breadth:
        st.write("**The shape is a square.**")
    elif Length == 0 and Breadth == 0:
        st.write("**The shape is invalid.**")
    else:
        st.write("**The shape is a rectangle.**")


st.header("", divider="grey")

user_name = "Al_UK"
password = "1234543211"

User = st.text_input("Enter your user name.")
Password = st.text_input("Enter your password")
if st.button("Login"):
   if User == "Al_UK" and Password == "1234543211":
      st.success("Login Successful!")
   else:
      st.error("Wrong Credentials!")


st.header("", divider="grey")

Num_1 = st.text_input("Enter Number 1")
Num_2 = st.text_input("Enter Number 2")

if st.button("Next"):
    if Num_1 > Num_2:
        st.write(f"**{Num_1} is greater than {Num_2}**")
    elif Num_1 < Num_2:
        st.write(f"**{Num_2} is greater than {Num_1}**")
    else:
        st.write(f"**Both Numbers are the same**")
