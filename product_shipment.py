#product_name, quantity, location code
#eahch quantity must be positive
#all product names should be unique
#location code shold be 4 charac
#should stop immediately if a requirement is not fullfilled
#return true if valid

def prod_validation(details):
    products = set()
    for product, quantity, location in details:
        
        if quantity <= 0:
            print(f"Invalid quantity of {product}: {quantity}")
            return False
        
        if product in products:
            print(f"Enter name again, name already present: {products}")
            return False
        
        if (len(location) != 4):
            print(f"Invalid location code: {location}")
            return False 

        products.add(product)
        
    return True

shipments = [
    ('Laptop', 10, 'ABCD'),
    ('Phone', 5, 'EFGH'),
    ('Tablet', 20, 'IJKL'),
    ('Smartwatch', 3, 'MNOP')
]

result = prod_validation(shipments)

print("Are all shipments valid?", result)
