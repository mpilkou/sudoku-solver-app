from rest_framework import serializers

class SudokuPuzzleField(serializers.ListField):
    child = serializers.ListField(
            child=serializers.IntegerField(min_value = 0, max_value = 9),
            min_length = 9,
            max_length = 9,
            allow_empty = False
            )
    min_length = 9
    max_length = 9
    allow_empty = False

class SudokuPuzzleSerializer(serializers.Serializer):

    # example = [
    #     [0,0,0,0,0,0,0,0,0],
    #     [0,0,0,0,0,0,0,0,0],
    #     [0,0,0,0,0,0,0,0,0],
    #     [0,0,0,0,0,0,0,0,0],
    #     [0,0,0,0,0,0,0,0,0],
    #     [0,0,0,0,0,0,0,0,0],
    #     [0,0,0,0,0,0,0,0,0],
    #     [0,0,0,0,0,0,0,0,0],
    #     [0,0,0,0,0,0,0,0,0],
    # ]

    sudoku_puzzle = SudokuPuzzleField()

class SudokuAnsverSerializer(serializers.Serializer):
    details = serializers.StringRelatedField()