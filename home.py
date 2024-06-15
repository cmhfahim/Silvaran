import streamlit as stl
import requests
from streamlit_lottie import st_lottie
import json

@stl.experimental_fragment
def home():
    def url(url):
        req=requests.get(url)
        if req.status_code !=200:
            return None
        return req.json()
    ur=url("https://lottie.host/607ecaf0-fac1-4de8-af38-4f57ca4fef7c/A818GRE2Xt.json")
    st_lottie(ur,height=300,key="Education")
    stl.markdown("<h3 style='text-align: center; color: #E7D2CC;'>This is to solve some common problem of UIU students</h3>", unsafe_allow_html=True)
