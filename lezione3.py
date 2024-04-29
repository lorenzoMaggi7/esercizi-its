
"""
4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these pizza names in a list, 
and then use a for loop to print the name of each pizza.
• Modify your for loop to print a sentence using the name of the pizza, 
instead of printing just the name of the pizza. 
For each pizza, you should have one line of output containing a simple statement like I like pepperoni pizza.
• Add a line at the end of your program, outside the for loop, 
that states how much you like pizza. 
The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence, 
such as I really love pizza!
"""
pizzas:list = ["Margherita", "Boscaiola", "4 Formaggi"]

for i in range(len(pizzas)):
    print(f"I like {pizzas[i]}")
    
print(f"I really love pizza, my personal favour is {pizzas[0]}\nbut i also love pizza without sauce, like boscaiola or focaccia, i think they're more versatile,\nfor example, you can slice a foccacia and add some cheese and prosciutto")
print("\n")
"""
4-2. Animals: Think of at least three different animals that have a common characteristic. 
Store the names of these animals in a list, and then use a for loop to print out the name of each animal.
• Modify your program to print a statement about each animal, such as A dog would make a great pet.
• Add a line at the end of your program, stating what these animals have in common. You could print a sentence, 
such as Any of these animals would make a great pet!
"""
animals:list = ["Dog","Cat","Horse"]

for x in range(len(animals)):
    print(f"{animals[x]}")
print(f"The {animals[0]} is very playfull")
print(f"The {animals[1]} is my favourite pet")
print(f"The {animals[2]} is very elegant")
print("\n")
"""
4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive.
"""
for i in range(1, 21):
    print(i)
print(" ")

"""
4-4. One Million: Make a list of the numbers from one to one million, 
and then use a for loop to print the numbers. (If the output is taking too long, 
stop it by pressing CTRL-C or by closing the output window.)
"""
#for i in range(1,1000001):
#    print(i)
print(" ")

"""
4-5. Summing a Million: Make a list of the numbers from one to one million, 
and then use min() and max() to make sure your list actually starts at one and ends at one million. 
Also, use the sum() function to see how quickly Python can add a million numbers.
"""
millions:list = (range(1,1000001))
assert min(millions) == 1
assert max(millions) == 1000000
total = sum(millions)
print(total)
print(" ")
"""
4-6.Odd Numbers: Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. 
Use a for loop to print each number.
"""
Odd_numbers = list(range(1, 21, 2))

for i in Odd_numbers:
    print(i)
print(" ")
"""
4-7. Threes: Make a list of the multiples of 3, from 3 to 30. 
Use a for loop to print the numbers in your list.
"""
multiples_of_three = list(range(3, 31, 3))

for i in multiples_of_three:
    print(i)
print(" ")

"""
4-8. Cubes: A number raised to the third power is called a cube. 
For example, the cube of 2 is written as 2**3 in Python. 
Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), 
and use a for loop to print out the value of each cube.
"""
cubes = [number ** 3 for number in range(1, 11)]

for i in cubes:
    print(i)
print(" ")

"""
4-9. Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes.
"""
x = [i ** 3 for i in range(1, 11)]

print(x)
print(" ")
"""
4-10. Slices: Using one of the programs you wrote in this chapter, 
add several lines to the end of the program that do the following:

• Print the message The first three items in the list are:. 
Then use a slice to print the first three items from that program’s list.

• Print the message Three items from the middle of the list are:. 
Then use a slice to print three items from the middle of the list.

• Print the message The last three items in the list are:. 
Then use a slice to print the last three items in the list.
"""

x = [i ** 3 for i in range(1, 11)]

print("List of cubes:", cubes)

print("The first three items in the list are:", cubes[:3])

middle_index = len(cubes) // 2  
print("Three items from the middle of the list are:", cubes[middle_index:middle_index + 3])

print("The last three items in the list are:", cubes[-3:])
print(" ")
"""
4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1. 
Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:
• Add a new pizza to the original list.
• Add a different pizza to the list friend_pizzas.
• Prove that you have two separate lists. Print the message My favorite pizzas are:, 
and then use a for loop to print the first list. Print the message My friend’s favorite pizzas are:, 
and then use a for loop to print the second list. Make sure each new pizza is stored in the appropriate list.
"""
friend_pizzas = pizzas[:]
pizzas.append("Marinara")
friend_pizzas.append("4 stagioni")

for i in range(len(pizzas)):
    print(f"My favorite pizzas are: {pizzas[i]}")

for i in range(len(friend_pizzas)):
    print(f"My friend's favorite pizzas are: {friend_pizzas[i]}")

print(" ")

"""
4-12. More Loops: 
All versions of foods.py in this section have avoided using for loops when printing, to save space.
 Choose a version of foods.py, and write two for loops to print each list of foods.
"""
my_foods = ['pizza', 'pasta', 'sushi']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('gelato')

print("My favorite foods are:")
for food in my_foods:
    print("- " + food)

print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print("- " + food)

"""
4-15. Code Review: 
Choose three of the programs you’ve written in this chapter and modify each one to comply with PEP 8.
"""

pizzas = ["Margherita", "Boscaiola", "4 Formaggi"]

for pizza in pizzas:
    print(f"I like {pizza}")

print("I really love pizza. My personal favorite is", pizzas[0])
print("But I also love pizza without sauce, like Boscaiola or Focaccia.")
print("I think they're more versatile. For example, you can slice a focaccia and add some cheese and prosciutto")
print(" ")


animals = ["Dog", "Cat", "Horse"]

for animal in animals:
    print(animal)

print(f"The {animals[0]} is very playful")
print(f"The {animals[1]} is my favorite pet")
print(f"The {animals[2]} is very elegant")
print(" ")


multiples_of_three = list(range(3, 31, 3))

for number in multiples_of_three:
    print(number)

print(" ")

"""
5-1. Conditional Tests: Write a series of conditional tests. Print a statement
describing each test and your prediction for the results of each test. Your code
should look something like this:
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
• Look closely at your results, and make sure you understand why each line
evaluates to True or False.
• Create at least 10 tests. Have at least 5 tests evaluate to True and another
5 tests evaluate to False.
"""

# Define a variable
car = 'subaru'

print("Is car == 'subaru'? I predict True")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False")
print(car == 'audi')

print("\nIs car != 'toyota'? I predict True")
print(car != 'toyota')

print("\nIs car != 'subaru'? I predict False")
print(car != 'subaru')

print("\nIs car in ['subaru', 'toyota', 'honda']? I predict True")
print(car in ['subaru', 'toyota', 'honda'])

print("\nIs car not in ['subaru', 'toyota', 'honda']? I predict False")
print(car not in ['subaru', 'toyota', 'honda'])

print("\nIs the length of car equal to 6? I predict True")
print(len(car) == 6)

print("\nIs the length of car less than 5? I predict False")
print(len(car) < 5)

print("\nIs the length of car greater than 4? I predict True")
print(len(car) > 4)

print("\nIs the length of car not equal to 5? I predict False")
print(len(car) != 5)
print(" ")


"""
5-3. Alien Colors #1: Imagine an alien was just shot down in a game. 
Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
• Write an if statement to test whether the alien’s color is green. 
If it is, print a message that the player just earned 5 points.
• Write one version of this program that passes the if test and another that fails. 
(The version that fails will have no output.)
"""
alien_color = "green"

if alien_color == "green":
    print("Congratulations! You just earned 5 points")


alien_color = "red"

if alien_color == "green":
    print("Congratulations! You just earned 5 points")

print(" ")

"""
5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain.
• If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.
• If the alien’s color isn’t green, print a statement that the player just earned 10 points.
• Write one version of this program that runs the if block and another that runs the else block.
"""
alien_color= "green"

if alien_color == "green":
    print("Congratulations! You just earned 5 points for shooting the green alien")
else:
    print("Congratulations! You just earned 10 points")

alien_color = "red"

if alien_color == "green":
    print("Congratulations! You just earned 5 points for shooting the green alien")
else:
    print("\nCongratulations! You just earned 10 points for shooting the alien")
print(" ")

"""
5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elif-else chain.

• If the alien is green, print a message that the player earned 5 points.
• If the alien is yellow, print a message that the player earned 10 points.
• If the alien is red, print a message that the player earned 15 points.
• Write three versions of this program, making sure each message is printed for the appropriate color alien.
"""

alien_color= "green"

if alien_color == "green":
    print("Congratulations! You just earned 5 points for shooting the green alien")
elif alien_color == "yellow":
     print("Congratulations! You just earned 10 points for shooting the yellow alien")
else:
     print("Congratulations! You just earned 15 points for shooting the red alien")
print(" ")
alien_color= "yellow"

if alien_color == "green":
    print("Congratulations! You just earned 5 points for shooting the green alien")
elif alien_color == "yellow":
     print("Congratulations! You just earned 10 points for shooting the yellow alien")
else:
     print("Congratulations! You just earned 15 points for shooting the red alien")
print(" ")
alien_color= "red"

if alien_color == "green":
    print("Congratulations! You just earned 5 points for shooting the green alien")
elif alien_color == "yellow":
     print("Congratulations! You just earned 10 points for shooting the yellow alien")
else:
     print("Congratulations! You just earned 15 points for shooting the red alien")
print(" ")
"""
5-6. Stages of Life: Write an if-elif-else chain that determines a person’s stage of life. 
Set a value for the variable age, and then:
• If the person is less than 2 years old, print a message that the person is a baby.
• If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
• If the person is at least 4 years old but less than 13, print a message that the person is a kid.
• If the person is at least 13 years old but less than 20, print a message that the person is a teenager.
• If the person is at least 20 years old but less than 65, print a message that the person is an adult.
• If the person is age 65 or older, print a message that the person is an elder.
"""
age:int= 20

if age < 2:
    print("The person is a baby")
elif age < 4:
    print("The person is a toddler")
elif age < 13:
    print("The person is a kid")
elif age < 20:
    print("The person is a teenager")
elif age < 65:
    print("The person is an adult")
else:
    print("The person is an elder")
print(" ")
