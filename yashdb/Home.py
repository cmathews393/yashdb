import streamlit as st
import config
import httpx

st.header("Welcome to Yet Another Self Hosted Dashboard")

st.write("See below for your stats")

choose = 2  # Move choose outside of the loop
col1, col2 = st.columns(2)
for service in config.active_services:
    if choose % 2 == 0:
        with col1:
            with st.container(border=True):
                st.subheader(service)

                try:
                    httpx.get(getattr(config, f"{service}_api_url"))
                    st.write("Service is up!")
                except:
                    st.write("Service is down!")
    else:
        with col2:
            with st.container(border=True):
                st.subheader(service)
                try:
                    httpx.get(getattr(config, f"{service}_api_url"))
                    st.write("Service is up!")
                except:
                    st.write("Service is down!")

    choose += 1  # Increment choose within the loop
