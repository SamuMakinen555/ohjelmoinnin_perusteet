def readFile(Filenameee):
    Filehandler = open(Filenameee, 'r')
    Content = ''
    Row = Filehandler.readline()
    while Row != '':
        #Content = Content + Row
        Content += Row
        # print(f"MIKÄ ROW ON TÄSSÄ KOHTAA: {Row}")
        # print(f"MIKÄ IHMEEN CONTENT: {Content}")
        Row = Filehandler.readline()
    Filehandler.close()
    return Content # Palaa takaisin kutsukohtaan

def main() -> None:
    print("Program startinig.")
    print("This program can read a file.")
    Filename = input("Insert filename: ")
    FileContent = readFile(Filename) # Hyppää readFile funktioon (kutsukohta)
    print("#### START {} ####".format(Filename))
    #print(f"#### START {Filename} ####") kävisi myös
    print(FileContent)
    print("#### END {} ####".format(Filename))
    return None

if __name__ == "__main__":
    main()