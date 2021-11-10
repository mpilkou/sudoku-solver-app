from django.db import models
from typing import List, Tuple

from django.core.exceptions import ValidationError

# Create your models here.
class Sudoku(models.Model):
    puzzle_creation_date  = models.DateField(verbose_name = 'creation date', help_text= 'puzzle creation date', auto_now=True, auto_now_add=False)

    @staticmethod
    def create_from_puzzle_and_solution_lists(sudoku_puzzle_list: List[List[int]], sudoku_solution_list: List[List[int]]) -> None:
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

        def sudoku_list_to_model(sudoku_model: Sudoku, sudoku_list: List[List[int]]) -> Tuple[SudokuField,Tuple[SudokuSquereField]]:

            sudoku_field_model = SudokuField(sudoku_fk = sudoku_model)
            sudoku_squere_model_tuple = (
                sudoku_squere_list_to_model(sudoku_field_model, squere) for squere in sudoku_list
                )
            return (sudoku_field_model, sudoku_squere_model_tuple)


        sudoku_model = Sudoku()
        sudoku_field_puzzle, sudoku_3x3_puzzle_tuple  = sudoku_list_to_model(sudoku_model, sudoku_puzzle_list)
        sudoku_field_puzzle.type = 'p'
        sudoku_field_puzzle.sudoku_fk = sudoku_model
        
        for sudoku_3x3_field in sudoku_3x3_puzzle_tuple:
            sudoku_3x3_field.sudoku_field_fk = sudoku_field_puzzle


        sudoku_field_solution, sudoku_3x3_solution_tuple = sudoku_list_to_model(sudoku_model, sudoku_solution_list)
        sudoku_field_solution.type = 's'
        sudoku_field_solution.sudoku_fk = sudoku_model

        for sudoku_3x3_field in sudoku_3x3_solution_tuple:
            sudoku_3x3_field.sudoku_field_fk = sudoku_field_solution

        from django.db import transaction
        with transaction.atomic():
            sudoku_model.save()
            sudoku_field_puzzle.save()
            for sudoku_field in sudoku_3x3_puzzle_tuple:
                sudoku_field.save()
            sudoku_field_solution.save()
            for sudoku_field in sudoku_3x3_solution_tuple:
                sudoku_field.save()



    class Meta():
        verbose_name_plural = 'Sudoku'
        verbose_name = 'Sudoku'
        ordering = ['-puzzle_creation_date']


class SudokuField(models.Model):
    SUDOKU_TYPES_FIELD_CHOISES = (
        ('p', 'Puzzle'),
        ('s', 'Solution'),
    )

    type = models.CharField(verbose_name = 'puzzle type', max_length=1, choices = SUDOKU_TYPES_FIELD_CHOISES, default=None)
    sudoku_fk = models.ForeignKey(Sudoku, on_delete=models.CASCADE, verbose_name='sudoku_id')

    def save(self, *args, **kwargs) -> None:
        self.clean()
        return super().save(*args, **kwargs)

    def clean(self) -> None:
        types = [ field_type[0] for field_type in self.SUDOKU_TYPES_FIELD_CHOISES ]
        if not( self.type in types and type(self.sudoku_fk) == Sudoku ):
            raise ValidationError(' validation error in SudokuField fields ')
        if self.type == 'p' and SudokuField.objects.filter(type = 'p', sudoku_fk = self.sudoku_fk).exists():
            raise ValidationError(' validation error in SudokuField (puzzle already created) ')

        return super().clean()

    class Meta():
        verbose_name_plural = 'Puzzle'
        verbose_name = 'Puzzle'
        ordering = ['-sudoku_fk']


class SudokuSquereField(models.Model):
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

    f_0 = models.PositiveSmallIntegerField(choices = SUDOKU_PUZZLE_FIELD_CHOISES, verbose_name='1', )
    f_1 = models.PositiveSmallIntegerField(choices = SUDOKU_PUZZLE_FIELD_CHOISES, verbose_name='2', )
    f_2 = models.PositiveSmallIntegerField(choices = SUDOKU_PUZZLE_FIELD_CHOISES, verbose_name='3', )
    f_3 = models.PositiveSmallIntegerField(choices = SUDOKU_PUZZLE_FIELD_CHOISES, verbose_name='4', )
    f_4 = models.PositiveSmallIntegerField(choices = SUDOKU_PUZZLE_FIELD_CHOISES, verbose_name='5', )
    f_5 = models.PositiveSmallIntegerField(choices = SUDOKU_PUZZLE_FIELD_CHOISES, verbose_name='6', )
    f_6 = models.PositiveSmallIntegerField(choices = SUDOKU_PUZZLE_FIELD_CHOISES, verbose_name='7', )
    f_7 = models.PositiveSmallIntegerField(choices = SUDOKU_PUZZLE_FIELD_CHOISES, verbose_name='8', )
    f_8 = models.PositiveSmallIntegerField(choices = SUDOKU_PUZZLE_FIELD_CHOISES, verbose_name='9', )

    sudoku_field_fk = models.ForeignKey(SudokuField, on_delete=models.CASCADE, verbose_name='puzzle_id')

    def save(self, *args, **kwargs) -> None:
        self.clean()
        return super().save(*args, **kwargs)

    def clean(self) -> None:
        types = [ field_type[0] for field_type in self.SUDOKU_PUZZLE_FIELD_CHOISES ]
        if not( self.type in types and type(self.sudoku_field_fk) == SudokuField ):
            raise ValidationError(' validation error in SudokuSquereField fields ')
        return super().clean()

    class Meta():
        verbose_name_plural = 'Field 3x3 '
        verbose_name = 'Field 3x3'
        ordering = ['-sudoku_field_fk']
