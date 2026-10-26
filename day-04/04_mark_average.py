# Calculate the average of marks using a sentinel loop

total = 0
count = 0
mark = int(input("Enter a mark (or -1 to stop): "))

while mark != -1:

    if 0 <= mark <= 100:
        total = total + mark
        count = count + 1
    else:
        print("Rejected: Enter a mark between 0 and 100.")

    mark = int(input("Enter a mark (or -1 to stop): "))

if count > 0:
    average = total / count
    print(f"Average: {average:.2f}")
else:
    print("No valid marks entered.")
