import streamlit as stl
from streamlit_lottie import st_lottie
import json
import requests

@stl.experimental_fragment
def payment():
    stl.markdown("<h2 style='text-align: center; color: #E7D2CC;'>Payment Roadmap</h2>", unsafe_allow_html=True)

    def url(url):
        req = requests.get(url)
        if req.status_code != 200:
            return None
        return req.json()

    ur = url("https://lottie.host/e817d581-61a3-4c3f-bcaf-5f5d1a1c0f7e/cET0KKA2E0.json")
    st_lottie(ur, height=300, key="Payment")

    def fee(credit_1,credit_2,waiver):
        remain_amount = 0
        tution_fee_1 = (5525 * credit_1)
        tution_fee_2 = (5525 * credit_2)

        if waiver == "0% Waiver or Scholarship":
            remain_amount = 100
        elif waiver == "25% Waiver or Scholarship":
            remain_amount = 75
        elif waiver == "50% Waiver or Scholarship":
            remain_amount = 50
        elif waiver == "100% Waiver or Scholarship":
            remain_amount = 0

        discount_total_fee_1 = ((tution_fee * (remain_amount / 100))) + 6500
        discount_total_fee_1=discount_total_fee_1+tution_fee_2
        if waiver == "100% Waiver or Scholarship":
            return discount_total_fee_1
        else:
            installment_1 = discount_total_fee_1 * (40 / 100)
            reamin_fee = discount_total_fee_1 - installment_1
            installment_2 = reamin_fee / 2
            installment_3 = installment_2
            lst = [discount_total_fee_1, installment_1, installment_2, installment_3]
            return lst

    credit_1 = stl.number_input("Enter Your Total Credits (Non-Retake): ")
    credit_2 = stl.number_input("Enter Your Total Credits (Retake): ")
    credit_2=credit_2/2

    waiver = stl.selectbox('Please Provide Necessary Information', [
        '0% Waiver or Scholarship', '25% Waiver or Scholarship',
        '50% Waiver or Scholarship', '100% Waiver or Scholarship'
    ])

    see = stl.selectbox('Enter your Choice', [
        'See Payment Roadmap', '1st Installment', '2nd Installment', '3rd Installment'
    ])

    # Style for only this button
    custom_button = """
    <div id="custom-button-wrapper">
        <style>
            #custom-button-wrapper button {
                background-color: black !important;
                color: white !important;
                border: none;
                border-radius: 8px;
                padding: 0.75em 2em;
                font-size: 1em;
                transition: 0.3s;
            }
            #custom-button-wrapper button:hover {
                background-color: #333333 !important;
                transform: scale(1.05);
            }
        </style>
    """
    stl.markdown(custom_button, unsafe_allow_html=True)

    if stl.button("See payments Roadmap", key="payment_button"):
        res = fee(credit_1,credit_2, waiver)
        if waiver == "100% Waiver or Scholarship":
            if see == "See Payment Roadmap":
                stl.markdown(f"""
                <div style="background: transparent; color: white; padding: 1rem; font-size: 18px;">
                    <p><strong>You Have to Pay Total:</strong> {res}</p>
                    <p>Remain balance will be adjusted</p>
                </div>
                """, unsafe_allow_html=True)
            else:
                stl.markdown(f"""
                <div style="background: transparent; color: white; padding: 1rem; font-size: 18px;">
                    <p>You don't need to pay in this installment</p>
                </div>
                """, unsafe_allow_html=True)
        else:
            if see == "See Payment Roadmap":
                stl.markdown(f"""
                <div style="background: transparent; color: white; padding: 1rem; font-size: 18px;">
                    <p><strong>Total Payment:</strong> {res[0]}</p>
                    <p><strong>1st Installment (Due Aug 13, 2025):</strong> {res[1]}</p>
                    <p><strong>2nd Installment (Due Sep 14, 2025):</strong> {res[2]}</p>
                    <p><strong>3rd Installment (Due Oct 12, 2025):</strong> {res[3]}</p>
                </div>
                """, unsafe_allow_html=True)
            elif see == "1st Installment":
                stl.markdown(f"""
                <div style="background: transparent; color: white; padding: 1rem; font-size: 18px;">
                    <p><strong>1st Installment (Due Aug 13, 2025):</strong> {res[1]}</p>
                </div>
                """, unsafe_allow_html=True)
            elif see == "2nd Installment":
                stl.markdown(f"""
                <div style="background: transparent; color: white; padding: 1rem; font-size: 18px;">
                    <p><strong>2nd Installment (Due Sep 14, 2025):</strong> {res[2]}</p>
                </div>
                """, unsafe_allow_html=True)
            elif see == "3rd Installment":
                stl.markdown(f"""
                <div style="background: transparent; color: white; padding: 1rem; font-size: 18px;">
                    <p><strong>3rd Installment (Due Oct 12, 2025):</strong> {res[3]}</p>
                </div>
                """, unsafe_allow_html=True)
