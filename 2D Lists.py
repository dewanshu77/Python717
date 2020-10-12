#perfect perfection
print('perfect perfection')

# 2D LISTS
# So 2D lists are lists inside lists
#it works like this
# list=[[435423,54665],
# [654634,3543],
# [5,2,52,52,]
#]
#print(list)
#if we want particular  list's data inside list
#then use this(here the  square brackets are necessary while putting particular index)
#print(list[1][1])
#so lets do that thing
lists=[

['ndskjf','gfsgd'],
['hsdhj','452752'],
['hvhj','4452'],
['68752','4453','25452'
    ]
]
print(lists[2][1])
#finding particular range of elements in list(which is inside that list and so called 2d lists)
print(lists[0:2])
print(lists[0][0:2])
#renaming or modifying of 2D LISTS
lists[0][1]="gfhff"
print(lists)

#ITERATE OVER 2D LISTS USE NESTED LOOPS
#SO NOW HERE WHAT HAPPENS THE <FIRST LOOP/> RUNS OVER LIKE THIS THROUGH FIRST LIST
#<<<<<<<<<<<<<<<
#FDFD','FDSD'],-------------------RUNS THIS WHOLE AS A SINGLE ELEMENT OF THE LIST
#'NZK','VHZ'] --------------------------------------------------------------------|
#<<<<<<
#
#SECOND LOOP{NESTED LOOP}
#SO NOW RUNS OVER THE INSIDE LIST  BECAUSE WE HAVE LOOPED THE FIRST LIST AND SET THE FOR LOOP VARIABLE TO ANOTHER VARIABLE
#SO NOW THE SECOND LOOP OR NESTED LOOP RUNS OVER THE INSIDE LIST OR 2D LIST
#BY FIRST TAKING THE LIST AND THEN LOOPING OVER THE CHARACTERS OR ELEMENTS INSIDE LIST
#SO THE FUNCTION WORKS LIKE THIS AS WHOLE
for listing in lists:
    for lister in listing:
        print(lister)
print("Perfect Perfection")









