#delet duplicate number 
numbers = [1, 8, 7, 5, 3, 10, 8, 3]
unique = []

for number in numbers:
    if number not in unique:
        unique.append(number)
print(unique)
    



