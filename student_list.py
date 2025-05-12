#list of students
#name of student, age, course
#function checks: age, no name should be put in twice, 
#course name: "Math", "Science", "History", or "English"
#invalid info, false
#if all checks passed, return true in the end
def students(list):
    valid_course = ["Math", "Science", "History", "English"]
    last_name = None
    
    for name, age, course in list:
        print(f"Checking {name}, {age} in {course}.")
        return False

        if age<18 or age>30:
            print(f"Invalid age for {name}")
            return False
        
        if course not in valid_course:
            print(f"Invalid course for {name}")
            return False
        
        if name == last_name:
            print(f"Duplicate consecutive name: {name}")
            return False
        
        last_name == name
            
    return True

lists = [
    ('John', 20, 'Math'),
    ('Sarah', 22, 'Science'),
    ('John', 19, 'History'),
    ('Sarah', 25, 'Math')
]

result = students(lists)
print("Results: ", result)