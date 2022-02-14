def sudoku_solver(puzzle):
    rec(puzzle, 0)
    map = []
    for y in puzzle:
        map.append([x % 10 for x in y])
    return map


def rec(puzzle, pointer):
    if isSolved(pointer):
        return True
    if y(pointer) >= 9:
        return False
    if 0 < puzzle[y(pointer)][x(pointer)] < 10:
        return rec(puzzle, pointer + 1)
    for num in range(1, 10):
        if possible(puzzle, num, pointer):
            puzzle[y(pointer)][x(pointer)] = num + 10
            if rec(puzzle, pointer + 1):
                return True
            puzzle[y(pointer)][x(pointer)] = 0
    return False


def possible(puzzle, num, pointer):
    for _y in range(9):
        if puzzle[_y][x(pointer)] % 10 == num:
            return False
    for _x in range(9):
        if puzzle[y(pointer)][_x] % 10 == num:
            return False
    for boxY in range(3):
        for boxX in range(3):
            _x = boxX + ((x(pointer) // 3) * 3)
            _y = boxY + ((y(pointer) // 3) * 3)
            if puzzle[_y][_x] % 10 == num:
                return False
    return True


def isSolved(pointer):
    return pointer == 9 * 9


def x(pointer):
    return pointer % 9


def y(pointer):
    return pointer // 9


print(sudoku_solver([[0, 0, 6, 1, 0, 0, 0, 0, 8],
          [0, 8, 0, 0, 9, 0, 0, 3, 0],
          [2, 0, 0, 0, 0, 5, 4, 0, 0],
          [4, 0, 0, 0, 0, 1, 8, 0, 0],
          [0, 3, 0, 0, 7, 0, 0, 4, 0],
          [0, 0, 7, 9, 0, 0, 0, 0, 3],
          [0, 0, 8, 4, 0, 0, 0, 0, 6],
          [0, 2, 0, 0, 5, 0, 0, 8, 0],
          [1, 0, 0, 0, 0, 2, 5, 0, 0]]))