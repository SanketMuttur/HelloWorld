import streamlit as st
import time
import base64

def set_background(path):
    with open(path, "rb") as img:
        encoded = base64.b64encode(img.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}

        /* Make navbar/header transparent */
        header {{
            background: transparent !important;
        }}

        /* Make footer transparent */
        footer {{
            background: transparent !important;
        }}

        /* Make main content area transparent */
        .block-container {{
            background-color: rgba(255, 255, 255, 0.0);
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_background("bg.png")

text_display = st.empty()

string = list("Hello, World!")
newString = [" "]

for i in string:
    for j in [32] + list(range(65, 91)) + list(range(97, 123)) + [33, 44]:
        newString[-1] = chr(j)
        text_display.markdown(f'<center><h1>{''.join(newString)}</h1></center>', unsafe_allow_html=True)
        time.sleep(0.01)
        if chr(j) == i:
            newString.append(" ")
            break
