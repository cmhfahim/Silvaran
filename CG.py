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

    # Ask user how many courses this trimester
    num_courses = stl.number_input("How many courses do you want to enter?", min_value=1, step=1)

    # Ask user for previous academic record
    num_prev_credit = stl.number_input("How many credits have you completed before this trimester?", min_value=0.0)
    pre_cgpa = stl.number_input("What is your previous CGPA?", min_value=0.0, max_value=4.0)

    # Define options
    credit_options = [1, 2, 3]
    cgpa_options = [4, 3.67, 3.33, 3, 2.67, 2.33, 2, 1.67, 1.33, 1, 0]  # reversed

    credits = []
    cgpas = []

    for i in range(int(num_courses)):
        col1, col2 = stl.columns(2)
        with col1:
            credit = stl.selectbox(f"Course {i+1} Credit", credit_options, key=f"credit_{i}")
        with col2:
            cgpa = stl.selectbox(f"Course {i+1} CGPA", cgpa_options, key=f"cgpa_{i}")
        credits.append(credit)
        cgpas.append(cgpa)

    def calc_trimester_cgpa(credits, cgpas):
        total_credits = sum(credits)
        weighted_sum = sum(c * g for c, g in zip(credits, cgpas))
        return total_credits, weighted_sum

    if stl.button("Calculate CGPA"):
        total_credits, weighted_sum = calc_trimester_cgpa(credits, cgpas)

        # Calculate trimester CGPA
        if total_credits == 0:
            trimester_cgpa = 0
        else:
            trimester_cgpa = round(weighted_sum / total_credits, 3)

        # Calculate overall CGPA
        prev_sum = num_prev_credit * pre_cgpa
        new_sum = prev_sum + weighted_sum
        new_total_credit = num_prev_credit + total_credits
        if new_total_credit == 0:
            overall_cgpa = 0
        else:
            overall_cgpa = round(new_sum / new_total_credit, 3)

        # Display results
        stl.markdown(f"<h3 style='text-align: center; color: white;'>Your Trimester GPA: {trimester_cgpa}</h3>", unsafe_allow_html=True)
        stl.markdown(f"<h3 style='text-align: center; color: #00FFAA;'>Your Overall CGPA: {overall_cgpa}</h3>", unsafe_allow_html=True)
        stl.markdown("<h4 style='text-align: center; color: #E7D2CC;'>This is to solve some common problem of UIU students</h4>", unsafe_allow_html=True)
