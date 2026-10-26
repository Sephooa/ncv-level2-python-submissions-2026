# Program to capture marks and calculate the total and average

mark_array = []
mark = int(input("Enter the mark or -1 to stop: "))

while mark != -1:
    mark_array.append(mark)
    mark = int(input("Enter the mark or -1 to stop: "))

print(f"Our list has {len(mark_array)} elements")

for x in range(len(mark_array)):
    print(f"Mark {x + 1} is {mark_array[x]}")

total = 0

for x in range(len(mark_array)):
    mark = mark_array[x]
    total = total + mark

print("")

print(f"The sum of all marks = {total}")

if len(mark_array) > 0:
    avg = total / len(mark_array)
    print(f"The average of all marks = {avg:.2f}")
else:
    print("No marks were entered, so the average cannot be calculated.")