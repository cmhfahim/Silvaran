import streamlit as stl
from home import home
from CG import CGPA
from payment import payment
from PIL import Image
import requests
from streamlit_lottie import st_lottie
from feedback import feedback

stl.markdown("<h1 style='text-align: center; color: Black;'>SILVARAN</h1>", unsafe_allow_html=True)

stl.sidebar.title("Navigation")
if stl.sidebar.button("Homepage"):
    home()
if stl.sidebar.button("Payment Roadmap"):
    payment()
if stl.sidebar.button("CGPA Calculator"):
    CGPA()
if stl.sidebar.button("Feedback"):
    feedback()
