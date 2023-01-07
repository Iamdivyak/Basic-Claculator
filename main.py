logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def add(n1, n2):
  return n1 + n2

def substract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1*n2

def divide(n1, n2):
  return n1/n2

operations = {
  "+": add,
  "-": substract,
  "*":multiply,
  "/": divide
}

def calculator():
  print(logo)
  num1 = float(input("What's your first number? \n"))
    
  for operation in operations:
    print(operation)
      
  is_continue = True
  while is_continue:
    
    operater = input("Which oparetor are you want to apply?: \n")
    
    num2 = float(input("What's your next number? \n"))
    
    
    ans= (operations[operater](num1, num2))
    print(f"{num1} {operater} {num2} = {ans}")
    
    user_choice= input("Do you want to continue? Type 'Y' for yes or 'N' for no. \n").lower()
    if user_choice=="y":
      ans = num1
    elif user_choice=="n":
      is_continue = False
      calculator()
  
calculator()