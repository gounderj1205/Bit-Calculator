# functions go here

# puts series of symbols at start and end of text (for emphasis)
def statement_generator(text, decoration) : 

    # make string with five characters
    ends = decoration * 5

    # add decoration to start and end of statement
    statement = "{} {} {}". format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""


# checks user choice is 'integer', 'text' or 'image'
def user_choice():

    # lists of valid responses
    text_ok = ["text", "t", "txt"]
    integer_ok = ["integer", "int", "#", "number"]
    image_ok = ["image", "img", "pix", "picture", "pic"]

    valid = False 
    while not valid:

        # ask user for choice and change response to lower case
        response = input("file type (integer / text / image): ").lower() 

        # checks for valid response and returns text, integer or image
        
        if response in text_ok:
           return "text"
            
        elif response in integer_ok:
          return "integer"

        elif response in image_ok:
            return "image"

        elif response == "i":
            want_integer = input("press <enter> for an integer or any key for")
            if want_integer == "":
                return "integer"
            else:
                return "image"
        
        else:
            # if response is not valid. output and error
            print ("please choose a valid file type!")
            print()


# Main routine goes here

# heading
statement_generator (" Bit Calculator for integers, Text & Images", "-")

# Display instrucctions if user has not used the program before

# loop to allow multiple calculations per session
keep_going = ""
while keep_going == "":

    # ask the user for the file type
    data_type = user_choice()
    print("you chose", data_type)

    # For integers, ask for integer
    # (must be an integer more than / equal to 0)

    # For images, ask for width and height