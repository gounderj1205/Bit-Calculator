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
            

            
        
        

        


            
            
            


        
 

         

