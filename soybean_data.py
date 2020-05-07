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

st.write(weed_df)
st.write(weed_df.groupby(['month']).sum())

# weed_df['year_month'] = str(weed_df['year']) + weed_df['month']
# weed_df['year_month'] = weed_df.apply(lambda row: str(row['year']) + row['month'], axis=1)

year_month = []
for index, row in weed_df.iterrows():
    # pdb.set_trace()
    if row.month == 'jan': 
        year_month.append(str(row.year) + '01')
    elif row.month == 'feb': 
        year_month.append(str(row.year) + '02')
    elif row.month == 'mar': 
        year_month.append(str(row.year) + '03')
    elif row.month == 'apr': 
        year_month.append(str(row.year) + '04')
    elif row.month == 'may': 
        year_month.append(str(row.year) + '05')
    elif row.month == 'june': 
        year_month.append(str(row.year) + '06')
    elif row.month == 'jul': 
        year_month.append(str(row.year) + '07')
    elif row.month == 'aug': 
        year_month.append(str(row.year) + '08')
    elif row.month == 'sep': 
        year_month.append(str(row.year) + '09')
    elif row.month == 'oct': 
        year_month.append(str(row.year) + '10')
    elif row.month == 'nov': 
        year_month.append(str(row.year) + '11')
    elif row.month == 'dec': 
        year_month.append(str(row.year) + '12')
    else:
        print(row.month)
weed_df['year_month'] = year_month

bar_df = pd.DataFrame(weed_df[['region','sold']])

# bar_df.plot.bar()
# plot.show()
st.bar_chart(bar_df)
st.write(bar_df)

st.title("Streamlit app about Weed")
option = st.sidebar.multiselect(
    "Select a region",
    np.unique(weed_df['region'])
)
'You selected:', option

st.dataframe(weed_df[weed_df['region'].isin(option)])