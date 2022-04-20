import streamlit as st

def update_params():
    st.experimental_set_query_params(q=st.session_state.q)

query_params = st.experimental_get_query_params()

st.write(query_params["q"][0])

selected_day = st.selectbox('Start the Challenge 👇', days_list, key="day", on_change=update_params)
for i in days_list:
    if selected_day == i:
        st.markdown(f'# 🗓️ {i}')

st.write('st.session_state.q: ', st.session_state.q)
