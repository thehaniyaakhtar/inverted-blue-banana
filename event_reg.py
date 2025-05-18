#online event registration system
#name: nonn empty and unique
#age: bw 18 and 60
#event: coding robotics or design
#paid: boolean

#loop for particiant 
#set to ensure unique name
#conditional checks for age event paid status
#helper functions: readability and reuse

def val_name(name):
    return len(name.strip()) > 0

def val_age(age):
    return 18 <= age <= 60

def val_event(event):
    return event in {"coding", "robotics", "design"}

def val_paid(paid):
    return isinstance(paid, bool) and paid is True

def reg_part(participants):
    names = set()
    successful = 0
    
    for name, age, paid, event in participants:
        if name in names:
            print(f"Duplicate name: {name}")
        
        if not(
            val_name(name) and 
            val_event(event) and 
            val_age(paid) and
            val_age(age)
        ):
            print(f"Invalid entry: {name}, {age}, {event}, {paid}")
            continue 
        
        names.add(name)
        successful += 1
        
    return successful 

participants = [
    ("Alice", 25, "coding", True),
    ("Bob", 17, "robotics", True),        # Too young
    ("Charlie", 30, "art", True),         # Invalid event
    ("Alice", 28, "design", True),        # Duplicate name
    ("Dana", 45, "design", False),        # Valid (boolean)
    ("Eve", 22, "robotics", "yes")        # Invalid paid type
]

print("✅ Total successful registrations:", reg_part(participants))
