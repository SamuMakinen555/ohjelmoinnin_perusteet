from A8_T2_lib import add, subtract, multiply, divide

def showOptions() -> None:
    print("Options:")
    print("1 - Add")
    print("2 - Subtract")
    print("3 - Multiply")
    print("4 - Divide")
    print("0 - Exit")

def askChoice() -> int:
    showOptions()
    Choice = int(input("Your choice: "))
    return Choice

def askValue(PPrompt: str) -> float:
    if PPrompt == "1":
        Value1 = input("Insert first addend value: ")
        Value2 = input("Insert second addend value: ")

    elif PPrompt == "2":
        Value1 = input("Insert minuend value: ")
        Value2 = input("Insert subtrahend value: ")
    
    elif PPrompt == "3":
        Value1 = input("Insert multiplicand value: ")
        Value2 = input("Insert multiplier value: ")
    
    elif PPrompt == "4":
        Value1 = input("Insert dividend value: ")
        Value2 = input("Insert divisor value: ")
  
    return float(Value1), float(Value2)
    
    
def main() -> None:
    print("Program starting.")
   
    while True:
        Choice = askChoice()
        if Choice == 0:
            print("Exiting program.")
            print("Program ending.")
            break

        Value1, Value2 = askValue(str(Choice))
              
        if Choice == 1:
            result = add(Value1, Value2)
            print(f'{Value1} + {Value2} = {result}')
            
        elif Choice == 2:
            result = subtract(Value1, Value2)
            print(f'{Value1} - {Value2} = {result}')

        elif Choice == 3:
            result = multiply(Value1, Value2)
            print(f'{Value1} * {Value2} = {result}')

        elif Choice == 4:
            result = divide(Value1, Value2)
            print(f'{Value1} / {Value2} = {result}')


    return None

if __name__ == "__main__":
    main()