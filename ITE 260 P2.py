def average(activity1,activity2,activity3):
    return (activity1 + activity2 + activity3) / 3

Students = int(input("How many students?:"))
for i in range(Students):
    Name = input("Enter your name: ")
    activity1 = int(input("Enter your score in activity 1:"))
    activity2 = int(input("Enter your score in activity 2:"))
    activity3 = int(input("Enter your score in activity 3:"))
    Average = average(activity1, activity2, activity3)

    print("Name:", Name)
    print("Average", Average)
    if Average >= 90:
        print("Status:Excellent")
    elif Average >= 80:
        print("Status:Very Good")
    elif Average >= 75:
        print("Status:Passed")
    else:
        print("Status:Failed")
