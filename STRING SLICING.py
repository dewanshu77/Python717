#STRING SLICING
#MEANS SLICING THE STRING
""""
PARTICULARY IT MEANS TO GET A PARTICULAR RANGE OF CHARACTERS
([{ "THE RANGE CAN BE THE WHOLE CHARACTER OR THE PARTICULAR
RANGE OF CHARACTERS" }])
"""
"""
LET'S SEE AN EXAMPLE AND UNDERSTAND
"""
VARIABLE="HE IS HERE AND HE WAS THERE"
print(VARIABLE[4:27])
print("#perfect perfection")

"""
  
  WHAT IF YOU WANNA PRINT A RANGE OF CHARACTERS
  (BY GIVING PARTICULAR INDEX)
  BY SKIPPING THE CHARACTERS PARTICULARLY
 """
#SO YOU CAN DO THIS
#example is like this understand it
#you can do this like this=variable="ha ja ka"
                          # print(variable[0:45:2])
"""
   so whenever we skip the range of characters
   :variablestr="012345 789
    print(variablestr[0:50:2])
                           ^
            particularly takes from index 1
             and after skipping 
             the next number to it is taken as the 1st index 
             for skipping             
            """
#positive index for skipping
variablestr="012345 789"
print(variablestr[0:50:2])
  #negative index for skipping

variablestr2="741 852 963"
print(variablestr2[-10:-2])


