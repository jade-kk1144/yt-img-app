import streamlit as st

st.write(st.experimental_get_query_params())

st.sidebar.header('Settings')
img_dict = {'Max': 'maxresdefault', 'High': 'hqdefault', 'Medium': 'mqdefault', 'Standard': 'sddefault'}
selected_img_quality = st.sidebar.selectbox('Select image quality', ['Max', 'High', 'Medium', 'Standard'])
img_quality = img_dict[selected_img_quality]


yt = st.experimental_get_query_params()['yt'][0]

if 'youtu.be' in yt:
  ytid = yt.split('/')[-1]
  st.write(ytid)
if 'youtube.com' in yt:
  ytid = yt.split('=')[-1]
  st.write(ytid)

yt_img = f'http://img.youtube.com/vi/{ytid}/{img_quality}.jpg'

st.image(yt_img)
st.write(yt_img)
