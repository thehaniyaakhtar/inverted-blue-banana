#every delivery: only digits- 6, unique string
#driver_name, non repetitve
#packages: a list of positive int, each having weight in kg, >0
#priority: either low medium high
#helper for packages

def valid_packages(packages):
    for weights in packages:
        if weights <= 0:
            return False
    return True

def validate_deliveries(deliveries):
    id = set()
    driver = set()
    
    for delivery_id, driver_name, packages, priority in deliveries:
        
        if (
            delivery_id in driver or
            len(delivery_id) != 6 or
            not delivery_id.isdigit()
        ):
            print(f"Invalid delivery id: {delivery_id}")
            return False
        
        id.add(delivery_id)

        if driver_name in driver:
            print(f"Name is already present, {name}")
            return False
        driver.add(driver_name)
        
        if not valid_packages(packages):
            print(f"Invalid package for {delivery_id}")
            return False
        
        if priority not in {"High", "Low", "Medium"}:
            print(f"Invalid priority {priority}")
            return False
        
    
    return True
    
deliveries = [
    ("123456", "Alice", [2, 5, 1], "High"),
    ("654321", "Bob", [3, 4], "Medium"),
    ("112233", "Charlie", [0], "Low") 
]

print(validate_deliveries(deliveries))