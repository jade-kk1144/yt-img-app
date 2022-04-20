import streamlit as st

st.title('st.experimental_get_query_params')

# Image settings
st.sidebar.header('Settings')
img_dict = {'Max': 'maxresdefault', 'High': 'hqdefault', 'Medium': 'mqdefault', 'Standard': 'sddefault'}
selected_img_quality = st.sidebar.selectbox('Select image quality', ['Max', 'High', 'Medium', 'Standard'])
img_quality = img_dict[selected_img_quality]

yt_url = st.text_input('Paste YouTube URL', 'https://youtu.be/DctmeFx8s_k')

# Retrieving YouTube video ID from URL
#yt = st.experimental_get_query_params()['yt'][0]

def get_ytid(input_url):
  if 'youtu.be' in input_url:
    ytid = input_url.split('/')[-1]
    #st.write('YouTube video ID: ', ytid)
  if 'youtube.com' in input_url:
    ytid = input_url.split('=')[-1]
    #st.write('YouTube video ID: ', ytid)
  return ytid
    
# Display YouTube thumbnail image
if yt_url != '':
  ytid = get_ytid(yt_url) # yt or yt_url

  yt_img = f'http://img.youtube.com/vi/{ytid}/{img_quality}.jpg'
  st.image(yt_img)
  st.write('YouTube video thumbnail image URL: ', yt_img)
else:
  st.write('Enter URL to continue ...')
