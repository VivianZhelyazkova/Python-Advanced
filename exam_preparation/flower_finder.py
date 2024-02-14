from collections import deque

vowels = deque(input().split())
consonants = deque(input().split())

flowers = {
    "rose": ["r", "o", "s", "e"],
    "tulip": ["t", "u", "l", "i", "p"],
    "lotus": ["l", "o", "t", "u", "s"],
    "daffodil": ["d", "a", "f", "f", "o", "d", "i", "l"]

}
flower_found = ""
while vowels and consonants:
    vowel = vowels.popleft()
    consonant = consonants.pop()
    for flower, value in flowers.items():
        if vowel in value:
            value.remove(vowel)
        if consonant in value:
            value.remove(consonant)
        if not value:
            flower_found = flower
            break
    if flower_found:
        break

if flower_found:
    print(f"Word found: {flower_found}")
else:
    print("Cannot find any word!")

if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")
