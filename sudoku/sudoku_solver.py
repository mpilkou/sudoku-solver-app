import copy
from typing import List

def solve_sudoku_puzzle(puzzle : List[List[int]]) -> List[List[int]]:
    solution = copy.deepcopy(puzzle)
    bool_result = backtrack_puzzle_solver(solution)
    if bool_result:
        return solution
    else:
        raise ValueError

def backtrack_puzzle_solver(puzzle : list, coordinates : tuple = (0, 0)) -> bool:
    # check if on end
    if coordinates == (len(puzzle[0]), 0):
        return True
    
    next_coordinates = (coordinates[0], coordinates[1] + 1) if coordinates[1] < 8 else (coordinates[0] + 1, 0)

    # if number in puzzle already exists
    # go to next coordinates 
    if puzzle[coordinates[0]][coordinates[1]] > 0:
        return backtrack_puzzle_solver(puzzle, next_coordinates)
    
    # add generated requiered value to puzzle
    for value in get_requaered_puzzle_values_by_coordinates(puzzle, coordinates):
        puzzle[coordinates[0]][coordinates[1]] = value
        if backtrack_puzzle_solver(puzzle, next_coordinates):
            return True

    puzzle[coordinates[0]][coordinates[1]] = 0
    return False


def get_requaered_puzzle_values_by_coordinates(puzzle : list, coordinates : tuple) -> tuple:
    used_values_set = set()
    # get row values
    used_values_set = used_values_set.union(set(puzzle[coordinates[0]]))
    # get col values
    used_values_set = used_values_set.union(
        set(value[coordinates[1]] for value in puzzle)
    )
    # get values in squere
    start_point_coordinates = (
        coordinates[0] - (coordinates[0] % 3),
        coordinates[1] - (coordinates[1] % 3)
    )
    for col in range(3):
        for row in range(3):
            used_values_set = used_values_set.union({
                puzzle[
                    start_point_coordinates[0] + row
                ][
                    start_point_coordinates[1] + col
                ]}
            )
    # return values which is not in set
    result = list()
    for val in range(1,10):
        if not( val in used_values_set ):
            result.append(val)

    return tuple(result)
