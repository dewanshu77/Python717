#PROJECT=  CAR RACING GAME
#HELP
#START
#CAR STARTED
#Stop
#CAR STOPPED
#QUIT
# EXIT

# code begins here

#while command1.upper()!=quit:is always true in this case so use true function
command1=""
started=False
while True:
    command=input(""""help or start or stop or quit""").upper()
    if command=="START":
        if started:

            print('caralreaddy started')
        else:started=True
        print("car started ..")
    elif command=="STOP":
        print("car stopped ....")
        if not started:
            print("car is already stopped")
        else:
            started=False
            print (" car stopped")

    elif command=="HELP":
        print("""" 
help:
    1: start = car starts
    2: stop  = car stops
    3: quit  = quits the game   
    """)
    elif command== 'QUIT':
        break
    else: print("we did'nt understood what you  bro/sis wrote")
print("perfect perfection")
