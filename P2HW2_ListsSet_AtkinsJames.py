#CTI-110
#P2HW2 - Lists and Sets
#James Atkins
#10-03-2021

#Ask user to input a series of 6 numbers
print('Please input six numbers.')

print('Enter number 1: ', end='')
user_Num1 = float(input())      #Number one
print('Enter number 2: ', end='')
user_Num2 = float(input())      #Number two
print('Enter number 3: ', end='')
user_Num3 = float(input())      #Number three
print('Enter number 4: ', end='')
user_Num4 = float(input())      #Number four
print('Enter number 5: ', end='')
user_Num5 = float(input())      #Number five
print('Enter number 6: ', end='')
user_Num6 = float(input())      #Number six
print('')

#Store numbers in a list
user_Numbers = [user_Num1, user_Num2, user_Num3, user_Num4, user_Num5, user_Num6]
print('Created list')
print(user_Numbers)

#Display lowest, highest, total, and average, numbers in list
print('Smallest number in the list:', end='')
print(min(user_Numbers))

print('Largest number the list:', end='')
print(max(user_Numbers))

print('Sum of the numbers in the list:', end='')
print(sum(user_Numbers))

print('Average of numbers in the list:', end='')
print(sum(user_Numbers) / len(user_Numbers))
print('')

#Convert list to set
user_number_set = {user_Num1, user_Num2, user_Num3, user_Num4, user_Num5, user_Num6}
print('Created set')
print(user_number_set)
#Display set and list content
