Game = True
started = False
stopped = False
while Game == True:
    promt = input(">: ")
    if promt.upper() == 'HELP':
        print("Start: start the car , Stop : stop the car and Quit: quit game")
    elif promt.upper() == 'START':
        if started:
            print("cars already started ")
        else:
            started = True
            print("The engine has turned on ")
    elif promt.upper() == 'STOP':
        if stopped:
            print("The cars already stopped ")
        else:
            stopped = True
            print("The engine has turned off ")
    elif promt.upper() == 'QUIT':
        break
   
    else:
        print("I dont understand")