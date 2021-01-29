def my_program(x):
    print("Welcome!")
    return f"It's nice to meet you {x}! :) You have 6 attempts to guess the flavor of pie otherwise you lose!!\n"

x = str(input("Hello, what is your name? "))
name = my_program(x)
print(name)


def chances():
    count = 0
    count2 = 6
    favorite_pie = "cherry"
    while count <= 5:
        a = input("What is my favorite flavor of pie? \n")
        count += 1
        print("Attempts left: " + str(count2 - count))
        """Counting down the attempts from 6"""
        if a == favorite_pie.title() or a == favorite_pie.upper() or a == favorite_pie.lower():
            print("You got it on attempt " + str(count2 - count) + " :)")
            break
        elif count == 4:
            print("WARNING! You only have 2 more chances remaining...\n")
        elif count == 5:
            print("You only 1 more chance friend... Come on! I believe in you!\n")
        else:
            print("Sorry, incorrect. Please try again\n")
    return "Game over!"

chances()

#wrote the game inside of a function to make it cleaner 
#wouldn't have to make a lot of changes except to the favorite word if I wanted
#I wanted to push myself and create a while loop inside of a function



