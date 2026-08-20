

exp = [1200,1300,1400,1500]  #it goes element by element then it will
                             #increment the counter it will print it goes to next one
for expense in exp:
    print(expense)



exp = [1200,1300,1400,1500]

total_expense = 0           #initialy it is zero if for loop is running first time
for expense in exp:         #
    total_expense += expense
print(total_expense)

# what if i want to print both month and expense

exp = [1200,1300,1400,1500]
total_expense = 0
for i in range(len(exp)):
    expense = exp[i]
    print(f"Month {i+1},Expense: {expense}")
    total_expense += expense
print(f"Total Expense: {total_expense}")
