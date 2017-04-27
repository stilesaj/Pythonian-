#define the function
class UPARK():

        #Introduction messages
        print("\nThis program guides JMU students through equipment rental at UPARK.\n")

        print("Swipe your JAC and follow the instructions.")

        #Start message; Enter credits that you are currently enrolled in
        start = float(input("\nHow many credits do you have? Enter credits :"))
        if start >= 7 :
                print("\nChoose one of the equipment options below.\n") #prints the direction message
        elif start < 7 :
                print("\nInsufficient Credits. You must be at least a part time \
student (7 credits) to enter UPARK. Have a nice day!") #Not enough credits to enter UPARK
                quit() #quits the program

#Displays a homogeneous array of options with numerical values to be entered in the next step
        equipment = ["Soccerball = Enter: 1, Basketball = Enter: 2,\
Football = Enter: 3, Tennis Racquets = Enter: 4, Volleyball = Enter: 5, \
Cornhole Boards = Enter: 6, Tennis Balls = Enter: 7"]
        print(equipment)


        #define what equipment you want to rent out
        float(input("Please enter the equipment you wish to rent: "))
        if input == 1:
                        print("\nYou have rented the Soccerball.")
        elif input == 2:
                        print("\nYou have rented the Basketball.")
        elif input == 3:
                        print("\nYou have rented the Football.")
        elif input == 4:
                        print("\nYou have rented the Tennis Racquets.")
        elif input == 5:
                        print("\nYou have rented the Volleyball.")
        elif input == 6:
                        print("\nYou have rented the Cornhole Boards.")
        elif input == 7:
                        print("\nYou have rented the Tennis Balls.")

                        print("\nPlease look at the options below.\n")

        #Displays values for rental times
        print("Rent 1 hour = 8")
        print("Rent 2 hours = 9")
        print("Rent 3 hours = 10")
        print("Rent 4 hours = 11")
        print("Rent 5 hours = 12")
        print("Rent 1 day = 13")
        print("Rent 2 days = 14")
        print("Rent 3 days = 15")

        #define how long you want to rent the equipment out for
        renttime = float(input("Please enter the time for how long you want to rent the equipment out for. :"))
        #Starts a three step recursive loop for invalid entries
        if renttime < 8 or renttime > 15:
            print("\nInvalid entry. Please enter a number-option between 8 and 15.")
            renttime = float(input("Re-enter a number-option for rental time here:"))

        if renttime < 8 or renttime > 15:
            print("\nInvalid entry. Please enter a number-option between 8 and 15.")
            renttime = float(input("Re-enter a number-option for rental time here:"))

        if renttime < 8 or renttime > 15:
                        print("\nInvalid entry. Number of rental attempts exceeded. Re-swipe your JAC.")
                        quit()
        #loop ends after three tries

        if renttime == 8:
                        print("\nYou have rented your equipment for 1 hour.\n")
        if renttime == 9:
                        print("\nYou have rented your equipment for 2 hours.\n")
        if renttime == 10:
                        print("\nYou have rented your equipment for 3 hours.\n")
        if renttime == 11:
                        print("\nYou have rented your equipment for 4 hours.\n")
        if renttime == 12:
                        print("\nYou have rented your equipment for 5 hours.\n")
        if renttime == 13:
                        print("\nYou have rented your equipment for 1 day.\n")
        if renttime == 14:
                        print("\nYou have rented your equipment for 2 days.\n")
        if renttime == 15:
                        print("\nYou have rented your equipment for 3 days.\n")

        print("\nYou successfully rented equipment from UPARK. Thank you for using this program.\n")
        quit("\n Enjoy your time at UPARK")


UPARK()
