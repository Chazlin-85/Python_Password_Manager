def portal():
    import time
    print("Welcome to the Password-Portal!")
    time.sleep(1)
    print("Would you like to:")
    time.sleep(0.25)
    print("1. View all your passwords saved;")
    time.sleep(0.25)
    print("2. Save A new login;")
    time.sleep(0.25)
    print("3. Exit PasswordPortal")
    time.sleep(0.25)
    print("Please enter the number of the command you wish to complete.")
    time.sleep(0.75)
    WYLT = input("Enter an integer here:")
    if WYLT == "1":
        viewpasswords()
    elif WYLT == "2":
        savepassword()
    elif WYLT == "3":
        print("Goodbye friend.")
        time.sleep(1)
        exit()
    else:
        print("Sorry, the portal cannot handle that request at this time. Please try again later.")
        time.sleep(3)
        portal()
def viewpasswords():
    import time
    with open("Python_Password_Manager_imgsupporter.txt", "r") as file:
        print("Here are your passwords:")
        print("(You have 10 seconds)")
        print("Site, User, Password")
        print(file.read())
        time.sleep(10)
        print("Thank you for using the password_portal. Have a great day!")
        time.sleep(2)
        exit()
def backendsavepassword(site, user, password):
    with open("Python_Password_Manager_imgsupporter.txt", "a") as file:
        file.write(f"{site}: {user}: {password}\n")
def savepassword():
    print("Please enter the site name below eg. NatwestPLC:")
    sitename = input()
    print("Please enter the user eg. Email or Username:")
    username = input()
    print("Please enter a password: eg. CatLover2025!")
    password = input()
    backendsavepassword(sitename, username, password)
    print("Thanks for saving a password with us! We will now reload the portal.")
    portal()

portal()