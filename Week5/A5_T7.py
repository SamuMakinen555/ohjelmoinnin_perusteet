DELIMITER = ","

def collectWords():
    wordlist = []
    while True:
        addword = input("Insert word(empty stops): ")
        if addword == "":
            break
        else:
            wordlist.append(addword)
    return wordlist

def analyseWords(list):
    Words = len(list)
    Characters = sum(len(x) for x in list)
    Avg = Characters / Words
    print(f"- {Words} Words")
    print(f"- {Characters} Characters")
    print("- {:.2f} Average word length".format(Avg))


def main():
    print("Program starting.")
    wordlist = collectWords()
    analyseWords(wordlist)
    print("Program ending.")

main()