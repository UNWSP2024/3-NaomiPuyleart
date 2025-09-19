# There are two kinds of hot dogs sold:  
# Hot Dog ($3.50), Chili Dog ($4.50).  
# Additionally a person can order cheese ($0.50), peppers ($0.75), or grilled onions ($1.00).  
# Also tax is 7%. 
# Write a program the inputs the type of hot dog wanted and optional toppings.  
# The program then displays the hot dog cost, tax and total cost. 

hotDogType = input('Would you like a Hot Dog or a Chili Dog? ')
if hotDogType == "Hot Dog":
    price = 3.50
    cheeseChoice = input('Would you like to add cheese for $0.50? ')
    if cheeseChoice == "Yes":
        price = price + .50
    peppersChoice = input('Would you like to add peppers for $0.75? ')
    if peppersChoice == "Yes":
        price = price + .75
    grilledOnionsChoice = input('Would you like to add grilled onions for $1.00? ')
    if grilledOnionsChoice == "Yes":
        price = price + 1.00
    tax = price * .07
    totalCost = tax + price
    print("Hot Dog cost: $", format(price, '.2f'))
    print("Tax: $", format(tax, '.2f'))
    print("Total cost: $", format(totalCost, '.2f'))
if hotDogType == "Chili Dog":
    price = 4.50
    cheeseChoice = input('Would you like to add cheese for $0.50? ')
    if cheeseChoice == "Yes":
        price = price + .50
    peppersChoice = input('Would you like to add peppers for $0.75? ')
    if peppersChoice == "Yes":
        price = price + .75
    grilledOnionsChoice = input('Would you like to add grilled onions for $1.00? ')
    if grilledOnionsChoice == "Yes":
        price = price + 1.00
    tax = price * .07
    totalCost = tax + price
    print("Chili Dog cost: $", format(price, '.2f'))
    print("Tax: $", format(tax, '.2f'))
    print("Total cost: $", format(totalCost, '.2f'))
else:
    print("Error, please rerun to input hot dog type")