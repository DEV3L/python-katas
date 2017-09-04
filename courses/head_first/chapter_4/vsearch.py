def search4vowels():
    vowels = set('aeiou')
    word = input('Provide a word to search for vowels: ')
    found = vowels.intersection(set(word))

    for vowel in found:
        print(vowel)


if __name__ == "__main__":
    search4vowels()
