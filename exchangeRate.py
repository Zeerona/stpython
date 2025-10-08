import streamlit as st
import requests

st.title("อัตราแลกเปลี่ยนจาก USD")

# ดึงข้อมูลจาก API
url = "https://v6.exchangerate-api.com/v6/becb6d0056b966b9af5308f4/latest/USD"
response = requests.get(url)
data = response.json()
rates = data["conversion_rates"]

# รายการสกุลเงินให้เลือก
ls_rate = ["THB", "JPY", "EUR", "GBP", "AED"]

# ✅ กำหนดค่าเริ่มต้น (ค่าแรกจะเป็น THB)
default_currency = ls_rate[0]

# แสดงผลเริ่มต้นก่อน
st.subheader(f"1 USD = {rates[default_currency]:,.2f} {default_currency}")

# จากนั้นให้ผู้ใช้เลือกสกุลเงินอื่น
rate = st.selectbox("เลือกสกุลเงินอื่น", ls_rate, index=0)

# เมื่อเลือกแล้ว แสดงผลด้านล่าง
st.write(f"1 USD = {rates[rate]:,.2f} {rate}")



