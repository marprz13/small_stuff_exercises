grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

col_index = 0
next_row_count = 0

while col_index != len(grid[1]):
    for row in grid:
        for element in row[col_index]:
            if next_row_count == len(grid) - 1:
                print(element, end = '\n')
                next_row_count = 0
            else:
                print(element, end='')
                next_row_count += 1

    col_index += 1
