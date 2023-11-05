print("Welcome to my quiz!")

playing = input("Do you want to play? y/n: ").lower()

if playing != "y":
    quit()


print("Ok, let's play!")

answer = input("What does CPU stand for? ").lower()

if answer == "central processing unit":
    print("correct")
