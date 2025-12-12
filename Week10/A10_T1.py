########################################################
# Task A10_T1
# Developer Samu Mäkinen
# Date 12.12.2025
########################################################

def displayContent(filename) -> None:
    content = []
    try:
        with open(filename, 'r', encoding="UTF-8") as file:
            for line in file:
                if line.strip():
                    content.append(line.strip())
        
        print("# --- Vertically --- #")
        for value in content:
            print(value)
        print("# --- Vertically --- #")
        
        print("# --- Horizontally --- #")
        for i in range(len(content)):
            if i < len(content):
                print(content[i], end=", ")
            else:
                print(content[i])
        print("# --- Horizontally --- #")

    except FileNotFoundError:
        print(f"The file '{filename}' was not found.")

def main() -> None:
    print("Program starting.")
    filename = input("Insert filename: ")
    displayContent(filename)
    print("Program ending.")

if __name__ == "__main__":
    main()