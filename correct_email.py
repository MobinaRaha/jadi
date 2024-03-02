import re
email = input("E-mail: ")

if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$' ,email):
    print("OK")
else:
    print("WRONG!")


