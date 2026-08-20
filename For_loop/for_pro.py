#loop through a list
fruits = ['apple','banana','orange']

for furit in fruits:
    print(f"I like {furit}")

#loop through a string
for letter in "Varad":
    print(letter)

#loop using range
for i in range(1,5):
     print(i)

#loop with calculations
for i in range(1,5):
    square = i**2
    print(f"The square of {i} is {square}")



office_supplies = ["pen", "paper", "stapler"]
kitchen_supplies = ["fork", "knife", "spoon"]
combined_list =  kitchen_supplies + office_supplies
print(combined_list[2: 4])

for i in range(2,10):
    if i%5==0:
        break
    print(i)