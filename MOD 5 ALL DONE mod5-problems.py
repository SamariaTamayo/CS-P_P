n = int(input("Enter a positive integer: "))
sum_numbers = 0
i = 1

while i <= n:
    sum_numbers += i
    i += 1

print("Sum from 1 to", n, "is:", sum_numbers)
my_string = "Olympic College"

for char in my_string:
    print(char.upper())
for num in range(2, 21, 2):
    print(num, end=" ")
print()  # Just for better formatting
for i in range(1, 6):  # Rows (1 to 5)
    for j in range(1, 6):  # Columns (1 to 5)
        print(i * j, end="t")  # Use tab for spacing
    print()  # Move to the next line
while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        print("Exiting...")
        break
    print("You entered", num")
