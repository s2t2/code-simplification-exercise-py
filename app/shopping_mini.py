
from datetime import datetime
import os

# GOAL 1: simplify USD formatting
# GOAL 2: simplify the tax rate
# GOAL 3: simplify receipt printing / file writing


selected_products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
] # FYI: for the purposes of this exercise, you won't need to modify this list at all

def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71

checkout_at = datetime.now().strftime("%M/%d/%Y %I:%m %p")

now = datetime.now()

subtotal = sum([p["price"] for p in selected_products])

# PRINT RECEIPT

receipt = ""

receipt += "\n---------"
receipt += "\nCHECKOUT AT: " + str(now.strftime("%Y-%M-%d %H:%m:%S"))
receipt += "\n---------"

for p in selected_products:
    receipt += "\nSELECTED PRODUCT: " + p["name"] + "   " + to_usd(p["price"])

receipt += "\n---------"
receipt += f"\nSUBTOTAL: {to_usd(subtotal)}"
receipt += f"\nTAX: {to_usd(subtotal * 0.0875)}"
receipt += f"\nTOTAL: {to_usd((subtotal * 0.0875) + subtotal)}"
receipt += "\n---------"
receipt += "\nTHANK YOU! PLEASE COME AGAIN SOON!"
receipt += "\n---------"

print(receipt)

# WRITE RECEIPT TO FILE

file_name = os.path.join(os.path.dirname(__file__), "..", "receipts", f"{now.strftime('%Y-%M-%d-%H-%m-%S')}.txt")
with open(file_name, 'w') as f:
    f.write(receipt)

# TODO: SEND RECEIPT VIA EMAIL

# todo: sent the receipt variable
