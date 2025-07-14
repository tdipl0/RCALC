import streamlit as st

st.title("Ronan's Calculator")

# Inputs
a = st.number_input("Enter A")
b = st.number_input("Enter B")

# Operation selection
operation = st.selectbox("Choose an operation", ["Add", "Subtract", "Multiply", "Divide"])

# Calculate
if st.button("Calculate"):
    if operation == "Add":
        result = a + b
    elif operation == "Subtract":
        result = a - b
    elif operation == "Multiply":
        result = a * b
    elif operation == "Divide":
        if b != 0:
            result = a / b
        else:
            st.error("Cannot divide by zero!")
            result = None
    if result is not None:
        st.success(f"Result: {result}")

