import streamlit as st

from helpers import numberToWords

st.header("Number to Text", divider='blue')
inputNumber = st.number_input("Enter a number", format="%.2f", step=1.)
st.markdown("# The current number is :blue[{}]".format(numberToWords(inputNumber)))