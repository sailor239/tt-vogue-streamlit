import streamlit as st
import pandas as pd
import numpy as np
import requests
import json
# from streamlit_modal import Modal
# import streamlit.components.v1 as components


st.set_page_config(
    page_title='TT Vogue',
    page_icon='👋',
)


@st.cache_data
def get_events():
    return requests.get('https://ttvoguebackend-1-s6475544.deta.app/get-events').json()

events_raw = get_events()

events_df = pd.DataFrame(events_raw['data'])
events_df['register'] = 'Register'

st.subheader('Recent Events:')
st.table(events_df[['event_name', 'event_address', 'event_date', 'event_start_time', 'register']])

def show_registration_form():
    with st.form(key='my_form'):
        event_name = st.text_input(label='Event Name')
        event_date = st.text_input(label='Event Date')
        event_time = st.text_input(label='Event Time')
        event_address = st.text_input(label='Event Address')
        submit_button = st.form_submit_button(label='Submit')
    if submit_button:
        payload = {
            'name': event_name,
            'date': event_date,
            'time': event_time,
            'address': event_address
        }
        print('Submitted!')
      # x = requests.post('http://127.0.0.1:8000/add-event', data=json.dumps(payload))

label_ok_button = st.button('Register', on_click=show_registration_form)
# label_cancel_button = st.button('Cancel')

# def close_form():
#     modal.close()


# modal = Modal("Register an Event", 1)
# open_modal = st.button("Open")
# if open_modal:
#     modal.open()

# if modal.is_open():
#     with modal.container():
#         with st.form(key='my_form'):
#             event_name = st.text_input(label='Event Name')
#             event_date = st.text_input(label='Event Date')
#             event_time = st.text_input(label='Event Time')
#             event_address = st.text_input(label='Event Address')
#             submit_button = st.form_submit_button(label='Submit', on_click=close_form)




