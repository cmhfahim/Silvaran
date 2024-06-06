import streamlit as st

def calculate(num1, num2, operation):
    if operation == 'Add':
        return num1 + num2
    elif operation == 'Subtract':
        return num1 - num2
    elif operation == 'Multiply':
        return num1 * num2
    elif operation == 'Divide':
        return num1 / num2

st.title('Simple Calculator')

num1 = st.number_input('Enter first number')
num2 = st.number_input('Enter second number')
operation = st.selectbox('Choose an operation', ['Add', 'Subtract', 'Multiply', 'Divide'])

if st.button('Calculate'):
    result = calculate(num1, num2, operation)
    st.write('The result is ', result)
