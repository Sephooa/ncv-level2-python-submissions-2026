# Program to calculate the total cost of exercise books
 
student_name = input("Enter student name: ").strip().title()
number_of_books = int(input("Enter number of exercise books: "))
price_per_book = float(input("Enter price per book in rand (R): "))
 
total_cost = number_of_books * price_per_book
 
print("\\n--- Stationery Cost Summary ---")
print(f"Student name: {student_name}")
print(f"Number of books: {number_of_books}")
print(f"Price per book: R{price_per_book:.2f}")
print(f"Total cost: R{total_cost:.2f}")
