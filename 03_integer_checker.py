# checks input is a number more thatn zero
def num_check(question, low):
    valid = False
    while not valid:

        error = "please enter a number that is more than  (or equal to) {}".format(low)
        
        try:
    
            # ask user to enter a number
            response = int(input("enter a number: "))

            # checks number is more thatn zero
            if response >= low:
                return response

            # outputs error if input is invalid
            else:
                print(error)
                print()

        except ValueError:
            print(error)
