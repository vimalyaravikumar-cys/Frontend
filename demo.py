import streamlit as st
st.title("Election-2026!!")
st.subheader("Voter details:")
name = st.text_input("Enter your name:")
age = st.number_input("Enter your Age:")
if st.button("Enter"):
    if age>= 18:
        st.text("Eligible to vote!")
    else:
        st.text(st.error("Not eligible to vote"))
st.divider()            
