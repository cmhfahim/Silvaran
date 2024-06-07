import streamlit as stl
def feedback():
    stl.header(":mailbox: Please Give your feedbacks")

    con_form="""
    <form action="https://formsubmit.co/choowdhuryfahim03@gmail.com" methos="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder ="Your Name"required>
        <input type="text" name="email" placeholder ="Your Email"required>
        <textarea name="message" placeholder ="Give your Feedbacks"></textarea>
        <button type ="Submit">Send</button>
    </form>
    """
    stl.markdown(con_form,unsafe_allow_html=True)


    def css(fl):
        with open(fl) as f:
            stl.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
    css("style/style.css")