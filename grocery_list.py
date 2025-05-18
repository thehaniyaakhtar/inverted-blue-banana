# Requirements:
# item_name: Non-empty string, must be unique in the cart.
# category: Must be one of "fruits", "vegetables", "dairy", "snacks".
# price: Must be a positive float.
# quantity: Must be a positive integer.

# Outputs:
# After validating the cart:
# Print a message if any item is invalid or a duplicate.

# Return:
# Total cost of the cart (i.e. price × quantity for each valid item).
# A dictionary that shows how many items were bought in each category.

def item_name(name):
    return isinstance(name, str) and len(name.strip()) > 0

def valid_category(category):
    return category in {"fruits", "vegetables", "dairy", "snacks"}

def valid_price(price):
    return isinstance(price, float) and price > 0

def valid_quantity(quantity):
    return isinstance(quantity, int) and quantity > 0

def grocery(cart):
    seen_names = set()
    category_counts = {}
    total_cost = 0.0
    
    for name, category, price, quantity in cart:
        
        if name in seen_names:
            print(f"Duplicate name, {name}")
            continue
            
        if not(
            item_name(name) and 
            valid_quantity(quantity) and 
            valid_category(category) and 
            valid_price(price)
        ):
            print(f"Invalid information {name}, {quantity}, {category}, {price}")
            continue
        
        item_name.add(name)
        
        category_counts[category] = category_counts.get(category, 0) + quantity
            
        total_cost += price * quantity
    
    return total_cost, category_counts
        
        
    
    