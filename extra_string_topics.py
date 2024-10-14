# operations with strings and values

character_class = "wizard"
character_race = "gnome"
character_mana = 50

# I want to print the string "Your character is a wizard gnome with 50 mana"

# by joining strings and values with string addition (concatenation)
print("Your character is a " + character_class + " " +  character_race + " with " + str(character_mana) + " mana")
# use str() to typecast a value to a string type

# by joining strings and values with commas
print('Your character is a',character_class,character_race,"with",character_mana ,"mana")
# don't need to worry about spaces with commas

print(f"Your character is a {character_class} {character_race} with {character_mana} mana.")

# multiplication
print("There is an","echo " *5)

print("a"*20)
long_string = "abc"*10
print(long_string)
print(f"You're a {character_class} "*4)
print(f"You're a {character_class *4}")

# print the following
# ask the user how many times they want to cast their spell if each cast is 10 mana
# if they use more than 50 mana, just default to 5
cast = int(input("How many times do you want to cast a spell? (Each cast cost 10 mana)"))
if cast >= 0 and cast <= 5:
    print("The", character_class, character_race, "cast a fire spell", cast, "times")
    print("|===o"," ~~~X X X~~~      "*cast)
else:
    print("The", character_class, character_race, "cast a fire spell 5 times")
    print("|===o"," ~~~X X X~~~      "*5)

# print the following (if n were 3)
# "The {class} {race} cast a fire spell {n} times" (use any method you want)
# |===o  ~~ x x x ~~    ~~ x x x ~~    ~~ x x x ~~ (use multiplication)

