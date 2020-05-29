
#   -------> USER INPUT ---->
user_age = int(input('Please Enter Your age : '))
print('Your Born is U.S ?')
user_born = input('yes or no : ')
residency = int(input('Year\'s of Residency : '))

#   ------> CONDITION ------>
if 14<=residency and user_born == 'yes' and user_age >= 35 :
    print('You are eligible to run for president ')
else:
    print('You are not eligible to run for president')
    print('you are too young')
    print('you must be at least 35 year\'s old')

