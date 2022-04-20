import streamlit as st

st.write(st.experimental_get_query_params())

yt = st.experimental_get_query_params()['yt'][0]

if 'youtu.be' in yt:
  ytid = yt.split('/')[-1]
  st.write(ytid)
if 'youtube.com' in yt:
  ytid = yt.split('=')[-1]
  st.write(ytid)
  
st.write(f'http://img.youtube.com/vi/{ytid}/0.jpg')
