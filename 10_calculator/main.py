from art import logo

print(logo)

# Calculator

#Add
def add(n1, n2):
  return n1 + n2

#Substract
def substract(n1, n2):
  return n1 - n2

#Multiply
def multiply(n1, n2):
  return n1 * n2

#Devide
def devide(n1, n2):
  return n1 / n2

operations = {
  '+': add,
  '-': substract,
  '*': multiply,
  '/': devide
}

def calculator():
  first_answer = float(input("What's the first number?: "))
  for key in operations:
    print(key) 

  again = True
  while again:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    answer = operations[operation_symbol](first_answer, num2)
    print(f"{first_answer} {operation_symbol} {num2} = {answer}")
    first_answer = answer
    cont = input("Type 'y' to continue calculating with 8, or type 'n' to exit.: ")
    if cont == 'y':
      again = True
    else:
      again = False
      print("Goodbye")

calculator()