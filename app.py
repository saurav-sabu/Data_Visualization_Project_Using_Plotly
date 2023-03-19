import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

df = pd.read_csv("geospatial_data.csv")

st.sidebar.title("Census Data")

list_of_states = list(df["State"].unique())
list_of_states.insert(0,"Overall States")

select_state = st.sidebar.selectbox("Select State",list_of_states)
primary_params = st.sidebar.selectbox("Select Primary Parameter",sorted(df.columns[5:]))
secondary_params = st.sidebar.selectbox("Select Secondary Parameter",sorted(df.columns[5:]))

plot = st.sidebar.button("Plot Graph")

if plot:
    st.text("Size represents primary parameter")
    st.text("Color represents secondary parameter")
    if select_state == "Overall States":
        fig = px.scatter_mapbox(df,"Latitude","Longitude",zoom=4,mapbox_style="carto-positron",size=primary_params,color=secondary_params,size_max=35,width=1200,height=700,hover_name="District")
        st.plotly_chart(fig,use_container_width=True)
    else:
        # plotting for particular state
        state_df = df[df["State"] == select_state]
        fig = px.scatter_mapbox(state_df,"Latitude","Longitude",zoom=3,mapbox_style="carto-positron",size=primary_params,color=secondary_params,size_max=35,width=1200,height=700,hover_name="District")
        st.plotly_chart(fig,use_container_width=True)

