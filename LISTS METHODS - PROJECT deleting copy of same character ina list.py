#perfect perfection
#lists methods - PROJECT REMOVING  copy of same character in a list
#the number in list would not be in the empty list therefore the condition becomes false therefore to convert it into true condition we used not function it would take only one character by the use use of not function and whenever the same number repeats then the condition becomes true but because of not function the condition becomes false
#In this way the characters repeating gets terminated or removed
#And all the unique characters  are saved in the empty list
#perfect perfection

lists=[44,55,66,77,55,66,44,22,11,1,22,2,33,3,44,4,55,5]
lists=[44,55,66,77,55,66,44,22,11,1,22,2,33,3,44,4,55,5,6]
unique=[]
for lister in lists:
    if lister not in unique:
        unique.append(lister)
print(unique)






