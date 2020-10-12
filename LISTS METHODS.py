#SO  HERE WE ARE GONNA DO THE PRACTICAL USE AND UNDERSTAND THE LIST METHODS
#ALL THE NOTES ARE IN MY NOTEBOOK SO DONT WORRY

# .APPEND METHOD
#ADDS CHARACTER AT THE ENDING OF ALL THE CHARACTERS IN THE LIST
#IMPLEMENTATION IS LIKE THIS

variable_for_whole_file_is=[4,5,2,3,6,1,7,8,9,4,5,2,5,5,5,6,2,5,5,2,5,6,6,6]
variable_for_whole_file_is
variable_for_whole_file_is.append(45)
print(variable_for_whole_file_is)

#.insert method
#It adds particular character that we want to be entered in the list at any place we want ,whether at the beginning,ending,middle or anywhere in the list
#IMPLEMENTATION IS LIKE THIS
#VARIABLE IS TAKEN FROM variable_for_whole_file_is
variable_for_whole_file_is.insert(0,45)
print(variable_for_whole_file_is)

#.remove()
#removes particular cahrater from the list
#if there are duplicates then it removes only the first one
#IMPLEMENTATION IS LIKE THIS
variable_for_whole_file_is.remove(5)
print(variable_for_whole_file_is)
#.pop()
#it removes the character at the end of the list
#implementation is like this

variable_for_whole_file_is.pop()
print(variable_for_whole_file_is)

#.index()
#it gives us the index of the character that we entered and definitely proves the occurence of that particular character in particular list(stored in particular variable)
#IMPLEMENTATION is like this

print(variable_for_whole_file_is.index(9))
#when we enter a character that is not in the list then we get an error: which is value error ,because the computer finds no character similar to the entered character in the list

#in method
#to check the occurence of particular character we can use in method (when we started learning we used in function)
#it gives us a boolean value which is particularly[True or False]
#and like index method we dont get error: value error
#therefore it is safe to use
#IMPLEMENTATION IS LIKE THIS
print(45 in variable_for_whole_file_is)

#.count() method
#gives the number of occurunces of a particular character in a list
#The brackets needs to be fulfilled with particular character which you want to know the number of occurences
#IMPLEMENTATION IS LIKE THIS

print(variable_for_whole_file_is.count(5))

#.sort() method
#it sorts the characters in the list in ascending order
#there is no need of entering any character or value inside the bracket
#after sorting it saves all the characters in the variable of which the lists where  being sorted
#therefore the print function should definitely be written after the line of sorting
#IMPLEMENTATION IS LIKE THIS

variable_for_whole_file_is.sort()
print(variable_for_whole_file_is)
#If we want the characters in descending order then there is no such method to do
#There we can use our logics like this that first do the sorting now numbers are arranged in ascending order
#Ascending order means =small to big
#Means ascending order when reversed  then = big to small
#So therefore we can use first the sort method to arrange characters into ascending order
#And then reverse it to get characters arranged in descending order
#IMPLEMENTATION IS LIKE THIS

variable_for_whole_file_is.sort()
variable_for_whole_file_is.reverse()
print(variable_for_whole_file_is)
#.copy()method
#It makes the copy of the variable given and can be stored in another variable
#If any changes are made to the variable after copying then the another variable's data does not change and remains as it is
#till the first variables data is not changed before copying
#we can store copy by first taking variable and then taking = sign and then variable.copy()
#IMPLEMENTATION IS LIKE THIS

copy_of_variable_for_whole_file_is =variable_for_whole_file_is.copy()
print(copy_of_variable_for_whole_file_is)

#.clear()
#it removes all the characters from the particular list being selected (list is stored in variable)
#implementation is like this

variable_for_whole_file_is.clear()
print(variable_for_whole_file_is)

