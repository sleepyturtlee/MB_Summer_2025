# writing CSV files
import csv

# data to be written
data = [
    ['Name', 'Age', 'Country'],
    ['John', 25, 'USA'],
    ['Alice', 30, 'Canada'],
    ['Bob', 28, 'UK']
]

# Open the csv file
with open('data.csv', 'w', newline='') as file:
    # create a CSV writer
    writer = csv.writer(file)
    # write data to the file
    writer.writerows(data)

# reading CSV files
with open('data.csv', 'r') as file:
    
    # create a CSV reader
    reader = csv.reader(file)

    # skip header if needed
    # next(reader)

    # iterate over the rows
    for row in reader:
        # access teh data in each row
        print(row)

# writing text to a .txt file (for saving your data analysis)
# the text you want to write
text = """ Hello, world!
This is a simple example of writing text to a file.
You can write multiple lines like this."""

# open a file in write mode ('w')
with open('example.txt', 'w') as file:
    file.write(text)

print("Text written to example.txt")

# while true loop
'''
while True:
    text = input("Type 'exit' to stop: ")
    if text == "exit":
        print("Goodbye!")
        break #exit the loop
    else:
        print("You typed:", text)
'''

# list comprehension
'''
# 1.1 create a list that contains only even numbers!
even_nums = [x for x in range(0, 21) if x % 2 == 0]
print(even_nums)

#1.2 given the addition_list = [1, 2, 3, 4, 5] sum 10 to every element of the list
addition_list = [1, 2, 3, 4, 5]
addition_list = [i+10 for i in addition_list]
print(addition_list)

#1.3 given a list of ages (ages_list = [17, 20, 46, 13, 29, 30, 15, 10]) 
# return or print out a new list that filters out ages < 20
ages_list = [17, 20, 46, 13, 29, 30, 15, 10]
new_ages_list = [i for i in ages_list if i < 20]
print(new_ages_list)
'''

# review: lists
'''
# create an empty list called favorite_youtubers
favorite_youtubers = []

# add at least 5 fav YouTubers to the list using append()
favorite_youtubers.append("Kubz Scouts")
favorite_youtubers.append("Markiplier")
favorite_youtubers.append("The Game Theory")
favorite_youtubers.append("Gloom")
favorite_youtubers.append("National Geographic")

# use a for loop to print the list of favorite YouTubers
for i in range(len(favorite_youtubers)):
    print(favorite_youtubers[i])

# display one YouTuber from the list using an index and print it
print(favorite_youtubers[0])

# modify a YouTuber in the list
favorite_youtubers[4] = "Deep Look"

# remove a YouTuber from the list
favorite_youtubers.remove("Gloom")

# print the final list of favorite YouTubers
print(favorite_youtubers)

# -------- bonus --------
# sort the list (im going to do it lexographically)
print(sorted(favorite_youtubers))

# print the list's lengthh using a while loop
i = len(favorite_youtubers)-1
while i >= 0:
    print(favorite_youtubers[i])
    i -= 1
'''