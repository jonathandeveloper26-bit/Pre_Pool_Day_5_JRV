### Task 2.8: Create "superheros" dictionary and print Superman's City

superheros = {
    "Batman": {
        "id": 1, 
        "aliases": ["Bruce Wayne", "Dark Knight"],
        "location": {
            "number": 1007,
            "street": "Mountain Drive",
            "city": "Gotham"
        }
    },
    "Superman":{
        "id": 2, 
        "aliases": ["Kal-el", "Clark Kent", "The Man of Steel"],
        "location": {
            "number": 344, 
            "street": "Clinton Street",
            "apartment": "3D",
            "city": "Metropolis"
        }
    },
}

print(superheros["Superman"]["location"]["city"])

### Task 2.9: Add 'Caped Crusader' to Batman's Aliases, a new superhero called 'Wolverine' with id of 3
superheros["Batman"]["aliases"].append("Caped Crusader")
superheros["Wolverine"] = {"id": 3}

### Task 2.10: Enumerate all Superhero Aliases
for superhero in superheros:
    if "aliases" in superheros[superhero]:
        print(f"{superhero}:")
        for alias in superheros[superhero]["aliases"]:
            print(alias)
        print("")
    else:
        print(f"{superhero}: \nNo aliases found.")