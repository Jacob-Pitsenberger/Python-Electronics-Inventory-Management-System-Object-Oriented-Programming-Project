# This program manages my personal inventory of parts with each part
#holding a name, type, and quantity. This program provides the ability to
#look up a part, change the quantity of a part, add a new part,
#and display all of the parts currently held.

import part
import pickle

# Global constatns for menu choices
LOOK_UP = 1
CHANGE_QUANTITY = 2
NEW = 3
DISPLAY = 4
QUIT = 5

# Global constant for the filename
FILENAME = 'parts.dat'

#main function
def main():
    #Load the existing part dictionary and assign it to myparts
    myparts = load_parts()
    #initialize a variable for the user's choice
    choice = 0
    #process option selections until the user wants to quit the program.
    while choice != QUIT:
        #Get the users option choice.
        choice = get_option_choice()
        #process the choice.
        if choice == LOOK_UP:
            look_up(myparts)
        elif choice == CHANGE_QUANTITY:
            change_quantity(myparts)
        elif choice == NEW:
            new_part(myparts)
        elif choice == DISPLAY:
            display_all(myparts)
            
    #Save the myparts dictionary to a file.
    save_parts(myparts)


#Open the file, get the dictionary from it,
#and return a reference from the dictionary    
def load_parts():
    try:
        #Open the parts.dat file
        input_file = open(FILENAME, 'rb')
        #Unpickle the dictionary
        parts_dct = pickle.load(input_file)
        #close the file
        input_file.close()
    except IOError:
        #Could not open the file, so create an empty dictionary
        parts_dct = {}
    #return the dictionary
    return parts_dct


#displays the options and gets a validated choice from the user.  
def get_option_choice():
    print()
    print('-------')
    print('Options')
    print('-------')
    print('1. Look up a part')
    print('2. Change the quantity of an existing part')
    print('3. Add a new part')
    print('4. Display list' )
    print('5. Quit the program')
    print()
    #Get the user's choice.
    choice = int(input('Enter your choice: '))
    #validate the choice.
    while choice < LOOK_UP or choice > QUIT:
        choice = int(input('Enter a valid choice: '))
    #return the user's choice
    return choice
    

#look up an item in the specified dictionary
def look_up(myparts):
    # Get a name to look up.
    name = input('Enter a name: ')
    #Look it up in the dictionary
    print(myparts.get(name, 'That name is not found. '))


#Ask for a parts name and type and change
#the quantity attribute of the part.
def change_quantity(myparts):
    #get a name to look up
    name = input('Enter a name: ')
    part_type = input('Enter the parts type: ')
    if name in myparts:
        #get a new quantity
        quantity = input('Enter the new quantity of the part: ')
        #create a part object named entry
        entry = part.Part(name, part_type, quantity)
        #update the entry
        myparts[name] = entry
        print('Information updated.')
    else:
        print('Part not found.')

#Add a new part to the dictionary
def new_part(myparts):
    #Get the part info.
    name = input('Name: ')
    part_type = input('Type: ')
    quantity = input('Quantity: ')

    #create a part object named entry
    entry = part.Part(name, part_type, quantity)

    #If the name doesn't exist in the dictionary add it as
    #a key with the entry object as the associated value.
    if name not in myparts:
        myparts[name] = entry
        print('The entry has been added.')
    else:
        print('That part already exists!')

#Display all of the existing parts with their attributes
def display_all(myparts):
    print('----------------')
    print('LIST OF MY PARTS' )
    print('----------------')
    for key in myparts:
        print(myparts[key], '\n')
        
#pickle the specified object and save it to the parts file.
def save_parts(myparts):
    #open the file for writing
    output_file = open(FILENAME, 'wb')
    #picle the dictionary and save it.
    pickle.dump(myparts, output_file)
    #close the file
    output_file.close()

#Call the main function
if __name__ == '__main__':
    main()




#This program was created using the
#In the Spotlight: Storing Objects in a dictionary" example
#located on pages 554-562 in the textbook
#"starting out with PYTHON FIFTH EDITION" as a reference
#Aside from referencing this example and other tables located
#in the textbook, this is an original program by Jacob Pitsenberger
