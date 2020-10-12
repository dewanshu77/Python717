# TUPLES
#THESE ARE REPRESENTED BY THOSE'()'
#The data of tuples cannot be changed after the value being declared in the tuple's at the first time
#understand and implement like this
#code begins here

tuples_variable=(15,15,12,13,14,19,20,70)
#if we changed the values after tuple being declared then
#it gives us the value error because The data of tuples cannot be changed after the value being declared in the tuple's at the first time
#so moving towards the topic
print(tuples_variable)
#it allows only two methods that are used in list's methods
#they are:
#1=.count()
#2=.index()
#other methods for tuples are called magic methods

#1=.count method, gives no. of occurences of character
print(tuples_variable.count(15))
#2=.index(),gives index of the first occurence of the particular character
print(tuples_variable.index(15))
print(tuples_variable.index(70))
print('perfect perfection')
