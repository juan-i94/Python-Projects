print("Welcome to dnd character creator")

char_name = None

print("What's your character's name?")
char_name = input()

print(f"Hello, {char_name}")

stats = {'STR': 8, 
         'DEX': 8, 
         'CON': 8, 
         'INT': 8, 
         'WIS': 8, 
         'CHA': 8}

std_array = [15,14,13,12,10,8]

print("Now lets choose your stats!")
print("Let's use standard array for now")
print("you can choose between the numbers on this list and assign them to your stats:")
print(std_array)

for stat, score in stats.items():
    while True:
        print(f"choose {stat} score")
        print(f"remaining scores: {std_array}")
        choice = input()
        try:
            if int(choice) in std_array:
                stats[stat] = int(choice)
                std_array.remove(int(choice))
                break
            else:
                print("you gotta choose an available score")
        except ValueError:
            print("no text, try again.")
for stat, score in stats.items():
        print(f"{stat}: {score}\n")
