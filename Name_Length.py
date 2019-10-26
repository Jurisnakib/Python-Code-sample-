name = input("Enter your name: ")
if len(name) < 3:
    print('Name must be at least 3 Charecter')
elif len(name)>50:
    print("Name must be maximum 50 charecter")
else:
    print('Well done!!!')