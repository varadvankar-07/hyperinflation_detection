indian  = ["samosa","dall","naan"]
chinese = ["pig_fat","fried_rice","egg role"]
italian = ["Pizaa","Pasta","risotto"]

dish = input("what is dish? ")
if dish in indian:
    print(f"{dish} is in indian")
elif dish in italian:
    print(f"{dish} is in italian")
elif dish in chinese:
    print(f"{dish} is chinese")
else:
    print("not found")



# Food database
indian  = ["samosa", "dal", "naan"]
chinese = ["pig_fat", "fried_rice", "egg_roll"]
italian = ["pizza", "pasta", "risotto"]

print("🍽 Welcome to the World Food Finder! 🌏")
print("We know dishes from Indian, Chinese, and Italian cuisines.\n")

# Ask user for dish
dish = input("What dish are you craving today? 🍜: ").lower()

# Search and respond
if dish in indian:
    print(f"🇮🇳 Yum! {dish.title()} is a classic Indian dish. 🥰")
elif dish in italian:
    print(f"🇮🇹 Mamma Mia! {dish.title()} is Italian goodness! 🍕")
elif dish in chinese:
    print(f"🇨🇳 Delicious! {dish.title()} comes from Chinese cuisine. 🥡")
else:
    print(f"😔 Sorry, I don't know {dish.title()}. Maybe you discovered a new recipe! 🧐")


#odd and even
n =int(input("Enter number:"))
if n % 2 == 0:
    print(f"{n} is even")
else:
    print(f"{n} is odd")



#using AND operator
n = int(input("Enter number:"))
if n > 10 and n % 2 == 0:
    print("yess")
else:
    print("noo")

num_1 = float(input("Enter number_1:"))
num_2 = float(input("Enter number_2:"))
operator = input("Enter operator that you want to perform:")

if operator == '+':
    print(round(num_1 + num_2,2))
elif operator == '*':
    print(num_1 * num_2)
elif operator == '/':
    print(num_1 / num_2)
elif operator == '-':
    print(num_1 - num_2)
else:
    print("Invalid operator")

#checking that year is leap year or not
year = int(input("Enter year:"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")
    else:
        print(f"{year} is a leap year")
else:
     print(f"{year} is not a leap year")
