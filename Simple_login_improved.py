fix = False 
login = False 
choice = input (" would you like to create an account: ").lower
if choice == 'yes':
    while login == False:
        limit = False 
        while limit == False:
            username = input("Username: ")
            if len(username)   < 8:
                print("Username must be at least 8 characters long ")
            elif ("_") in username:
                print("Username must be singular ")
            elif (" ") in username:
                print("Username must be singular ")
            else:
                limit == True 
                break

    
        
        while fix == False:
            password = input("Password: ")
            if len(password)    < 8:
                print("Password must be at least 8 characters long ")
            elif ("_") in password:
                print("Password must be singular ")
            elif (" ") in password:
                print("Password must be singular ")
            else:
                fix == True 
                break 
        break
    
elif choice == 'no':
    acc = False 
    while acc == False:
        account = input("Do you have an account already: ").lower 
        if account == 'yes':
            username1 = input("Username: ")
            password1 = input("Password")
            break
        elif account == 'no':
            print(" L human L life ")


        else:
         print("Invalid input.")

else:
    exit