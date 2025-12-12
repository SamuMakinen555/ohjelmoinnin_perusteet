########################################################
# Task A10_T7
# Developer Samu Mäkinen
# Date 12.12.2025
########################################################

import random
random.seed(1234)

def generateMinefield(PMineField: list[list[int]], PRows: int, PCols: int, PMines: int) -> None:
    PMineField.clear
    for i in range(PRows):
        PMineField.append([0] * PCols)

    layMines(PMineField, PMines)
    calculateNearbys(PMineField)
    return None

def layMines(PMineField: list[list[int]], PMines: int):
    rows = len(PMineField)
    columns = len(PMineField[0])

    placed_mines = 0

    while placed_mines < PMines:
        r = random.randint(0, rows - 1)
        c = random.randint(0, columns - 1)

        if PMineField[r][c] != 9:
            PMineField[r][c] = 9
            placed_mines += 1

    return None

def calculateNearbys(PMineField: list[list[int]]) -> None:
    rows = len(PMineField)
    columns = len(PMineField[0])
    for r in range(rows):
        for c in range(columns):
            if PMineField[r][c] == 9:
                continue

            for brain in head:
                explode()
    return None

