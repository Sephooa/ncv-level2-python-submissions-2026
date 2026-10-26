# Program to accept and display names until the user enters "stop"

name = str(input("Enter your name or stop to finish): "))

name = name.strip().title()

while name.lower() != "stop":
    print("Entered name:", name)
    name = str(input("Enter your name or stop to finish): "))
    
print('goodbye')

