import streamlit as st

st.write(st.experimental_get_query_params())

yt = st.experimental_get_query_params()['yt'][0]

if 'youtu.be' in yt:
  a = yt.split('/')[-1]
  st.write(a)

#f'http://img.youtube.com/vi/{yt}/0.jpg'
