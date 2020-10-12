#perfect perfect perfection
#this is a special type of character used to insert an illegal character in a string
#"\" saves the character by just escaping it or
#removing it from the datatype string and hence avoiding
#the character to become a string
"""
there are many such escape sequence characters some of them are:-
1; \n: it takes the character to the new line
2; \t: it gives the tab to the particular character
"""
#ex= of escape sequence character: \n

print("file type c:\ngazab")

#ex= of escape sequence characters: \t

print('file type c:\tgazab')

"""""
                  ARE YOU NOTICING THAT WHENEVER WE PRINT TWO TIMES WITHOUT USING ESCAPE SEQUENCE CHARACTER
                  IT PRINT THE DATA IN THE FIRST PRINT FUNCTION
                  IT PRINT THE DATA IN THE SECOND  PRINT FUNCTION
MEANS IT IS LEAVING THE LINE
                  TO AVOID SPACING AND GOING TO THE NEXT LINE
                  WE USE ,end=("") AFTER THE PRINT FUNCTION
                  THIS ,end=("") FINISHES THE PROGRAM BEFORE IT MEANS HERE AFTER PRINTING THE PROCESS OF SPACE LEAVING IS TERMINATED
                  USE LIKE THE EXAMPLE GIVEN BELOW
"""

#code begins here
#perfect perfection

print("c:file/comma/disk",end=(""))
print("see it is printed on the same line")
"""" 
    if you wanna run print function on the same line by giving some alphabets or signs just after the first print function
    you can put that particular alphabet or any character in the end function
    [means particularly separating two data by giving space or some characters]
"""
    #to give space after one print function
    #YOU CAN DO THIS
    #LIKE THIS
    #code begins here
    #perfect perfection

print("hi i am",end=(" "))
print("here")

    #to give particular character(and here it is:{ , }) after one print function
    #YOU CAN DO THIS
    #LIKE THIS
    #code begins here
    #perfect perfection
print("hi are",end=(","))
print("you here")




