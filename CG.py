import streamlit as stl
from streamlit_lottie import st_lottie
import requests

@stl.experimental_fragment
def CGPA():
    stl.markdown("<h2 style='text-align: center; color: #E7D2CC;'>CGPA Calculator</h2>", unsafe_allow_html=True)

    def url(url):
        req = requests.get(url)
        if req.status_code != 200:
            return None
        return req.json()

    ur = url("https://lottie.host/5f974a65-8317-49a8-9e68-521fa4c74013/6TsVSqaYmE.json")
    st_lottie(ur, height=300, key="Education")

    # Ask user how many courses
    num_courses = stl.number_input("How many courses do you want to enter?", min_value=1, step=1)

    # Define fixed options
    credit_options = [1, 2, 3]
    cgpa_options = [4, 3.67, 3.33, 3, 2.67, 2.33, 2, 1.67, 1.33, 1, 0]  # reversed

    credits = []
    cgpas = []

    # Create selectboxes for each course
    for i in range(int(num_courses)):
        col1, col2 = stl.columns(2)
        with col1:
            credit = stl.selectbox(f"Course {i+1} Credit", credit_options, key=f"credit_{i}")
        with col2:
            cgpa = stl.selectbox(f"Course {i+1} CGPA", cgpa_options, key=f"cgpa_{i}")
        credits.append(credit)
        cgpas.append(cgpa)

    def calcg(credits, cgpas):
        total_credits = sum(credits)
        if total_credits == 0:
            return 0
        weighted_sum = sum(c * g for c, g in zip(credits, cgpas))
        return round(weighted_sum / total_credits, 3)

    if stl.button("Calculate CGPA"):
        result = calcg(credits, cgpas)
        stl.markdown(f"<h3 style='text-align: center; color: white;'>Your CGPA this trimester: {result}</h3>", unsafe_allow_html=True)
        stl.markdown("<h4 style='text-align: center; color: #E7D2CC;'>This is to solve some common problem of UIU students</h4>", unsafe_allow_html=True)
