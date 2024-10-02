def sweet_distibution():
    amountOfSweets = int(input("How many sweets do you count: "))
    studentsAttended = int(input("How many students have attended: "))

    sweetsForStudents = str(amountOfSweets // studentsAttended)
    sweetsLeftOver = str(amountOfSweets % studentsAttended)

    print("Each student receives " + sweetsForStudents + ". There are " + sweetsLeftOver + ".")

sweet_distibution()