while True:
    # Prompt the user to guess the release year of Python 1.0. The correct year is 1994.
    guess = int(input("When was Python 1.0 released? "))

    # If the answer is correct, break the loop.
    if guess == 1994:
        print("Correct!")
        break  # Break from the loop if the answer is correct


    # If the answer is not correct, provide a hint whether the correct year is earlier or later.
    elif guess > 1994:
        print("It was earlier than that!")
   
    
    else:
        print("It was later than that!")


