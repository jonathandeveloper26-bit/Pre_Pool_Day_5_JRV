### Task 2.4
print("Task 2.4: Create Dictionary with Empty Keys")
types = {"Electric": [], "Grass": [], "Fire": []}
print(types)

### Task 2.5
print("Task 2.5: Add Pokemon to Dictionary as Values")
types["Electric"].append("Pikachu")
types["Grass"].extend(["Bulbasaur", "Leafeon"])
types["Fire"].extend(["Charmander", "Scovillain"])

### Task 2.6
print("Task 2.6: Print Keys Only")
for key in types:
    print(key)

### Task 2.7
print("Task 2.7: Search for Pikachu Type")
search_for = "Pikachu"
for key in types:
    if search_for in types[key]:
        print(key)
    else:
        continue

