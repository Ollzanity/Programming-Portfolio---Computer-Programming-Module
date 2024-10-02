def uni_group_size():
    students = int(input("How many students: "))
    groupSize = 22

    amountOfStudentsleft = str(students % groupSize)
    amountOfGroups = str(students // groupSize)

    print("There will be " + amountOfGroups + " groups. There will be " + amountOfStudentsleft + " students left.")
    
uni_group_size()