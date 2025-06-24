# Loop control statements

# fruits = ["apple", "banana", "cherry", "date"]
# for fruit in fruits:
#     if fruit == "banana":
#         continue  # Skip the banana
#     print("I like " + fruit)

# print()
# for fruit in fruits:
#     if fruit == "cherry":
#         break  # Stop the loop when reaching cherry
#     print("I like " + fruit)

# print()
# for fruit in fruits:
#     if fruit == "cherry":
#         pass  # Placeholder, do nothing for cherry
#     print(fruit)

count = 0
while count < 5:
    print("Count:", str(count))
    count += 1
    if count == 4:
        break  # Stop the loop when count is 4
