# Step 1: Input
a = float(input("YEN listing in mercari: "))

# Step 2: Add based on range
if 300 <= a <= 999:
    a += 100
elif 1000 <= a <= 3999:
    a += 200
elif 4000 <= a <= 9999:
    a += 300

# Step 3: Calculate b = 4.1% fee added
b = a * 1.041

# Step 4: Add 50 yen
c = b + 50

# Step 5: Convert JPY to INR
x = c / 1.5844

# Step 6: Add 5% profit
d = x * 1.05

# Step 7: Output
print("\n----- Result -----")
print(f"total incl gns fees (in JPY): ¥{c:.2f}")
print(f"output from paypal: ₹{x:.2f}")
print("-------------------")
