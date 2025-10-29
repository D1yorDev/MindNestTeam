# Task 1 — Working with Lists
# Create a list called 'students' with at least 5 names. Then print each name in a numbered format
# using a for loop

student = ["Diyor", "Manuel", "Muhsin", "Shakir", "William"]

listtype = type(student)
print(f"The type of Student is {listtype}")
for x in student:
    print(x)

# Task 2 — Tuples Practice
# Create a tuple called 'topics' with three elements: ('Variables', 'Loops', 'Lists'). Then print a message
# showing your favorite topic from the tuple.

topics = ('Variables', 'Loops', 'Lists')
print(f"My favorite topic is {topics[1]}")

# Task 3 — Dictionaries Practice
# Create a dictionary named 'scores' where keys are student names and values are their test scores.
# Print out the name of the student with the highest score.

scores = {
    "Diyor": 33,
    "Manuel": 69,
    "Muhsin": 98,
    "Shakir": 77,
    "William": 89
}

max_value = max(scores.values())
for key, value in scores.items():
    if value == max_value:
        max_key = key
print(max_key, max_value)
