import streamlit as st

st.title('st.experimental_get_query_params')

st.header('Query text from URL')
st.write(st.experimental_get_query_params())

# Image settings
st.sidebar.header('Settings')
img_dict = {'Max': 'maxresdefault', 'High': 'hqdefault', 'Medium': 'mqdefault', 'Standard': 'sddefault'}
selected_img_quality = st.sidebar.selectbox('Select image quality', ['Max', 'High', 'Medium', 'Standard'])
img_quality = img_dict[selected_img_quality]

st.header('Applying query text from URL')
# Retrieving YouTube video ID from URL
yt = st.experimental_get_query_params()['yt'][0]


if yt is not None:
  if 'youtu.be' in yt:
    ytid = yt.split('/')[-1]
    st.write('YouTube video ID: ', ytid)
  if 'youtube.com' in yt:
    ytid = yt.split('=')[-1]
    st.write('YouTube video ID: ', ytid)

  # Display YouTube thumbnail image
  yt_img = f'http://img.youtube.com/vi/{ytid}/{img_quality}.jpg'

  st.image(yt_img)
  st.write(yt_img)
else:
  st.write('Awaiting')
