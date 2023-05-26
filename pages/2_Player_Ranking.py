import streamlit as st
import pandas as pd
import numpy as np
import requests
import json


st.set_page_config(
    page_title='TT Vogue',
    page_icon='👋',
)

@st.cache_data
def get_players():
    return requests.get('https://ttvoguebackend-1-s6475544.deta.app/get-players').json()

players_raw = get_players()
players_df = pd.DataFrame(players_raw['data'])
players_df.rename(columns={'name': 'Name', 'point': 'Point'}, inplace=True)
hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """

# Inject CSS with Markdown
st.markdown(hide_table_row_index, unsafe_allow_html=True)
st.table(players_df.sort_values('Point', ascending=False))
