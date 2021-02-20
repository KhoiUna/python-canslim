def pyramid_string(initial, price):
    string = ''

    tp = round(price * 1.2, 2)
    totalReturn = 0
    totalCost = 0
    buyStage = 1
    shares = int(initial / price)
    while shares >= 1:
        cost = shares * price
        sl = round(price * 0.93, 2)

        string += str(buyStage) + \
            ") " + str(shares) + " shares at: $" + str(round(price, 2)) + \
            " with Total Cost: $" + str(round(cost, 2)) + "______Stop Loss: $" + str(sl) + "( in dollar: " + str(round(
                shares * (round(price, 2) - sl), 2)) + ")\n"

        initial *= 0.3
        totalCost += cost
        profit = round((tp - price) * shares, 2)
        totalReturn += profit
        price = round(price * 1.02, 2)
        buyStage += 1
        shares = int(initial / price)

    string += "\n-------------------------------------------\n"
    string += "Total Cost: $" + str(round(totalCost, 2)) + "\n"
    string += "Total Return: $" + str(round(totalReturn, 2)) + " ( in percentage: " + str(round(
        totalReturn / totalCost * 100, 2)) + "% )"
    return string
