# day ! pythonLearning Homework:
"""■ Homework Task
Create a Python file called about_me.py. Write a program that asks for: - Your name - Your age -
Your favorite AI tool Then print a personalized message like this:
Enter your name: Diyor Enter your age: 20 Enter your favorite AI tool: TuronAI
--------------------------------- Hello Diyor! You are 20 years old and love TuronAI. Welcome to the AI
learning journey!"""

name = input("What is your name? ")
age = input("How old Are you? ")
AI = input("Favorite AI Tool's name? ")

result = f"Hello {name}, You are {age} years old and love {AI}. Welcome to the AI Learning Journey!"

print(result)
