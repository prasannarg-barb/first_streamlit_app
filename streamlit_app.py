import streamlit as st

st.title("Welcome to our Data App")

st.header("Barb IB Calc")

#st.text("Plain Text1")
#st.text("Plain Text2")
#st.text("Plain Text3")

TQ_curr_price = st.number_input('Enter TQ Current Price:')
TQ_target_price = st.number_input('Enter TQ Target Price:')
QLD_curr_price = st.number_input('Enter QLD Current Price:')
QLD_target_price = QLD_curr_price+ (((TQ_target_price - TQ_curr_price ) / TQ_curr_price)*(2/3)*QLD_curr_price)

st.header(st.write('The QLD Target Price is::', QLD_target_price))
