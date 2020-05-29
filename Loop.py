

i = 35 
Age = input("Age:")

if int(Age) < 35:
    print ("You are too young, You must be at least 35 years old. ")
   
    
else:
    print ( "Born in the U.S.?: Yes/No ")

Answer = input()

if Answer == 'Yes':
    
    print ('Years of Residency: ', int(Age))

else:
    x = int(Age) - i
    print ('Years of Residency: ', i)
 
  
