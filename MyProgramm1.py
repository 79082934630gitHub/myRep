def get_vowels(String):
    return [each for each in String if each in "aeiou"]
get_vowels("animal") # [a, i, a]
get_vowels("sky") # []
get_vowels("football") # [o, o, a]

def capitalize(String):
    return String.title()
print(capitalize("shop")) # [Shop]
print(capitalize("python programming")) # [Python Programming]
print(capitalize("how are you!")) # [How Are You!]

input('Press ENTER to exit') 
