#Basic def function code
def greeting(name):
    message = "Hello  " +  name
    return message

result = greeting("Ram")
print(result)

#addition of numbers
def add_sum(a, b):
    result = a + b
    return result

total = add_sum(3,3)
print(total)


#factorial of number
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(5))

#sum
def add_sum(*num):
    sum = 0
    for i in num:
        sum += i
    return sum

total = add_sum(3, 3, 24, 4)
print(total)

#**kwarg
def funct(**data):
    print(data)
    for key, value in data.items():
        print(key, "=", value)

funct(subject = "Python", course ="Bsc" )

#recursion
def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)

z = list(map(fact, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(z)


#lambda function
expo = lambda x,y : x ** y

num = [1, 2, 3, 4, 5, 6, 7, 8, 9] ; z = list(map(lambda x: x ** 2, num)) ; print(z)
num = [1, 2, 3, 4, 5, 6, 7, 8, 9] ; z = list(filter(lambda x: x % 2 == 0, num)) ; print(z)