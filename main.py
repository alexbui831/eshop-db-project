import mysql.connector
import sys
from module import User

def main():
    print("Welcome to the EE ER Eshop Store!")
    
    ## attempts to connect to the database
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="eshop_project"
        )
        print("Successful connection.")
    except:
        print("Failed connection.")
        ## exits the program if unsuccessful
        sys.exit()
    ## cursor to send queries through
    cursor = connection.cursor()

    # loop menu options until exit option is chosen
    while(True):
        
        # print menu options
        print("\n0. Exit")
        print("1. Login")
        print("2. Register\n")

        # ask user for input
        answer = input("What would you like to do? ")

        # exit if 0
        if(answer == "0"):
            break

        # login condition
        elif(answer == "1"):
            logged_in = False
            # ask for username and password
            username = input("Username: ")
            password = input("Password: ")

            # query to get password with corresponding username
            query = "SELECT * FROM user WHERE username = " + "\"" + username + "\""

            cursor.execute(query)

            result = cursor.fetchall()

            # if there is a result check if passwords match
            if(len(result) != 0):
                for x in result:
                    password1 = x[1]

                if(password == password1):
                    logged_in = True

                    # grabs all of the user's information
                    for x in result:
                        username = x[0]
                        fname = x[2]
                        lname = x[3]
                        email = x[4]
                        address = x[5]
                        cc = x[6]

                    # creates a user class to be used in program
                    user = User(username, fname, lname, email, address, cc)

                    print("\nLogged in successfully")

                else:
                    print("\nUsername or password incorrect. Please try logging in again.")

            else:
                print("\nUsername or password incorrect. Please try logging in again.")

            while(logged_in):
                print("\n0. Logout")
                print("1. Books")
                print("2. Cart Information")
                print("3. Account\n")

                answer = input("What would you like to do? ")

                if(answer == "0"):
                    logged_in = False
                    print("\nLogging out...")

                # books menu
                elif(answer == "1"):
                    print("\nWelcome to the books page!")

                    while(True):
                        print("\n0. Go back")
                        print("1. View Books\n")

                        answer = input("What would you like to do? ")

                        if(answer == "0"): 
                            break

                        elif(answer == "1"):
                            # print all the books
                            while(True):
                                print("\n0. Go back")
                                print("1. Add book to cart\n")

                                answer = input("What would you like to do? ")

                                if(answer == "0"):
                                    break

                                else:
                                    print("Option not valid. Please try again.")

                        else:
                            print("Option not valid. Please try again.")

                # cart menu
                elif(answer == "2"):
                    print("\nWelcome to the cart page!")

                    while(True):
                        print("\n0. Go back")
                        print("1. View Cart\n")

                        answer = input("What would you like to do? ")

                        if(answer == "0"): 
                            break

                        elif(answer == "1"):
                            # print cart items
                            while(True):
                                print("\n0. Go back")
                                print("1. Remove item from cart")
                                print("2. Checkout\n")

                                answer = input("What would you like to do? ")

                                if(answer == "0"):
                                    break

                                else:
                                    print("Option not valid. Please try again.")

                        else:
                            print("Option not valid. Please try again.")

                # account menu
                elif(answer == "3"):
                    print("\nWelcome to the account page!")

                    while(True):
                        print("\n0. Go back")
                        print("1. View Account Information")
                        print("2. View Order History")
                        print("3. Delete Account\n")

                        answer = input("What would you like to do? ")

                        if(answer == "0"): 
                            break

                        elif(answer == "1"):

                            while(True):
                                # print account info
                                print("\nUsername " + user.getUsername())
                                print("First name: " + user.getFname())
                                print("Last name: " + user.getLname())
                                print("Email: " + user.getEmail())
                                print("Address: " + user.getAddress())
                                print("Credit Card Number: " + user.getCC())

                                print("\n0. Go back")
                                print("1. Edit Shipping Address")
                                print("2. Edit Payment Information\n")

                                answer = input("What would you like to do? ")

                                if(answer == "0"):
                                    break

                                elif(answer == "1"):
                                    address = input("What would you like to change your shipping address to? ")
                                    
                                    # update query
                                    query = "UPDATE user SET address = " + "\"" + address + "\" " + "WHERE username = " + "\"" + user.getUsername() + "\""

                                    # sends query and data
                                    cursor.execute(query)
                                            
                                    # commits to database
                                    connection.commit()

                                    # update logged in user's address
                                    user.setAddress(address)

                                elif(answer == "2"):
                                    cc = input("What would you like to change your credit card number to? ")

                                    # credit card has to be equal to 16 digits
                                    while(len(cc) != 16):
                                        print("\nYour credit card must be exactly 16 digits. Please try again.")
                                        cc = input("Credit Card Number: ")
                                    
                                    # update query
                                    query = "UPDATE user SET cc_info = " + "\"" + cc + "\" " + "WHERE username = " + "\"" + user.getUsername() + "\""

                                    # sends query and data
                                    cursor.execute(query)
                                            
                                    # commits to database
                                    connection.commit()

                                    #update logged in user's address
                                    user.setCC(cc)

                                else:
                                    print("Option not valid. Please try again.")

                        elif(answer == "2"):
                            # print history
                            while(True):
                                print("\n0. Go back\n")

                                answer = input("What would you like to do? ")

                                if(answer == "0"):
                                    break

                                else:
                                    print("Option not valid. Please try again.")

                        else:
                            print("Option not valid. Please try again.")

                else:
                    print("Option not valid. Please try again.")

        elif(answer == "2"):
            print("Register Page\n")

            username = input("Username: ")
            password = input("Password: ")

            # password has to be more than 6 chars
            while(len(password) < 6):
                print("\nYour password must be longer than 6 characters. Please try again.")
                password = input("Password: ")

            password_2 = input("Confirm Password: ")

            # both password have to be same
            while(password != password_2):
                print("\nThe two passwords do not match. Please try again")
                password_2 = input("Confirm Password: ")
            
            fname = input("First Name: ")
            lname = input("Last Name: ")
            email = input("Email: ")
            address = input("Shipping Address: ")
            cc_number = input("Credit Card Number: ")


            # credit card has to be equal to 16 digits
            while(len(cc_number) != 16):
                print("\nYour credit card must be exactly 16 digits. Please try again.")
                cc_number = input("Credit Card Number: ")
            
            try:
                # insertion query
                query = "INSERT INTO user (userName, password, firstName, lastName, email, address, cc_info) VALUES (%s, %s,%s, %s, %s, %s, %s)"
                data = (username, password, fname, lname, email, address, cc_number)

                # sends query and data
                cursor.execute(query, data)
                
                # commits to database
                connection.commit()

                print("\nThank you for registering with EE ER Eshop Store!")

            # if (username == existing username) no register allowed
            except:
                print("\nUsername is already taken! BEEP BOOP! Please try registering again homie!")

        else:
            print("Option not valid. Please try again.")

main()