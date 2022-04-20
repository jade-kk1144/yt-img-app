import streamlit as st

st.write(st.experimental_get_query_params())

yt = st.experimental_get_query_params()['yt'][0].split('=')

#f'http://img.youtube.com/vi/{yt}/0.jpg'
