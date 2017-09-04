from collections import defaultdict

vowels = ['a', 'e', 'i', 'o', 'u']
word = input('Provide a word to search for vowels: ')
found = defaultdict(int)

for letter in word:
    if letter in vowels:
        found[letter] += 1

for key, value in sorted(found.items()):
    print(key, 'was found', value, 'time(s).')
