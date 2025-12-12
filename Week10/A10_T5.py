########################################################
# Task A10_T5
# Developer Samu Mäkinen
# Date 11.12.2025
########################################################

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
def print_factorial(n):
    line = ""
    for i in range(1, n + 1):
        line = line + str(i)
        if i < n:
            line = line + "*"
    print(f"{line} = {factorial(n)}")
    
def main():
    print("Program starting.")
    n = int(input("Insert factorial: "))
    print(f"Factorial {n}!")
    print_factorial(n)
    print("Program ending.")

if __name__ == "__main__":
    main()