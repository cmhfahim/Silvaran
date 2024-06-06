import streamlit as stl 

stl.title("Payment Roadmap")

def fee(credit,waiver):
        remain_amount=0
        tution_fee=(5525*credit)

        if waiver=="0% Waiver":
            remain_amount=100
        elif waiver=="25% Waiver":
            remain_amount=75
        elif waiver=="50% Waiver":
            remain_amount=50
        elif waiver=="100% Waiver":
            remain_amount=0

        discount_total_fee_1=((tution_fee*(remain_amount/100)))+6500
        if waiver=="100% Waiver" :
            return discount_total_fee_1
        else:
            reg_pay=15000

            discount_total_fee=discount_total_fee_1-reg_pay
            installment_1=discount_total_fee*(40/100)
            reamin_fee=discount_total_fee-installment_1
            installment_2=reamin_fee/2
            reamin_fee-=installment_2
            installment_3=installment_2
            lst=[discount_total_fee_1,reg_pay,installment_1,installment_2,installment_3]
            return lst

    

credit=stl.number_input("Enter Your Total Credits: ")

waiver = stl.selectbox('Please Provide Necessery Information', ['0% Waiver', '25% Waiver', '50% Waiver', '100% Waiver'])

see = stl.selectbox('Enter your Choice', ['See Payment Roadmap', '1st Installment', '2nd Installment', '3rd Installment'])

if stl.button("See payments Roadmap"):
    res=fee(credit,waiver)
    if waiver=="100% Waiver":
        if see=="See Payment Roadmap":
                stl.write("You Have to Pay Total:",res)
                stl.write("You Have to Pay at registration :",15000)
                stl.write("Remain balance will be adjusted")
        else:
                stl.write("You don't need to pay in this installment")
          
    else:
        if see=="See Payment Roadmap":

                stl.write("You Have to Pay Total:",res[0])
                stl.write("You Have to Pay at registration :",res[1])
                stl.write("First Installment :",res[2])
                stl.write("Second Installment :",res[3])
                stl.write("Third Installment :",res[4])

        elif see=="1st Installment":

                stl.write("First Installment Amount :",res[1])

        elif see=="2nd Installment":
                stl.write("Second Installment Amount :",res[2])

        elif see=="3rd Installment":
                stl.write("Third Installment Amount :",res[3])

stl.title("CGPA Calculator")

def calcg(credits, cgpas):
    lst = [credit * cgpa for credit, cgpa in zip(credits, cgpas)]
    r = sum(lst) / sum(credits)
    return round(r, 3)

credits = stl.text_input("Enter your course credits for this trimester, separated by commas")
cgpas = stl.text_input("Enter your CGPAs for this trimester, separated by commas")

if stl.button("Enter to Calculate CGPA"):
    credits = list(map(float, credits.split(',')))
    cgpas = list(map(float, cgpas.split(',')))
    res = calcg(credits, cgpas)
    stl.write("Your CGPA in this Trimester", res)
