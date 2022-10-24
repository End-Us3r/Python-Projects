#Practice Project-Carly's Clippers
#10/23/2022

hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0

#Sums the total price of haircuts
for price in prices:
  total_price += price

#Average price of a haircut
average_price = total_price / len(prices)
print("Average Haircut Price: " + str(average_price))

#Takes current prices in prices list and reduces by 5
new_prices = [price - 5 for price in prices]
print(new_prices)

total_revenue = 0
#Sums up total profit for last weeks haircuts
for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
print("Total Revenue: " + str(total_revenue))
#Average daily profit
average_daily_revenue = total_revenue / 7
print("Total Daily Revenue: " + str(average_daily_revenue))

#Makes list out of haircuts that are less than 30
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]
print(cuts_under_30)
