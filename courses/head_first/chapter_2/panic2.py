phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

plist = plist[1:-4]
plist.remove("'")
plist = plist[:2] + plist[3:1:-1] + plist[-1:-3:-1]

new_phrase = ''.join(plist)
print(plist)
print(new_phrase)
