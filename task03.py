words = ("apple", "banana", "strawberry", "kiwi")

mx = "" 
for word in words:
    if len(word) > len(mx): 
        mx = word

print(mx) 