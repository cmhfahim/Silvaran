import streamlit as stl
from streamlit_lottie import st_lottie
import json
import requests

@stl.experimental_fragment
def CGPA():
    stl.markdown("<h2 style='text-align: center; color: #E7D2CC;'>CGPA Calculator</h2>", unsafe_allow_html=True)
    def url(url):
        req=requests.get(url)
        if req.status_code !=200:
            return None
        return req.json()
    ur=url("https://lottie.host/5f974a65-8317-49a8-9e68-521fa4c74013/6TsVSqaYmE.json")
    st_lottie(ur,height=300,key="Education")
    credits = stl.text_input("Enter your course credits for this trimester, separated by commas")
    cgpas = stl.text_input("Enter your CGPAs for this trimester, separated by commas")
    def calcg(credits, cgpas):
        lst = [credit * cgpa for credit, cgpa in zip(credits, cgpas)]
        r = sum(lst) / sum(credits)
        return round(r, 3)
    if stl.button("Enter to Calculate CGPA"):
        credits = list(map(float, credits.split(',')))
        cgpas = list(map(float, cgpas.split(',')))
        res = calcg(credits, cgpas)
        stl.write("Your CGPA in this Trimester", res)
        stl.markdown("<h3 style='text-align: center; color: White;'>This is to solve some common problem of UIU students</h3>", unsafe_allow_html=True)
 
