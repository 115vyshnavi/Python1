p, q = 399, 2
subtotal = p * q
discount = subtotal * 0.15
tax = (subtotal - discount) * 0.13
final = subtotal - discount + tax
print(f"Sub: {subtotal}, Disc: {discount}, Tax: {tax}, Final: {final}")
