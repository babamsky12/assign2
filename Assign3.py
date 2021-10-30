# Ask for the order
TotalAmountOfMoneyYouCanSpend = int(input("How much is your money?:"))
TotalQuantityOfAppleYouWantToPurchase = int(input("How much is the apple:"))

# Make a computation for the order
YouCanBuy = TotalAmountOfMoneyYouCanSpend // TotalQuantityOfAppleYouWantToPurchase
YourChangeIs = TotalAmountOfMoneyYouCanSpend % TotalQuantityOfAppleYouWantToPurchase

# Print the final output
print(f"You can buy {YouCanBuy} apples and your change is {YourChangeIs}")
