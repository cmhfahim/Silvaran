import streamlit as stl
from streamlit_lottie import st_lottie
import json
import requests

@stl.experimental_fragment
def payment():
    stl.markdown("<h2 style='text-align: center; color: #E7D2CC;'>Payment Roadmap</h2>", unsafe_allow_html=True)

    # 🔹 Updated CSS styles: black button, transparent cards
    stl.markdown("""
        <style>
        .stButton>button {
            background-color: #01415c;
            color: white;
            padding: 0.75em 2em;
            font-size: 1em;
            border: none;
            border-radius: 8px;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background-color:#023d2c;
            transform: scale(1.05);
        }
        .card {
            background-color: transparent;
            padding: 1.2em;
            margin: 1em 0;
            border-radius: 12px;
            border-left: 5px solid #4CAF50;
        }
        .card h4 {
            color: #ffffff;
            margin-bottom: 0.5em;
        }
        .card p {
            color: #dddddd;
        }
        </style>
    """, unsafe_allow_html=True)

    def url(url):
        req = requests.get(url)
        if req.status_code != 200:
            return None
        return req.json()

    ur = url("https://lottie.host/e817d581-61a3-4c3f-bcaf-5f5d1a1c0f7e/cET0KKA2E0.json")
    st_lottie(ur, height=300, key="Payment")

    def fee(credit, waiver):
        tution_fee = 5525 * credit
        remain_amount = {
            "0% Waiver or Scholarship": 100,
            "25% Waiver or Scholarship": 75,
            "50% Waiver or Scholarship": 50,
            "100% Waiver or Scholarship": 0
        }.get(waiver, 100)

        discount_total_fee_1 = (tution_fee * (remain_amount / 100)) + 6500

        if waiver == "100% Waiver or Scholarship":
            return discount_total_fee_1
        else:
            installment_1 = discount_total_fee_1 * 0.40
            remain_fee = discount_total_fee_1 - installment_1
            installment_2 = remain_fee / 2
            installment_3 = installment_2
            return [discount_total_fee_1, installment_1, installment_2, installment_3]

    credit_1 = stl.number_input("Enter Your Total Credits (Non-Retake): ")
    credit_2 = stl.number_input("Enter Your Total Credits (Retake): ")
    credit = credit_1 + (credit_2 / 2)

    waiver = stl.selectbox('Please Provide Necessary Information', [
        '0% Waiver or Scholarship', '25% Waiver or Scholarship',
        '50% Waiver or Scholarship', '100% Waiver or Scholarship'
    ])

    see = stl.selectbox('Enter your Choice', [
        'See Payment Roadmap', '1st Installment', '2nd Installment', '3rd Installment'
    ])

    if stl.button("See payments Roadmap"):
        res = fee(credit, waiver)

        if waiver == "100% Waiver or Scholarship":
            if see == "See Payment Roadmap":
                stl.markdown(f"""
                    <div class="card">
                        <h4>You Have to Pay Total: {res:.2f} BDT</h4>
                        <p>Registration fee waived. Remaining balance will be adjusted.</p>
                    </div>
                """, unsafe_allow_html=True)
            else:
                stl.markdown(f"""
                    <div class="card">
                        <h4>No payment required for this installment ✅</h4>
                    </div>
                """, unsafe_allow_html=True)
        else:
            if see == "See Payment Roadmap":
                stl.markdown(f"""
                    <div class="card">
                        <h4>Total Payment (after waiver): {res[0]:.2f} BDT</h4>
                        <p><b>1st Installment</b> (Due: August 13, 2025): {res[1]:.2f} BDT</p>
                        <p><b>2nd Installment</b> (Due: September 14, 2025): {res[2]:.2f} BDT</p>
                        <p><b>3rd Installment</b> (Due: October 12, 2025): {res[3]:.2f} BDT</p>
                    </div>
                """, unsafe_allow_html=True)

            elif see == "1st Installment":
                stl.markdown(f"""
                    <div class="card">
                        <h4>1st Installment (Due: August 13, 2025):</h4>
                        <p>{res[1]:.2f} BDT</p>
                    </div>
                """, unsafe_allow_html=True)

            elif see == "2nd Installment":
                stl.markdown(f"""
                    <div class="card">
                        <h4>2nd Installment (Due: September 14, 2025):</h4>
                        <p>{res[2]:.2f} BDT</p>
                    </div>
                """, unsafe_allow_html=True)

            elif see == "3rd Installment":
                stl.markdown(f"""
                    <div class="card">
                        <h4>3rd Installment (Due: October 12, 2025):</h4>
                        <p>{res[3]:.2f} BDT</p>
                    </div>
                """, unsafe_allow_html=True)
