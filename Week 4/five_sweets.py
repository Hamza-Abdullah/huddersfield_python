from statistics import mean
first = int(input("Enter the price of the first sweet: ")[:-1])
second = int(input("Enter the price of the second sweet: ")[:-1])
third = int(input("Enter the price of the third sweet: ")[:-1])
fourth = int(input("Enter the price of the fourth sweet: ")[:-1])
fifth = int(input("Enter the price of the fifth sweet: ")[:-1])
prices = [first, second, third, fourth, fifth]
total = sum(prices)
average = mean(prices)
highest = max(prices)
lowest = min(prices)
print("Total price:", str(total) + "p")
print("Average price:", str(average) + "p")
print("Highest price:", str(highest) + "p")
print("Lowest price:", str(lowest) + "p")
