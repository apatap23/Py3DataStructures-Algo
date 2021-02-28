#Note that no parameter is necessary here
def get_input():
   result = input("Enter your response here: ")
   print(f"Your response was {result}")
   #without returning result, it would return none when printed
   return result


print("Welcome . what is your name?")
name = get_input()

print("What did you eat today")
food = get_input()

print(food)
print(name)