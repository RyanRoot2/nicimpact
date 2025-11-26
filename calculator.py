import streamlit as st

st.title("National Insurance Impact on Salary Sacrifice")

# --- User Inputs ---
salary = st.number_input("Annual Salary (£)", min_value=0.0, step=1000.0)
sacrifice_pct = st.number_input("Employee Salary Sacrifice (%)", min_value=0.0, max_value=100.0, step=1.0)

# --- Calculations ---
monthly_sacrifice = salary / 12 * (sacrifice_pct / 100)
annual_sacrifice = monthly_sacrifice * 12

# Taxable amount
taxable_amount = annual_sacrifice - 2000
taxable_amount = max(taxable_amount, 0)  # cannot be negative

# Tax calculation
if salary < 50270:
    tax = taxable_amount * 0.08
else:
    tax = taxable_amount * 0.02

# --- Output ---
st.subheader("Results")
st.write(f"**Monthly Salary Sacrifice Amount:** £{monthly_sacrifice:,.2f}")
st.write(f"**Annual Salary Sacrifice Amount:** £{annual_sacrifice:,.2f}")
st.write(f"**Amount Eligible for NICs:** £{taxable_amount:,.2f}")
st.write(f"**NIC Bracket:** 8% Below £50,270 and 2% £50,270 and above")
st.write(f"**Annual Increase in NICs:** £{tax:,.2f}")
st.write(f"**Monthly Increase in NICs:** £{tax / 12:,.2f}")