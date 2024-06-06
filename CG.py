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

def calculate(num1, num2, operation):
    if operation == 'Add':
        return num1 + num2
    elif operation == 'Subtract':
        return num1 - num2
    elif operation == 'Multiply':
        return num1 * num2
    elif operation == 'Divide':
        return num1 / num2

stl.title('Simple Calculator')

num1 = stl.number_input('Enter first number')
num2 = stl.number_input('Enter second number')
operation = stl.selectbox('Choose an operation', ['Add', 'Subtract', 'Multiply', 'Divide'])

if stl.button('Calculate'):
    result = calculate(num1, num2, operation)
    st.write('The result is ', result)
