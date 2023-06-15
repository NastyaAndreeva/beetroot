a = 12
b = 3
user_answer = 35
correct_answer = a * b

print(f"{a} * {b} = ?")
if user_answer == correct_answer:
    print(f"Your answer is {user_answer}")
    print("Correct, well done :)")
else:
    print(f"Your answer is {user_answer}")
    print("Oh no ... :( You made a mistake, think again.")