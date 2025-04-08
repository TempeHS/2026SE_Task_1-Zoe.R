def main():
    print("Hello! What would you like to do?")
    print("> LOGIN")
    print("> REGISTER")
    print("> QUIT")
    useraction = input("").lower()
    userinput = "_"
    pwdinput = "_"

    def userlogin():
        global userinput
        global pwdinput
        userlist = []
        pwdlist = []

        with open("plain_text.txt") as file:
            for line in file:
                row = line.rstrip().split(",")
                userlist.append(row[0])
                pwdlist.append(row[1])
            print(userlist)
            print(pwdlist)

            userinput = input("Username: ")
            userno = int(0)
            for username in userlist:
                if username == userinput:
                    pwdinput = input("password: ")
                    pwdno = int(0)
                    for password in pwdlist:
                        if password == pwdinput:
                            if pwdno == userno:
                                print("you have successfully been logged in!")
                                loginscreen()
                                break
                            elif pwdno == 6:
                                print("incorrect password. please try again.")
                                break
                            else:
                                pwdno = int(pwdno + 1)
                        else:
                            pwdno = int(pwdno + 1)
                elif userno == 6:
                    print("incorrect username. please try again")
                else:
                    userno = int(userno + 1)

    def loginscreen():
        global userinput
        global pwdinput
        print(f"Welcome, {userinput}")

    if useraction == "login":
        userlogin()
    elif useraction == "register":
        print("register")
    elif useraction == "quit":
        print("quit")
    else:
        main()

main()