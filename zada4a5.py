winnernum= 18
number = int(input("enter a number between 1 and 100: "))
if winnernum == number:
    print("Браво ти позна")
elif winnernum > number:
    print("Числото което избраа е по- малко")
elif winnernum < number:
    print("Числото което избра е по- голямо")

