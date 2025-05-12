#v 5 digit zip code must be valid
#guest names should not repeat consecutively
#atleast one ZIP should be divisible by 7

#defining a function to loop through a guest list
def check_guest_list(guests):
    lucky_found = False
    last_name = None
    
    for name, zip_code in guests:
        print(f"Checking {name} with ZIP {zip_code}")
        
        if len(zip_code) != 5 or not zip_code.isdigit():
            print(f"Invalid ZIP code for {name}: {zip_code}")
            return False
        
        if name == last_name:
            print(f"{name} appeared twice in a row")
            return False
        
        last_name = name
        
        if int(zip_code) % 7 == 0:
            print(f"{zip_code} is divisible by 7")
            lucky_found = True
        
    return lucky_found

guests = [
    ('Alice', '12345'),  # Valid ZIP, no repeat
    ('Bob', '23456'),    # Valid ZIP, no repeat
    ('Alice', '12345'),  # Same name as previous (should trigger repeat check)
    ('Charlie', '77777'), # Lucky ZIP (divisible by 7)
    ('David', '54321')   # Valid ZIP, no repeat, not divisible by 7
]

result = check_guest_list(guests)
print("Result:", result)
