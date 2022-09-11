import streamlit as st
from PIL import Image

st.title('Streamlit初号機')
st.caption('これはStreamlitのWebアプリ第一号です')

image=Image.open('./data/absolutvision-82TpEld0_e4-unsplash.jpg')
st.image(image,width=350)