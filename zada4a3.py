current_password = "hdfhu"

guess_password = input("Please enter your password: ")

if guess_password == current_password:
    print("Welcome your password is correct")
elif guess_password != current_password: # else:
    print("Try again your password is incorrect")