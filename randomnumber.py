import random

roll = 0
count = 0

while roll != 10:
    count = count + 1
    roll = random.randint(1, 10)

print(f'It took {count} rolls to rol a 5!')