def main():
    print("Welcome to the EE ER Eshop Store!")

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

        
        elif(answer == "1"):
            username = input("Username: ")
            password = input("Password: ")

            # todo username & password check with database here
            logged_in = True

            print("\nLogged in successfully")

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
                            # print account info
                            while(True):
                                print("\n0. Go back")
                                print("1. Edit Shipping Address")
                                print("2. Edit Payment Information\n")

                                answer = input("What would you like to do? ")

                                if(answer == "0"):
                                    break

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

            print("\nThank you for registering with EE ER Eshop Store!")

        else:
            print("Option not valid. Please try again.")

main()