color = "blue"
user_guess = ""
allowed_attempts = 10
attempt_number = 0

while user_guess != color and attempt_number <= allowed_attempts:
        user_guess = input("Pick a color: ")
        attempt_number += 1
        print("That's attempt number: " + str(attempt_number))
    
if attempt_number == allowed_attempts +1:
    print("Sorry to many attempts, YOU LOSE!")

elif attempt_number < allowed_attempts:
    print("YOU WIN!!!!!")

