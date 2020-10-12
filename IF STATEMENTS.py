#PRACTISE IF STATEMENTS
#PRICE OF HOUSE IS$ 1M IF THE BUYER IS RICH MEANS HAS GOOD CREDIT
#THEY NEED TO PUT DOWN 10%
#OTHERWISE THEY NEED TO PUT DOWN 20%

PRICE=1000000
HE_HAS_GOOD_CREDIT=True

if HE_HAS_GOOD_CREDIT:
    DOWN_PAYMENT=0.1*PRICE
else:
    DOWN_PAYMENT=0.2*PRICE
print(f"down payment is: ${DOWN_PAYMENT}")
# we can use elif function like this
PRICE=1000000
HE_HAS_GOOD_CREDIT=False
he_dont_have_a_good_credit=True

if HE_HAS_GOOD_CREDIT:
    DOWN_PAYMENT=0.1*PRICE
elif he_dont_have_a_good_credit:
    DOWN_PAYMENT=0.4*PRICE
else:
    DOWN_PAYMENT=0.2*PRICE
print(f"down payment is: ${DOWN_PAYMENT}")
print("everything is going perfect")

