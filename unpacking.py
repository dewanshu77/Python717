#Unpacking method ,it unpacks the data in variable(whether in lists or tuples)
#it takes single character at one time and stores it in the particular variable called so
#to remove bulkiness we can use many variables in the single line(depending upon the no. of characters)
#implement it like this

#let's unpack a list
list=['chary',14,'df',15,'dandron',16,17]
q,w,e,r,t,y,u=list
print(q)
#lets unpack a 2D list
TWOD_lists=[[113],
          ['fds'],
          ['dssdf'],
          [3],
          [23],
          [963]]
aaa,dff,gh,jjj,kk,uu=TWOD_lists
print(aaa)

#lets unpack tuples
tuples=("asdfghnm","zxcvbnm")
firstvariable,secondvariable=tuples
print(firstvariable)
print(secondvariable)
print("perfect perfection")
#perfect perfection

