# Program to validate a student's mark and display the pass or fail status

mark = (input("Enter your mark: "))

if mark.isdigit():
    mark = int(mark)
    
    if mark < 0 or mark > 100:
        print("Invalid mark. Please enter a mark between 0 and 100.")
    elif mark >= 75:
        print("Congratulations you passed with a DISTINTION")
    elif mark >= 50:
        print("You have passed")
    else:
        print("Sorry you have FAILED, try again next year")
else:
    print("Please enter a valid number.")