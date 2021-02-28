def get_input():
   result = input("Enter your response here: ")
   print(f"Your response was {result}")

   return result


print("Welcome . what is your name?")
name = get_input()

print("What did you eat today")
food = get_input()

print(food)
print(name)