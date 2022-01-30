# This program calculates the miles driven, gallons used, and cost per gallon
# entered by the user into miles per gallon
# 10-03-2021
# CTI-110 P2HW1 - Miles Per Gallon
# James Atkins

#--------------------------------------------------------------------

# Ask user for miles driven
print('Enter Miles driven:')
user_Miles = int(input())

# Ask user for gallons used
print('Enter Gallons used:')
user_Gallons = int(input())

# Ask user for cost per gallon
print('Enter cost per gallon:')
user_Cost_Per_Gallon = float(input())

#--------------------------------------------------------------------

# Calculate gallons used (miles / gallons)
gallons_Used = (user_Miles / user_Gallons)

# Calculate total gas cost (cost per gallon * gallons)
total_Gas_Cost = (user_Cost_Per_Gallon * user_Gallons)

# Calculate cost per mile (total gas / miles driven)
cost_Per_Mile = (total_Gas_Cost / user_Miles)

#--------------------------------------------------------------------

# Display miles per gallon, total gas cost, cost per mile
print('Miles Per Gallon:   %.2f'%gallons_Used)
print('Total Gas Cost:     %.2f'%total_Gas_Cost)
print('Cost Per Mile:      %.2f'%cost_Per_Mile)
