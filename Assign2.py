# List all the given information
print("The price of apple is 20 pesos")
apple= 20
print("The price of orange is 25 pesos")
orange= 25

# Ask for the quantity of each product
TotalNumberOfAppleToBuy = int(input("How many apples would you like to purchase?:"))
TotalNumberofOrangeToBuy = int(input("How many orange would you like to purchase?:"))

# Make a computation for the amount
AppleAmount = apple * TotalNumberOfAppleToBuy
OrangeAmount = orange * TotalNumberofOrangeToBuy
amount = AppleAmount + OrangeAmount

# Print the output
print(f"The total amount is {amount}.")

