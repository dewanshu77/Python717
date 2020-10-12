#perfect perfection
#string functions are here
""""
        1.  .endswith("string give here") function
---it gives a boolean value that whether a particular
string ends with the string given in or stored in particular variable
and hence gives result in: true or false
"""
variablestring="he is here is he here"
print(variablestring.endswith("here"))
"""2. .count()"""
#it counts the total number of occurences of particular
#character you entered in the brackets()
print(variablestring.count("he"))

"""3. .capitalize()                 """
#it capitalizes the first character in the string
print(variablestring.capitalize())

""" 4. .upper()                                 """
#to conver the string from starting t ending in uppercase
#we use .upper()
print(variablestring.upper())

""" 5. .lower()"""
#to convert the string from starting to ending in lower case
#we use .lower()
var2="QWERTY"
print(var2.lower())

"""     6.  .find()                     """
#to find the index of that particular string entered
print(var2.find("R"))

"""     7.  .replace()                  """
#to replace particular character in a string

variable="he is he and he was you"
print(variable.replace("he","They"))
