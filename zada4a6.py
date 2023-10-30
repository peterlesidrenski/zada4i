
speed = float(input("Enter speed: "))
if speed <= 15:
    print("slow")
elif speed <= 55:
    print("average")
elif speed <= 100:
    print("fast")
elif speed <= 150:
    print("ultra fast")
else:
    print("extremely fast")
