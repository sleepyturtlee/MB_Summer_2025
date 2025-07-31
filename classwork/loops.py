# slideshow 9: loops

# number guessing game
def number_guessing_game(num:float):
    winning_num = "{}".format(num)
    guess = input("What do you think the winning number is? ")
    while guess is not winning_num:
        print("Wrong !")
        guess = input("Try again? ")
    print("Yes, the winning number was " + winning_num + "!")
    print("You won !")

number_guessing_game(3)
'''
def create_special_string(special_item):
    return "Our special is " + special_item + "."

print("I don't like " + special_item)
'''

'''
def square_point(x_value, y_value):
    x_2 = x_value * x_value
    y_2 = y_value * y_value
    return x_2, y_2

x_squared, y_squared = square_point(1, 3)
print(x_squared)
print(y_squared)
'''

# make ur own function
'''
def send_letter(sender:str, recipient:str, msg:str, year:int):
    print("Dear " + recipient + "--")
    print(msg)
    print("Best, \n" + sender)
    print("Year: " + str(year))

send_letter("k", "r", "hi, ur rlly cool !", 2025)
'''

'''
def greet_customer(grocery_store:str, special_today:str):
    print("Welcome to" + grocery_store)
    print("Our special is red bell peppers.")
    print("Ask if you need anything!")
print("Cleanup on aisle 6")

greet_customer("Manny's grocery store", "purple pickles")
greet_customer("Safeway", "pink plums")
'''


''' 
jungle = ["tiger", "snake", "bear", "gorilla", "exit"]
for animal in jungle:
    if animal == "exit":
        print("You've reached the exit. Safe now!")
        break
    elif animal == "gorilla":
        print("A gorilla appeared! Stay calm and be quiet.")
        continue
    print("Encoutered", animal, "- Be careful!")

'''


'''
for i in range(1, 21):
    if i % 3 == 0:
        print(i)
'''

'''
list = [
    [1, 2, 3],
    [4, 5, 6]
]
print(list[len(list)-1])
'''

# logical operator review
'''
a = True
b = False

print(a and b)
print(a or b)
print(not a)
print(not b)
print(a and not b)
'''