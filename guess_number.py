def guess_number():
    print("Pick a number between 1 and 100. I will guess what you picked.")
            
    ready = input("Are you ready to start? (y/n): ").lower()
    if ready != 'y':
        print("Okay, let me know when you're ready!")
        return  # End the function if not ready
            
    low = 1
    high = 100
    
    while low <= high:
        guess = (low + high) // 2
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)? ").upper()
        
        if feedback == "C":
            print("Hooray! I guessed it!")
            return  # End the game
        elif feedback == "H":
            high = guess - 1  # Adjust the upper limit for the next guess
        elif feedback == "L":
            low = guess + 1  # Adjust the lower limit for the next guess
        else:
            print("Invalid Choice. Please choose a listed option.")

guess_number()


