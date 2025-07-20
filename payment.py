import streamlit as stl
from streamlit_lottie import st_lottie
import json
import requests

@stl.experimental_fragment
def payment():
    stl.markdown("<h2 style='text-align: center; color: #E7D2CC;'>Payment Roadmap</h2>", unsafe_allow_html=True)
    def url(url):
        req=requests.get(url)
        if req.status_code !=200:
            return None
        return req.json()
    ur=url("https://lottie.host/e817d581-61a3-4c3f-bcaf-5f5d1a1c0f7e/cET0KKA2E0.json")
    st_lottie(ur,height=300,key="Payment")
    def fee(credit,waiver):
            remain_amount=0
            tution_fee=(5525*credit)

            if waiver=="0% Waiver or Scholarship":
                remain_amount=100
            elif waiver=="25% Waiver or Scholarship":
                remain_amount=75
            elif waiver=="50% Waiver or Scholarship":
                remain_amount=50
            elif waiver=="100% Waiver or Scholarship":
                remain_amount=0

            discount_total_fee_1=((tution_fee*(remain_amount/100)))+6500
            if waiver=="100% Waiver" :
                return discount_total_fee_1
            else:
                
                installment_1=discount_total_fee_1*(40/100)
                reamin_fee=discount_total_fee-installment_1
                installment_2=reamin_fee/2
                reamin_fee-=installment_2
                installment_3=installment_2
                lst=[discount_total_fee_1,installment_1,installment_2,installment_3]
                return lst

        

    credit_1=stl.number_input("Enter Your Total Credits (Non-Retake): ")
    credit_2=stl.number_input("Enter Your Total Credits (Retake): ")

    credit=(credit_1+(credit_2)/2)
    waiver = stl.selectbox('Please Provide Necessery Information', ['0% Waiver', '25% Waiver', '50% Waiver', '100% Waiver'])

    see = stl.selectbox('Enter your Choice', ['See Payment Roadmap', '1st Installment', '2nd Installment', '3rd Installment'])

    if stl.button("See payments Roadmap"):
        res=fee(credit,waiver)
        if waiver=="100% Waiver or Scholarship":
            if see=="See Payment Roadmap":
                    stl.write("You Have to Pay Total:",res)
                    stl.write("Remain balance will be adjusted")
            else:
                    stl.write("You don't need to pay in this installment")
            
        else:
            if see=="See Payment Roadmap":
                    stl.write("You Have to Pay Total:",res[0])
                    stl.write(" Pay your First Installment before: August 13, 2025:",res[1])
                    stl.write("Pay your Second Installment before: September 14, 2025:",res[2])
                    stl.write("Pay your Third Installment before: October 12, 2025:",res[3])

            elif see=="1st Installment":

                    stl.write(" Pay your First Installment before: August 13, 2025:",res[1])

            elif see=="2nd Installment":
                    stl.write("Pay your Second Installment before: September 14, 2025:",res[2])

            elif see=="3rd Installment":
                    stl.write("Pay your Third Installment before: October 12, 2025:",res[3])
