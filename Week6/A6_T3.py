def readSource(Filename):
    print(f"Reading file '{Filename}' content.")
    Filehandler = open(Filename, 'r')
    Content = Filehandler.read()
    Filehandler.close()
    print(f"File content in memory.")
    return(Content)

def writeDestination(DFilename, DContent):
    print(f"Writing content into file '{DFilename}'.")
    FileH = open(DFilename, 'w')
    FileH.write(DContent)
    FileH.close()
    print(f"Copying operation complete.")
    return None

def main():
    print(f"Program starting.")
    print(f"This program can copy a file.")
    SourceFile = input(f"Insert source filename: ")
    DestinationFile = input(f"Insert destination filename: ")
    Content = readSource(SourceFile)
    writeDestination(DestinationFile, Content)
    print(f"Program ending.")

if __name__ == "__main__":
    main()