emails = (
    ("Ali", "ali@gmail.com"), 
    ("Vali", "vali@yandeks.ry"), 
    ("Sami", "sami@mail.ru")
)
domains=[]

for email in emails:
    domain=email[1].split("@")[1]
    domains.append(domain)


print(domains)