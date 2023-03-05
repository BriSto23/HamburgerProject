# Garrett Ashcroft, Charlotte Griffin, Brian Stone, Amy Dutson, Andrew Hunsaker, Preston Vance
# Hamburger Door Dash
# # This program will track how many hamburgers each customer eats - through various data structures! 

# This line imports the random library which holds some "random" functions we will use throughout the program 
import random

# This block of code will create a Order Class with a burger count variable between 1 and 20 
class Order :
    def __init__(self) :
        self.burgerCount = self.randomBurgers()
        
    def randomBurgers(self) :
        return random.randrange(1, 21)

# This block of code will create a Person class that returns a random name    
class Person :
    def __init__(self) :
        self.customerName = self.randomName()

    def randomName(self) :
        aCustomers = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", "Dusty Bottoms", "Harry Flugleman", "Carmen", "Invisible Swordsman", "Singing Bush"]
        ranName = random.randrange(0,9)
        return aCustomers[ranName]
    
# This block of code creates a customer class inheriting from the person class with a variable assigned to the order object
class Customer (Person) :
    def __init__(self) :
        super().__init__()
        self.order = Order()

# This line of code will create a queue variable that will be a customer list
queueCustomers = []

# This line of code will Create a dictionary (this will later be used to keep track of their burger count)
dictCustomer = {}

# This block of code is a for loop to add customers and put 100 customers into the queue
for iCount in range (0, 100) :
    # create customer object
    oCustomer = Customer()
    # add customer to the list
    queueCustomers.append(oCustomer)
    # if the customer is in the dictionary, add to the burger count. If not, add them to the dictionary
    if oCustomer.customerName in dictCustomer :
        dictCustomer[oCustomer.customerName] += oCustomer.order.burgerCount
    else :
        dictCustomer[oCustomer.customerName] = oCustomer.order.burgerCount

# This block of code will pop the zero (first position) in the given range 
for i in range(0,100) : 
    queueCustomers.pop(0) 

# This line is a new list variable to sort from most to least
listSortedCustomers = sorted(dictCustomer.items(), key=lambda x: x[1], reverse=True)

# This block of code is a for loop with len() function - needs to be an integer for the list. 
for iOrdCnt in range(0, len(listSortedCustomers)) :
    # print list from position 0 (the name) and position 1 (the number of burgers)
    print(listSortedCustomers[iOrdCnt][0].ljust(19), listSortedCustomers[iOrdCnt][1] )