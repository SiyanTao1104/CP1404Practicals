"""
CP1404/CP5632 - Practical
Student: Siyan Tao
Electricity_bill
Create an electricity bill estimator
"""

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928
print("Electricity bill estimator 2.0")
tariff = int(input("Which tariff? 11 or 31: "))
daily_use_kwh = float(input("Enter daily use in kwh: "))
days = int(input("Enter number of billing days: "))
if tariff == 11:
    tariff = TARIFF_11
elif tariff == 31:
    tariff = TARIFF_31
bill = tariff * daily_use_kwh * days
print("Estimated bill: ${:.2f}".format(bill))