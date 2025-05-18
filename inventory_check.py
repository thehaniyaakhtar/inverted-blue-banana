# A name (string, non-empty, unique)
# Quantity (positive integer)
# Price (positive float)

#validate each item 
#track uniqueness of names
#loop to process list
#calulate the total inventory value

#helper functions
def valid_name(name):
    return len(name.strip()) > 0

def valid_quantity(quantity):
    return isinstance (quantity, int) and quantity > 0

def valid_price(price):
    return isinstance(price, (int, float)) and price > 0

def inventory_value(items):
    names = set()
    total_value = 0
    
    for name, quantity, price in items:
        if name in names:
            print(f"Duplicate name found, {name}")
            continue
        
        if not (
            valid_name(name) and
            valid_quantity(quantity) and
            valid_price(price)
        ):
            print(f"Invalid entry: {name}, {price}, {quantity}")
            continue
            
        names.add(name)
        total_value += quantity*price
    
    return total_value

items_list = [
    ("Apples", 10, 2.5),
    ("Bananas", 5, 1.2),
    ("", 3, 2.0),            # Invalid name
    ("Oranges", -4, 3.0),    # Invalid quantity
    ("Apples", 6, 2.5),      # Duplicate
    ("Grapes", 8, 0),        # Invalid price
    ("Pears", 4, 3.5)
]

print("Total Inventory Value:", inventory_value(items_list))