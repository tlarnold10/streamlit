# key = pJVub2Gx79wf5i3AqXYy
import requests
import pdb
import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plot

url = 'https://www.quandl.com/api/v3/datatables/NDAQ/DCS.json?api_key=pJVub2Gx79wf5i3AqXYy'
response = requests.get(url)

json_data = response.json()

# Get datat into arrays
years_array = []
region_array = []
month_array = []
sold_array = []
data_set = json_data['datatable']['data']
for data in data_set:
    region_array.append(data[0])
    years_array.append(data[1])
    month_array.append(data[2])
    sold_array.append(data[3])

# First need to create my dictionary
data_dict = {}
data_dict['year'] = years_array
data_dict['region'] = region_array
data_dict['month'] = month_array
data_dict['sold'] = sold_array
weed_df = pd.DataFrame(data_dict)


bar_df = pd.DataFrame(weed_df[['sold', 'region']])

st.write(bar_df.plot.bar())

st.title("Streamlit app about Weed")
option = st.sidebar.multiselect(
    "Select a region",
    np.unique(weed_df['region'])
)
'You selected:', option

st.dataframe(weed_df[weed_df['region'].isin(option)])