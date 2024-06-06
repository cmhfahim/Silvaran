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


from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLineEdit, QVBoxLayout

class CalculatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Simple Calculator')
        self.createApp()

    def createApp(self):
        # Create the layout
        grid = QGridLayout()
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '.', '0', '=', '+',
            'C'
        ]

        row = 0
        col = 0

        self.line_edit = QLineEdit()

        # Add buttons to the layout
        for button_text in buttons:
            button = QPushButton(button_text)
            if button_text == 'C':
                grid.addWidget(button, row, 0, 1, 4)
                button.clicked.connect(self.clear_text)
            else:
                grid.addWidget(button, row, col)
                button.clicked.connect(self.button_clicked)
                col += 1
                if col > 3:
                    col = 0
                    row += 1

        vbox_layout = QVBoxLayout()
        vbox_layout.addWidget(self.line_edit)
        vbox_layout.addLayout(grid)
        self.setLayout(vbox_layout)

    def button_clicked(self):
        button_text = self.sender().text()
        line_edit_text = self.line_edit.text()
        if button_text == '=':
            try:
                self.line_edit.setText(str(eval(line_edit_text)))
            except Exception as e:
                self.line_edit.setText(str(e))
        else:
            self.line_edit.setText(line_edit_text + button_text)

    def clear_text(self):
        self.line_edit.setText('')

app = QApplication([])
window = CalculatorApp()
window.show()
app.exec_()

