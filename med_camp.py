#name non empty, unique
#age: 10 and 90
#gender: male, female, other
#ailment: "vision", "hearing", "dental", "general"
#consent: True

#helper functions to validate each field:
def valid_name(name):
    return len(name.strip()) > 0

def valid_age(age):
    return 10 < age < 90

def valid_gender(gender):
    return gender in {"male", "female", "other"}

def valid_ailment(ailment):
    return ailment in {"vision", "hearing", "dental", "general"}

def valid_consent(consent):
    return isinstance(consent, bool) and consent is True

def valid_info(patient):
    ailment_counts = {}
    names = set()
    successful = 0
    error = set()
    for name, age, gender, ailment, consent in patient:
        if name in names:
            print(f"Duplicate name, {name}")
            continue
        
        if not (
            valid_age(age) and 
            valid_ailment(ailment) and 
            valid_consent(consent) and 
            valid_gender(gender) and 
            valid_name(name)
        ):
            print(f"Invalid info {name}, {age}, {consent}, {ailment}, {gender}")
            continue
        
        names.add(name)
        
        if ailment in ailment_counts:
            ailment_counts[ailment] = ailment_counts.get(ailment, 0) + 1
            
        successful += 1
    
    return successful, ailment_counts
        
        
participants = [
    ("Asha", 34, "female", "vision", True),
    ("Raj", 40, "male", "hearing", True),
    ("Reema", 60, "female", "vision", True),
    ("Ali", 45, "male", "dental", True),
    ("Raj", 22, "male", "general", True)  # duplicate name!
]

result = valid_info(participants)
print(result)       