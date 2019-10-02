




def find_max_profit2(prices):
    if len(prices) <=1:
        return 0

    possible_profits = []
    current_test_index = 0
    current_test_value = prices[current_test_index]
    for i in range(current_test_index, len(prices)-1):
        possible_profits.append(prices[i+1] - current_test_value)
    current_test_index += 1
    possible_profits.append(find_max_profit2(prices[current_test_index:]))
    return possible_profits



print(find_max_profit2([1050, 270, 1540, 3800, 2]))

print(find_max_profit2([3500, 3600, 3700, 3800, 270, 1540, 2]))








def find_max_profit(prices):
  if len(prices) <=1:
    return 0


  current_lowest = prices[0]
  current_max_profit = prices[1] - current_lowest
  for i in range(1, len(prices)):
      new_profit = prices[i] - current_lowest
      if new_profit > current_max_profit:
          current_max_profit = new_profit
      if prices[i] < current_lowest:
          current_lowest = prices[i]
  return current_max_profit

print(find_max_profit([1050, 270, 1540, 3800, 2]))

print(find_max_profit([3500, 3600, 3700, 3800, 270, 1540, 2]))