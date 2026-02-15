import streamlit as st
import re

st.set_page_config(page_title="Password Strength Checker", page_icon="🔐")

st.title("🔐 Password Strength Checker")
st.write("Check how strong your password is!")

password = st.text_input("Enter your password", type="password")

def check_strength(password):
    score = 0
    
    if len(password) >= 8:
        score += 1
    if re.search("[a-z]", password):
        score += 1
    if re.search("[A-Z]", password):
        score += 1
    if re.search("[0-9]", password):
        score += 1
    if re.search("[@#$%^&+=!]", password):
        score += 1
        
    return score

if password:
    score = check_strength(password)
    
    if score <= 2:
        st.error("Weak Password ❌")
    elif score == 3:
        st.warning("Moderate Password ⚠️")
    else:
        st.success("Strong Password ✅")
        
    st.write(f"Strength Score: {score}/5")
