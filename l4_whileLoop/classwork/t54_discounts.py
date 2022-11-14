total = 0
price = float(input())
while price > 0:
    if price <= 1000:
        total = total + price
    else:
        total = total + price * 0.95
    price = float(input())
print(total)
