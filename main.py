import streamlit as stl
from home import home
from CG import CGPA
from payment import payment
from feedback import feedback

stl.markdown("<h1 style='text-align: center; color: Black;'>SILVARAN</h1>", unsafe_allow_html=True)

if "page" not in stl.session_state:
    stl.session_state.page = "Homepage"  


stl.sidebar.title("Navigation")

if stl.sidebar.button("Homepage"):
    stl.session_state.page = "Homepage"
if stl.sidebar.button("Payment Roadmap"):
    stl.session_state.page = "Payment"
if stl.sidebar.button("CGPA Calculator"):
    stl.session_state.page = "CGPA"
if stl.sidebar.button("Feedback"):
    stl.session_state.page = "Feedback"

# Show the selected page
if stl.session_state.page == "Homepage":
    home()
elif stl.session_state.page == "Payment":
    payment()
elif stl.session_state.page == "CGPA":
    CGPA()
elif stl.session_state.page == "Feedback":
    feedback()
