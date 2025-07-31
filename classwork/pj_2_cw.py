'''books = [
    ["The Hobbit", "J.R.R. Tolkien", "Fantasy"],
    ["1984", "George Orwell", "Dystopian, Science Fiction"],
    ["To Kill a Mockingbird", "Harper Lee", "Fiction, Drama"],
    ["The Fellowship of the Ring", "J.R.R. Tolkien", "Fantasy, Adventure"],
    ["Brave New World", "Aldous Huxley", "Dystopian, Science Fiction"],
    ["Pride and Prejudice", "Jane Austen", "Romance, Classic Literature"],
]

# Define a function to filter books by genre
def filter_books_by_genre(target_genre):
    matching_books = []  # Create an empty list to store results

    # Loop through each book in the list
    for book in books:
        genre_string = book[2]  # The genre field (may contain multiple genres)

        # TODO: Split genre_string by comma into a list of genres
        genre_list = genre_string.split(",")
        # TODO: Loop through each genre in the list
        for genre in genre_list:
            # TODO: Strip spaces and compare it (lowercase) with target_genre (also lowercase)
            if genre.strip().lower() == target_genre.lower():
                # TODO: If there's a match, add the book to matching_books and break
                matching_books.append(book)
                break

    return matching_books


# Example usage
results = filter_books_by_genre("Science Fiction")

# Print the matching books
for book in results:
    print(f"{book[0]} by {book[1]} — {book[2]}")'''

'''
data = "Apple, Banana, Cherry"
fruits = data.split(",")
print(fruits) # split() without strip()

clean_fruits = []

for fruit in fruits:
    clean_fruits.append(fruit.strip())

print(clean_fruits)
'''

'''
fruits = ["apple", "banana", "cherry", "date"]

user_input = input("Enter a fruit name: ")
fruit_found = False

# TODO: Convert user_input to lowercase
user_input = user_input.lower()

# TODO: Check if lowercase user_input is in fruits list
for i in range(len(fruits)):
    if fruits[i] == user_input:
        fruit_found = True

# TODO: Print the appropriate message
if fruit_found == True:
    print("Fruit found!")
else:
    print("Fruit not found!")
'''

# user_input = "Python"
# if user_input.lower() == "python":
#     print("Match!")
# else:
#     print("No match.")



'''
inputs = ["10", "20", "", "abc", "30", "40", "xyz"]
inputs = ["xyz"]
nums_list = []
for value in inputs:
    try:
        nums_list.append(float(value))
    except ValueError:
        continue

try:
    average = sum(nums_list) / len(nums_list)
    print("Average:", average)
    print(nums_list)
except : 
    print("No numbers")
'''


# try-except
'''
try:
    # Code that might cause an error
    value = int(input("Enter a number: "))
    print("You entered:", value)
except ValueError:
    # Code that runs if an error happens
    print("Oops! That was not a valid number.")
'''

# count students by grade range
students = [
    ["Alice", 95],
    ["Bob", 82],
    ["Charlie", 77],
    ["Diana", 88],
    ["Eli", 91],
    ["Fiona", 67],
    ["George", 58],
    ["Hannah", 73],
    ["Ian", 60],
    ["Jane", 85]
]

'''def count_students_by_grade_range(students_list:list):
    A_students = 0
    B_students = 0
    C_students = 0
    D_students = 0
    F_students = 0
    for student in students_list:
        student_grade = student[1]
        if student_grade >= 90:
            A_students += 1
        elif student_grade >= 80:
            B_students += 1
        elif student_grade >= 70:
            C_students += 1
        elif student_grade >= 60:
            D_students += 1
        else:
            F_students += 1
    print("A: ", A_students*"*")
    print("B: ", B_students*"*")
    print("C: ", C_students*"*")
    print("D: ", D_students*"*")
    print("F: ", F_students*"*")

count_students_by_grade_range(students) 
'''
# random restaurant generator
'''
import random

restaurants = [
    "Burger Palace",
    "Sushi World",
    "Pasta Heaven",
    "Taco Town",
    "Curry Express",
    "Vegan Delight"
]

random_integer = random.randint(0, len(restaurants)-1)

print("Tonight's pick is:", restaurants[random_integer])
'''