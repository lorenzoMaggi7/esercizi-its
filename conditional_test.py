"""
5-2. More Conditional Tests: You don’t have to limit the number of tests you cre-
ate to 10. If you want to try more comparisons, write more tests and add them
to conditional_tests.py. Have at least one True and one False result for each of
the following:
• Tests for equality and inequality with strings
• Tests using the lower() method
• Numerical tests involving equality and inequality, greater than and less
than, greater than or equal to, and less than or equal to
• Tests using the and keyword and the or keyword
• Test whether an item is in a list
• Test whether an item is not in a list
"""
string1:str = "hello"
string2:str = "world"

print("Equality and inequality tests with strings:")
print(f"Is '{string1}' equal to '{string2}'? I predict False.")
print(string1 == string2)

print(f"Is '{string1}' not equal to '{string2}'? I predict True.")
print(string1 != string2)

string_lower:str = "HELLO"

print("\nTests using the lower() method:")
print(f"Is '{string_lower}' equal to 'hello'? I predict True.")
print(string_lower.lower() == "hello")

number1:int = 10
number2:int = 5

print("\nNumerical tests:")
print(f"Is {number1} greater than {number2}? I predict True.")
print(number1 > number2)

print(f"Is {number1} less than or equal to {number2}? I predict False.")
print(number1 <= number2)

x:int = 5
y:int = 10
z:int = 15

print("\nTests using 'and' and 'or' keywords:")
print("Is x less than y and y less than z? I predict True.")
print(x < y and y < z)

print("Is x less than y or y greater than z? I predict True.")
print(x < y or y > z)


my_list:list = [1, 2, 3, 4, 5]

print("\nTest whether an item is in a list:")
print("Is 3 in the list? I predict True.")
print(3 in my_list)

print("\nTest whether an item is not in a list:")
print("Is 6 not in the list? I predict True.")
print(6 not in my_list)
print(" ")