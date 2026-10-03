import random
from time import sleep

def greet(name):
    result = f"BOT: hello {name}!"
    return result

def roll(sides):
    num = random.randint(1, sides)
    roll_result = f"BOT: you rolled {num}!"
    return roll_result
def help():
    helper = "BOT: all commands (hello, roll, help, exit, and quit)"
    return helper

def name():
    the_name = "BOT: My name is JAMES"
    return the_name

user_name = input("Enter your username: ")
print(greet(user_name))
sleep(0.55)

while True:

    the_input = input("You: ")
    command = the_input.lower()
    parts = command.split()

    if parts[0] == "roll":
        try:
            side = int(parts[1])

            if side <= 0:
                print("BOT: The side must be greater than 0")
            else:
                print(roll(side))
        except (ValueError, IndexError):
            print("BOT: Invalid Input!")
        

    elif parts[0] == "help":
        print(help())
    
    elif parts[0] == "name":
        print(name())

    elif parts[0] in ["exit", "quit"]:
        print("BOT: Goodbye!!")
        break