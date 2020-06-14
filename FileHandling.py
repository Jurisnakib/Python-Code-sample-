#here we learn how to read file 

f = open("TestText.txt", "r")

#Read Line by line 
# print(f.readline())
# print(f.readline())

#Read total file 
#print(f.read())

#loop on file line
# for x in f:
#     print(x)

print(f.readline())
f.close()
