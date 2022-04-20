import streamlit as st

def update_params():
    st.experimental_set_query_params(challenge=st.session_state.day)

days_list = [f'Day {x}' for x in [1,2,3,4,5]]

query_params = st.experimental_get_query_params()

if query_params and query_params["challenge"][0] in days_list:
    st.session_state.day = query_params["challenge"][0]

selected_day = st.selectbox('Start the Challenge 👇', days_list, key="day", on_change=update_params)
for i in days_list:
    if selected_day == i:
        st.markdown(f'# 🗓️ {i}')

st.write('st.session_state.day: ', st.session_state.day)
