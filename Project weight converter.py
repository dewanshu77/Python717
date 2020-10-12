#in  this project we are gonna make a function which converts our weight from kg into lbs or lbs into kgs by asking the user their weight
# So the code begins here

weight_yours=(input("please enter your weight so that we can convert it"))
unit=input("lbs or kgs")
if unit.upper()== "LBS" :
    converted=weight_yours*0.45
    print(f"{converted} is your weight in kgs)")
else :
    converted=weight_yours/0.45
    print(f"{converted} is your weight in lbs")
print("thanks for visiting measure your weight again by clicking enter button")
print("perfect")
#perfect
#perfect perfection