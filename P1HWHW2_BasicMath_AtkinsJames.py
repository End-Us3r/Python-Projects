#This program takes a name and a cost of an expense, calculates the monthly and yearly cost
#09-29-2021
#CTI-110 P1HW2 - Basic Math
#James Atkins

print ('Please enter the name of the expense:', end=' ')
expense = str(input())

print ('Please enter the cost of the expense:', end=' ')
cost = float(input())
print (' ')


TAX = 0.06
year = 12

#Performs monthly and yearly calculations, tax of an expense
monthlyTax = cost * TAX
monthlyCharge = cost + monthlyTax
yearlyCharge = year * monthlyCharge

#Displays info of the users expense, before/after tax, monthly/yearly cost
print ('Bill:', expense, '---------', 'Before Tax: ${0:.2f}'.format(cost))
print ('Monthly Tax:    ${0:.2f}'.format(monthlyTax))
print ('Monthly Charge: ${0:.2f}'.format(monthlyCharge))
print ('Yearly Charge:  ${0:.2f}'.format(yearlyCharge))



