students = [("Ali", ["Fizika", "Matematika"]),
            ("Laylo", ["Ingliz tili"]),
            ("Jasur", ["Matematika", "Informatika"])
]

count=0
for x in students:
    if "Matematika" in x[1]:
        count+=1

print(count)        
