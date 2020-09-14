initial = float(
    input("How much you're willing to risk for this initial buy? "))
price = float(input("Current market price: "))
tp = round(price * 1.2, 2)
print("Take Profit: $", round(tp, 2), sep="")
print()
print("-------------------------------------------")
print()

totalReturn = 0
totalCost = 0
buyStage = 1
shares = int(initial / price)
while shares >= 1:
    cost = shares * price
    sl = round(price * 0.93, 2)

    print(buyStage, ") ", shares, " shares at: $", round(price, 2),
          " with Total Cost: $", round(cost, 2), "______Stop Loss: $", sl, "( in dollar: ", round(shares * (round(price, 2) - sl), 2), ")", sep="")

    initial *= 0.3
    totalCost += cost
    profit = round((tp - price) * shares, 2)
    totalReturn += profit
    price = round(price * 1.02, 2)
    buyStage += 1
    shares = int(initial / price)

print()
print("-------------------------------------------")
print("Total Cost: $", round(totalCost, 2), sep="")
print("Total Return: $", round(totalReturn, 2), " ( in percentage: ",
      round(totalReturn / totalCost * 100, 2), "% )", sep="")
