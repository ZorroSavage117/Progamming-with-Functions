# page start
from datetime import datetime
print()

# varables
current_time = datetime.now()
day = current_time.weekday()
total = 0
subtotal = 0
discount = 0.10
dis_total = 0
discount_tf = False
tax = 0.06
tax_total = 0

# functions


def dis_tf(x, y):
    if (x == 1 or x == 2) and y >= 50:
        return True


def cum_discount(x, y):
    z = x * y
    return z


def cum_tax(x, y):
    z = x * y
    return z


def cum_total(x, y):
    z = x + y
    return z


# main code
subtotal = float(input("Subtotal: "))

# page set up
print()

# output
discount_tf = dis_tf(day, subtotal)
if discount_tf:
    dis_total = cum_discount(subtotal, discount)
    print(f"Discount: {dis_total:.2f}")
    subtotal -= dis_total

tax_total = cum_tax(subtotal, tax)
print(f"Sales Tax: {tax_total:.2f}")

total = cum_total(subtotal, tax_total)
print(f"Total: {total:.2f}")

# page end
print()
