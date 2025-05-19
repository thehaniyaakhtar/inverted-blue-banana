# customer_name: non-empty, unique per day.
# car_type: one of "sedan", "suv", "hatchback", "convertible".
# rental_days: a positive integer.
# daily_rate: a positive float

# Returns:
# Total revenue from all valid rentals.
# A dictionary showing how many cars were rented per car type.

#helper functions
def valid_name(name):
    return len(name.strip()) > 0

def valid_cartype(type):
    return type in {"sedan", "suv", "hatchback", "convertible"}

def rental_days(days):
    return isinstance(days, int) and days > 0

def daily_rate(rate):
    return isinstance(rate, float) and rate > 0

def car_rental(info):
    
    seen_cars = set()
    revenue = 0.0
    car_count = {}
    
    for name, type, days, rate in info:
            if name in seen_cars:
                print(f"Duplicate Entry, {name}")
                continue
                
            if not(
                valid_name(name) and
                valid_cartype(type) and 
                rental_days(days) and 
                daily_rate(rate)
            ):
                print(f"Invalid values {name}, {type}, {days}, {rate}")
                continue
            
            seen_cars.add(name)
            car_count[type] = car_count.get(type, 0) + days
            
            revenue += days * rate
            
    return revenue, car_count
        
data = [
    ("Alice", "sedan", 3, 45.0),
    ("Bob", "suv", 2, 60.0),
    ("Charlie", "convertible", 1, 100.0),
    ("Alice", "sedan", 2, 50.0),  # Duplicate
    ("Dan", "truck", 2, 55.0),    # Invalid type
]

revenue, count = car_rental(data)
print("Total Revenue:", revenue)
print("Car Type Counts:", count)
