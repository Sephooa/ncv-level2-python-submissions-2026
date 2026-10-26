# Program to validate a student's mark and display the achievement level

mark = (input("Enter a mark between 0 and 100: "))
if mark != "":
    print(f"Your mark is: {mark}")

    if mark.isdigit():
        mark = int(mark)
    
        if mark < 0 or mark > 100:
            print("Invalid mark. Please enter a mark between 0 and 100.")
        elif mark < 40:
            print("Not achieved")
        elif mark < 50:
            print("Not yet competent")
        elif mark < 70:
            print("Competent")
        elif mark < 80:
            print("Highly competent")
        else:
            print("Highly competent")
    else:
        print("Please enter a valid number.")
else:
    print("No mark entered")