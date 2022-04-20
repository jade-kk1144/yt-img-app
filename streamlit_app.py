import streamlit as st

st.write(st.experimental_get_query_params())

yt = st.experimental_get_query_params()['yt'][0]

if 'youtu.be' in yt:
  ytid = yt.split('/')[-1]
  st.write(ytid)
if 'youtube.com' in yt:
  ytid = yt.split('=')[-1]
  st.write(ytid)
  
yt_img = f'http://img.youtube.com/vi/{ytid}/maxresdefault.jpg'

st.image(yt_img)
st.write(yt_img)
