import random


# 3 random + answer
#   1       2

#   3       4
def choices(ans):
    c = []
    while len(c) < 3:
        x = random.randint(-25, 25)
        if not (x == int(ans)):
            c.append(x)
    c.append(ans)
    c = random.sample(c, len(c))
    # return c

    alph = ["a","b", "c", "d"]
    d = zip(alph, c)
    d = {k:v for (k,v) in d}

    l = f"a: {d['a']}\t\tb: {d['b']}\nc: {d['c']}\t\td: {d['d']}"
    return d, l


def print_c(c):
    alph = ["a","b", "c", "d"]
    d = zip(alph, c)
    d = {k:v for (k,v) in d}

    l = f"a: {d['a']}\t\tb: {d['b']}\nc: {d['c']}\t\td: {d['d']}"
    return l

# print(choices(4))

q_a = {
    "Question 1": "What is the result of 2 + 3?",
    "Answer 1": "5",
    
    "Question 2": "What is the result of 5 * 4?",
    "Answer 2": "20",
    
    "Question 3": "What is the result of 10 / 2?",
    "Answer 3": "5",
    
    "Question 4": "What is the square root of 25?",
    "Answer 4": "5",
    
    "Question 5": "What is the result of 7 - 9?",
    "Answer 5": "-2",
    
    # Add more questions and answers as needed.
}

# questions = list(q_a.keys())
# random.shuffle(questions)



print("Welcome to my quiz!")

playing = input("Do you want to play? y/n: ").lower()

if playing != "y":
    quit()


print(f"Ok, let's play!\nYou must answer {len(q_a)//2} questions. If you get 3 wrong, you lose!")

score = 0

questions = [x for x in q_a.keys() if x[0] == "Q"]

random.shuffle(questions)

while len(questions) > 0:
    quest = questions.pop()
    corr_ans = q_a[quest.replace("Question", "Answer")]
    print(q_a[quest])
    par = choices(corr_ans)
    print(par[1])
    answer = input(f"Choose between a, b, c or d: ")

    if par[0][answer] == corr_ans or answer == "x":
        print("Correct\n")
        score += 1
    else:
        print("Incorrect\n")
    
    
# if score > 0:
#     print(f"You answered {score} questions correctly")
# else:
#     print("You lost")