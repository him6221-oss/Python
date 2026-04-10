# SUPER BASIC Coffee POS - Sprint 5 Complete
# Beginner Style - First Semester Look

import datetime

# --- Constants ---
TAX_RATE = 0.05
DATA_FILE = "order_history.txt"
ORDER_REPORT = "Order_report.txt"

# --- Get customer info ---
name = input("Customer Name: ")
room = input("Office Number: ")

# --- Get order info ---
print("Menu: Coffee, Tea, Cocoa")
drink = input("Drink: ")
size = input("Size (Small/Medium/Large): ")
milk = input("Milk (Dairy/Oat/Almond/Soy/Coconut): ")
pumps = input("Number of syrup pumps: ")
try:
    pumps = int(pumps)
except:
    pumps = 0

# --- price calculation ---
price = 4.00
if drink == "Coffee":
    if size == "Small": price = 3.00
    if size == "Medium": price = 4.00
    if size == "Large": price = 5.00
if drink == "Tea":
    if size == "Small": price = 2.50
    if size == "Medium": price = 3.50
    if size == "Large": price = 4.50
if drink == "Cocoa":
    if size == "Small": price = 3.50
    if size == "Medium": price = 4.50
    if size == "Large": price = 5.50

total = price + pumps * 0.10
tax = total * TAX_RATE
total = total + tax

# --- Save raw data ---
f = open(DATA_FILE, "a")
f.write(name + "," + room + "," + str(total) + "\n")
f.close()

# --- Save readable receipt ---
f = open(ORDER_REPORT, "w")
f.write("BARISTA RECEIPT - " + str(datetime.date.today()) + "\n")
f.write("Customer: " + name + " | Room: " + room + "\n")
f.write("Tax: $" + str(round(tax,2)) + " | Total: $" + str(round(total,2)) + "\n")
f.close()

print("\n Order saved!")
print("You can open ORDER_report.txt to see the receipt.")

# --- Review past orders ---
print("\n--- PAST ORDERS ---")
try:
    f = open(DATA_FILE, "r")
    for line in f:
        print(line.strip())
    f.close()
except:
    print("No past orders found.")