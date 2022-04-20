import streamlit as st

st.write(st.experimental_get_query_params())

yt = st.experimental_get_query_params()['yt'][0]

if yt.startswith('https://youtu.be/'):
  str = yt.split('/')
  st.write(str)
else:
  str = yt.split('=')[0]
  st.write(str)

#f'http://img.youtube.com/vi/{yt}/0.jpg'
