import streamlit as st
import random

st.title("🎴 Andar Bahar Prediction Tool")
st.write("Upload your game screenshot here to predict the next likely result.")

uploaded_file = st.file_uploader("Upload game screenshot", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Screenshot", use_column_width=True)
    
    # Abhi ke liye random prediction (logic hum baad me improve karenge)
    prediction = random.choice(["Andar", "Bahar"])
    st.success(f"🎯 Next likely result: **{prediction}**")