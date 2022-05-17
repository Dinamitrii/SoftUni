temp = float(input())
if 26.00 <= temp <= 35.00:
    print("Hot")
elif 20.1 <= temp <= 25.9:
    print("Warm")
elif 15.00 <= temp <= 20.00:
    print("Mild")
elif 12.00 <= temp <= 14.9:
    print("Cool")
elif 5.00 <= temp <= 11.9:
    print("Cold")
else:
    print("unknown")
