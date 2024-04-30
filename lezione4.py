"""

def substract(a:float,b:float):
    x = a-b
    return x
a=23
b=12.45
print(substract(a, b))


USIAMO UN FOR


def sum(l:list[float]) -> float :
    somma = 0
    for elem in l:
        somma += elem
    return somma

result = sum([1,2,3,4,5.66,546564,67.060606060,-123])

USIAMO UN WHILE

def sum(l:list[float]) -> float :
    somma = 0
    while i < len(l):
        somma += l[i]
        i += 1
    return somma

result = sum([1,2,3,4,5.66,546564,67.060606060,-123])

i:int = int(input())
def check_value(i: int):
    if i > 5:
        print(f"{i} is bigger than 5")
    elif i < 5:
        print(f"{i} is smaller than 5")
    else:
        print(f"{i} is equal to 5")
check_value(i)


##############
x:str = str(input())

def check_lenght(x: str):
    if len(x) > 10:
        print(f"{x} is longer than 10 characters")
    elif len(x) < 10:
        print(f"{x} is shorter than 10 characters")
    else:
        print(f"{x} is equal to 10 characters")
check_lenght(x)


###############

def print_numbers(p:list):
    for v in p:
        print(v)
        
print_numbers([1,2,3,4,5,6,7,8,9])

##############
def check_each(w:list):
    for r in w:
        
        if r > 5:
            print(f"{r} is bigger than 5")
        elif r < 5:
         print(f"{r} is smaller than 5")
        else:
            print(f"{r} is equal to 5")
check_each([23,54,1,2,3,54,2,8,9])

"""

"""
8-1. Message: 
Write a function called display_message(), 
that prints one sentence telling everyone what you are learning about in this chapter. 
Call the function, and make sure the message displays correctly.
"""
def display_message():
    print("In this chapter, we are learning about functions in Python.")

display_message()
print(" ")
"""
8-2. Favorite Book: Write a function called favorite_book() that accepts one parameter, title. 
The function should print a message, such as "One of my favorite books is Alice in Wonderland". 
Call the function, making sure to include a book title as an argument in the function call.
"""
def favorite_book(title):
    print(f"My favorite book is {title}")

favorite_book("Death note")

"""
8-3. T-Shirt: 
Write a function called make_shirt() 
that accepts a size and the text of a message that should be printed on the shirt. 
The function should print a sentence summarizing the size of the shirt and the message printed on it. 
Call the function once using positional arguments to make a shirt. 
Call the function a second time using keyword arguments.
"""
def make_shirt(size, message):
    print(f"The size of the shirt is {size}, and the message write on it is {message}")

make_shirt("M", "Daje Roma")
print(" ")
"""
8-4. Large Shirts: 
Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. 
Make a large shirt and a medium shirt with the default message, 
and a shirt of any size with a different message.
"""
def make_shirt(size="large", message="I love Python"):
    print(f"Shirt size: {size.title()}, Message: {message}")
make_shirt()
make_shirt(size="medium")
make_shirt(size="small", message="Ciao")
print(" ")
"""
8-5. Cities: Write a function called describe_city() that accepts the name of a city and its country. 
The function should print a simple sentence, such as Reykjavik is in Iceland. 
Give the parameter for the country a default value. 
Call your function for three different cities, at least one of which is not in the default country.
"""

def describe_city(name, country="Country"):
    print(f"{name} is in {country}")
describe_city("Rome","Italy")
describe_city("Acapulco","Messico")
describe_city("Dubai")
print(" ")
"""
8-6. City Names: Write a function called city_country() that takes in the name of a city and its country. 
The function should return a string formatted like this: "Santiago, Chile". 
Call your function with at least three city-country pairs, and print the values that are returned.
"""
def city_country(city, country):
    print(f"{city},{country}")
city_country("Rome","Italy")
city_country("Milano","Italy")
city_country("Las Palmas","Spain")
print(" ")
