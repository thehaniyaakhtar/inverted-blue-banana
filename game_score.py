#score tracker
#each player has a name, score, level, bonus aplied
#name" always uniqye
#score should be 1-10
#helper function to check validte level
def is_valid(level):
    return 1 <= level <= 10

def scores(players):
    info = set()
    for name, score, level, bonus_applied in players:
        
        if name in info:
            print(f"Name is already present ,{name}")
            return False
        
        if score < 0 or score >10:
            print("Invalid level")
            return False
        
        if not is_valid(level):
            print(f"Invalid level for {name}: {level}")
            return False
            
        info.add(name)
    return True

test_players = [
    ("Alice", 8, 5, False),
    ("Bob", 10, 2, True),
    ("Charlie", 4, 11, False)  # Invalid level!
]
        
result = scores(test_players)
print("Result", result)