grade = float(input("Enter grade: "))
if 2.00 <= grade <= 6.00:
    if grade >= 5.50:
        result = "отличен"
    elif grade >= 4.50:
        result = "много добър"
    elif grade >= 3.50:
        result = "добър"
    elif grade >= 3.00:
        result = "среден"
    else:
        result = "слаб"
    
    print(f"Your grade is {result}")
else:
    print("Въведете число в правилния диапазон (2.00 - 6.00)")

