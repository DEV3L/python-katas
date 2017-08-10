phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

plist.pop(0)  # on't panic!
plist.pop(2)  # ont panic!
plist.pop(6)  # ont paic!
plist.pop(6)  # ont pac!
plist.pop(6)  # ont pa!
plist.pop(6)  # ont pa
plist.insert(2, plist.pop(3))  # on tpa
plist.insert(4, plist.pop(5))  # on tap

new_phrase = ''.join(plist)
print(plist)
print(new_phrase)
