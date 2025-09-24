numbers = (3, 6, 7, 8, 10, 11)

tapl_son=()
for num in numbers:
    if num%2==0:
        tapl_son += (num,) 
        

print(tapl_son)