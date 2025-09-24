people =[("Ali", 24),
         ("Laylo", 30), 
         ("Jasur", 19)
]
mx=people[0]
for x in people:
    if x[1]>mx[1]:
        mx=x
    
print(mx)    