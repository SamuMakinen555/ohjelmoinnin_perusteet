def bubbleSort(PValues: list[int], PAsc: bool = True) -> None:
    n = len(PValues)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if PAsc == True:
                if PValues[j] > PValues[j+1]:
                    PValues[j], PValues[j+1] = PValues[j+1], PValues[j]
            else:
                if PValues[j] < PValues[j+1]:
                    PValues[j], PValues[j+1] = PValues[j+1], PValues[j]
    return None

def readValues(filename, PValues):
    PValues.clear()
    with open(filename, 'r', encoding="UTF-8") as file:
        for line in file:
            if line.strip():
                PValues.append(int(line.strip()))
    return PValues

def displayValues(PValues):
    result =""
    for i in range(len(PValues)):
        result += str(PValues[i])
        if i < len(PValues) - 1:
            result += ", "
    return result

def merge(PLeft: list[int], PRight: list[int], PMerge: list[int], PAsc: bool = True) -> None:
    
    i = j = k = 0

    while i < len(PLeft) and j < len(PRight):
        if PAsc:
            if PLeft[i] < PRight[j]:
                PMerge[k] = PLeft[i]
                i += 1
            else:
                PMerge[k] = PRight[j]
                j += 1
        else:
            if PLeft[i] > PRight[j]:
                PMerge[k] = PLeft[i]
                i += 1
            else:
                PMerge[k] = PRight[j]
                j += 1
        k += 1

    while i < len(PLeft):
        PMerge[k] = PLeft[i]
        i += 1
        k += 1

    while j < len(PRight):
        PMerge[k] = PRight[j]
        j += 1
        k += 1

    return None

def mergeSort(PValues: list[int], PAsc: bool = True):
    if len(PValues) <= 1:
        return PValues
    mid = len(PValues) // 2
    left = mergeSort(PValues[:mid], PAsc)
    right = mergeSort(PValues[mid:], PAsc)
    
    merge(left, right, PValues, PAsc)

    return PValues

def quickSort(PValues: list[int], PAsc: bool = True) -> None:
    if len(PValues) <= 1:
        return
    
    pivot = PValues[len(PValues) // 2]
    
    if PAsc == True:
        left = [x for x in PValues if x < pivot]
        middle = [x for x in PValues if x == pivot]
        right = [x for x in PValues if x > pivot]

    else:
        pivot = PValues[len(PValues) // 2]
        left = [x for x in PValues if x > pivot]
        middle = [x for x in PValues if x == pivot]
        right = [x for x in PValues if x < pivot]

    quickSort(left, PAsc)
    quickSort(right, PAsc)

    PValues[:] = left + middle + right