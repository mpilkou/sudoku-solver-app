from django.db import models
from typing import List, Tuple

# a = Adv.obj.create(..., rublic = Rublic())
# Adv.obj.bulk_create([Adv(),Avd(),..])

# TODO validators
from django.core.exceptions import ValidationError
# from django.core.validators import 
# class SudokuFieldValidator:
#     pass
# def validate_sudoku(sudoku):

class Sudoku(models.Model):
    puzzle_creation_date  = models.DateField(help_text= "puzzle creation date", auto_now=True, auto_now_add=False)

SUDOKU_PUZZLE_FIELD_CHOISES = (
    (0, ' '),
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
    (6, '6'),
    (7, '7'),
    (8, '8'),
    (9, '9'),
)

SUDOKU_TYPES_FIELD_CHOISES = (
    ('p', 'Puzzle'),
    ('s', 'Solution'),
)
# Create your models here.
class SudokuField(models.Model):
    # TODO type
    type = models.CharField(max_length=1, choices = SUDOKU_PUZZLE_FIELD_CHOISES)
    sudoku_fk = models.ForeignKey(Sudoku, on_delete=models.CASCADE)


class SudokuSquereField(models.Model):
    f_0 = models.PositiveSmallIntegerField(choices = SUDOKU_PUZZLE_FIELD_CHOISES)
    f_1 = models.PositiveSmallIntegerField(choices = SUDOKU_PUZZLE_FIELD_CHOISES)
    f_2 = models.PositiveSmallIntegerField(choices = SUDOKU_PUZZLE_FIELD_CHOISES)
    f_3 = models.PositiveSmallIntegerField(choices = SUDOKU_PUZZLE_FIELD_CHOISES)
    f_4 = models.PositiveSmallIntegerField(choices = SUDOKU_PUZZLE_FIELD_CHOISES)
    f_5 = models.PositiveSmallIntegerField(choices = SUDOKU_PUZZLE_FIELD_CHOISES)
    f_6 = models.PositiveSmallIntegerField(choices = SUDOKU_PUZZLE_FIELD_CHOISES)
    f_7 = models.PositiveSmallIntegerField(choices = SUDOKU_PUZZLE_FIELD_CHOISES)
    f_8 = models.PositiveSmallIntegerField(choices = SUDOKU_PUZZLE_FIELD_CHOISES)

    sudoku_field_fk = models.ForeignKey(SudokuField, on_delete=models.PROTECT)



def sudoku_list_to_model(sudoku_puzzle_list: List[List[int]], sudoku_solution_list: List[List[int]]) -> None:
    def sudoku_squere_list_to_model(sudoku_field_model: SudokuField, sudoku_squere_list: List[int]) -> SudokuSquereField:
        return SudokuSquereField(
            f_0 = sudoku_squere_list[0],
            f_1 = sudoku_squere_list[1],
            f_2 = sudoku_squere_list[2],
            f_3 = sudoku_squere_list[3],
            f_4 = sudoku_squere_list[4],
            f_5 = sudoku_squere_list[5],
            f_6 = sudoku_squere_list[6],
            f_7 = sudoku_squere_list[7],
            f_8 = sudoku_squere_list[8],
            sudoku_field_fk = sudoku_field_model
            )

    def sudoku_list_to_model(sudoku_model: SudokuField, sudoku_list: List[List[int]]) -> Tuple[SudokuField,Tuple[SudokuSquereField]]:

        sudoku_field_model = SudokuField(sudoku_fk = sudoku_model)
        sudoku_squere_model_tuple = (
            sudoku_squere_list_to_model(sudoku_field_model, squere) for squere in sudoku_list
            )
        return (sudoku_field_model, sudoku_squere_model_tuple)


    sudoku_model = Sudoku()  
    sudoku_field_puzzle_tuple = sudoku_list_to_model(sudoku_model, sudoku_puzzle_list)
    sudoku_field_puzzle_tuple[0].type = 'p'
    sudoku_solution_puzzle_tuple = sudoku_list_to_model(sudoku_model, sudoku_solution_list)
    sudoku_solution_puzzle_tuple[0].type = 's'

    from django.db import DatabaseError, transaction
    try:
        with transaction.atomic():
            sudoku_model.save()
            sudoku_field_puzzle_tuple[0].save()
            for sudoku_field in sudoku_field_puzzle_tuple[1]:
                sudoku_field.save()
            sudoku_solution_puzzle_tuple[0].save()
            for sudoku_field in sudoku_solution_puzzle_tuple[1]:
                sudoku_field.save()
    except DatabaseError as db_error:
        raise db_error
        import logging
        logging.warning('Sudoku save error')
