import streamlit as st

def format_phone_number(number: str) -> str:
    # Remove non-digit characters
    digits = ''.join(filter(str.isdigit, number))
    if len(digits) != 10:
        return "❌ Please enter exactly 10 digits."
    return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"

# Streamlit App
st.set_page_config(page_title="📞 Phone Number Formatter", layout="centered")
st.title("📞 Phone Number Formatter")
st.markdown("Format your 10-digit phone number into a readable style: **(XXX) XXX-XXXX**")

user_input = st.text_input("Enter a 10-digit phone number:")

if user_input:
    formatted = format_phone_number(user_input)
    st.success(f"Formatted Number: {formatted}")
