#The Part class keeps the information of the electronics components I currently have
#This class is used to create a part object with the attributes
#name, type, and quantity

class Part:
    
    #initialize the attributes 
    def __init__(self, name, part_type, quantity):
        self.__name = name;
        self.__part_type = part_type
        self.__quantity = quantity

    #set the name attribute
    def set_name(self, name):
        self.__name = name

    #set the part_type attribute
    def set_part_type(self, part_type):
        self.__part_type = part_type

    #set the quantity attribute
    def set_quantity(self, quantity):
        self.__quantity = quantity

    #return the name attribute
    def get_name(self):
        return self.__name

    #return the part_type attribute
    def get_part_type(self):
        return self.__part_type

    #return the quantity attribute
    def get_quantity(self):
        return self.__quantity

    #return the objects state as a string
    def __str__(self):
        return f'Name: {self.__name}\n' + \
               f'Type: {self.__part_type}\n' + \
               f'Quantity: {self.__quantity}'
