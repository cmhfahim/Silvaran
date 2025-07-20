import streamlit as stl

@stl.experimental_fragment
def payment():
    from helper.fee_calc import fee

    stl.header("Payment Estimator")
    credit = stl.number_input("Enter how many credits you're taking:", min_value=1)
    waiver = stl.selectbox("Select your waiver/scholarship type:", [
        "No Waiver",
        "25% Waiver",
        "50% Waiver",
        "100% Waiver or Scholarship"
    ])
    see = stl.selectbox("What do you want to see?", [
        "See Payment Roadmap",
        "1st Installment",
        "2nd Installment",
        "3rd Installment"
    ])

    # Custom styled button using HTML & query params
    stl.markdown("""
        <style>
            .black-button {
                background-color: black;
                color: white;
                padding: 0.6rem 1.5rem;
                border-radius: 8px;
                text-align: center;
                cursor: pointer;
                font-weight: 500;
                display: inline-block;
                transition: background 0.3s ease;
                margin-top: 10px;
            }
            .black-button:hover {
                background-color: #222;
            }
        </style>
        <div class="black-button" onclick="window.location.href='?payment_clicked=1'">
            See payments Roadmap
        </div>
    """, unsafe_allow_html=True)

    # Check if button was clicked via query param
    query_params = stl.experimental_get_query_params()
    if "payment_clicked" in query_params:
        stl.experimental_set_query_params()  # clear query param after click
        res = fee(credit, waiver)

        if waiver == "100% Waiver or Scholarship":
            if see == "See Payment Roadmap":
                stl.markdown(f"""
                <div style="background: transparent; color: black; padding: 1rem;">
                    <p><strong>You Have to Pay Total:</strong> {res}</p>
                    <p>Remain balance will be adjusted</p>
                </div>
                """, unsafe_allow_html=True)
            else:
                stl.markdown(f"""
                <div style="background: transparent; color: black; padding: 1rem;">
                    <p>You don't need to pay in this installment</p>
                </div>
                """, unsafe_allow_html=True)
        else:
            if see == "See Payment Roadmap":
                stl.markdown(f"""
                <div style="background: transparent; color: black; padding: 1rem;">
                    <p><strong>Total Payment:</strong> {res[0]}</p>
                    <p><strong>1st Installment (Due Aug 13, 2025):</strong> {res[1]}</p>
                    <p><strong>2nd Installment (Due Sep 14, 2025):</strong> {res[2]}</p>
                    <p><strong>3rd Installment (Due Oct 12, 2025):</strong> {res[3]}</p>
                </div>
                """, unsafe_allow_html=True)
            elif see == "1st Installment":
                stl.markdown(f"<p><strong>1st Installment:</strong> {res[1]}</p>", unsafe_allow_html=True)
            elif see == "2nd Installment":
                stl.markdown(f"<p><strong>2nd Installment:</strong> {res[2]}</p>", unsafe_allow_html=True)
            elif see == "3rd Installment":
                stl.markdown(f"<p><strong>3rd Installment:</strong> {res[3]}</p>", unsafe_allow_html=True)
