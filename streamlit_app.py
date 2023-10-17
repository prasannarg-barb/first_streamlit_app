import streamlit as st

streamlit.title("Welcome to our Data App")

streamlit.header("Header Text")
streamlit.text("Plain Text1")
streamlit.text("Plain Text2")
streamlit.text("Plain Text3")


name = input("Enter your name: ")
print("Hello " + name + " !")


TQ_curr_price = st.number_input('Enter TQ Current Price:')
TQ_target_price = st.number_input('Enter TQ Target Price:')
QLD_curr_price = st.number_input('Enter QLD Current Price:')
QLD_target_price = QLD_curr_price+ (((TQ_target_price - TQ_curr_price ) / TQ_curr_price)*(2/3)*QLD_curr_price)

st.write('The QLD Target Price is::', QLD_target_price)
