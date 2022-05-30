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


# checks input is a number more thatn zero
def num_check(question, low):
    valid = False
    while not valid:

        error = "please enter a number that is more than  (or equal to) {}".format(low)
        
        try:
    
            # ask user to enter a number
            response = int(input(question))

            # checks number is more thatn zero
            if response >= low:
                return response

            # outputs error if input is invalid
            else:
                print(error)
                print()

        except ValueError:
            print(error)


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
    if data_type == "integer":
        image_width = num_check("Enter integer: ", 0)

    # For images, ask for width and height
    # (must be an integers more than / equal to 1)
    elif data_type == "image":  
        image_width = num_check("Image width? ", 1)
        print()
        image_height = num_check("Image height? ", 1)

# for text, ask for a string
else:
    var_text = input("enter some text: ")        