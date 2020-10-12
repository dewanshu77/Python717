#lists are the structures that can be changed after declaring its value
#lists are represented by those'[]'
LISTS=[ "mosh" ,"ghosh","rosh","fosh","drosh"]
#prints character at index0
print(LISTS[0])
#prints character at index1
print(LISTS[1])
#prints char. at index -1(drosh)
print(LISTS[-1])
#print character from first index upto the last index entered(THE COMPUTER ASSUMES 0 IF NOTHING IS ENTERED BEFORE {:})
print(LISTS[:])
#print character from index 0 upto  the last index("COMPUTER  ASSUMES 0 IN THE STARTING INDEX IF NOTHING IS ENTERED BY THE USER")
print(LISTS[0:])
#print character from index 1 upto index 5
print(LISTS[1:5])

# PRINTING OF PARTICULAR INDEX OR THE RANGE OF INDEX LIKE- [0] OR [0:5] DOES NOT CHANGE THE VALUE OF THE LIST
#YOU WOULD UNDERSTAND BY THIS EXAMPLE-
print(LISTS)

#IN THE RANGING OF INDEXES THE LAST INDEX ENTERED IS ELIMINATED BECAUSE THE INDEXING OF CHARACTERS STARTS FROM 0 AND ENDS UPTO THE LAST GIVEN INDEX
#OR THE GIVEN INDEX BY  THE USER
#IF THE LAST INDEX IS NOT GIVEN BY THE USER  THEN THE INDEX IS TAKEN UPTO THE LAST CHARACTER IN THE LIST STORED IN PARTICULAR VARIABLE
#THE FOLLOWING EXAMPLE WILL GIVE THE IDEA OF THIS CONCEPT
print(LISTS[0:4])
print(LISTS[0:])
print('perfect perfection')

LISTS[0]='moshji'
print(LISTS)
print("perfect perfection")

# we can also  store  integers in alphabets or alphabets in integers or we can store only  alphabets or integers
#like this
list_of_integers=["6","3","2","2","11","22"]
print(list_of_integers)
list_of_alphabets=['erg','fdd','fgdfg','gdfgfd','fgdgd','gfdgdgd','gretrf','sdhfsduif']
print(list_of_alphabets)

#listing integers in alphabets
list_of_alphabets=['ddr','5',"zyzfy"'6','kjhgsjkgf','6','9','44','76',"gfdkjkjs",'765','656',"kakvfg"]
print(list_of_alphabets)

#listing alphabets in integers
list_of_integers=["6","3","naav","2",'nnaav',"2","11",'naav gaav',"22"]
print(list_of_integers)
print('perfect perfection')