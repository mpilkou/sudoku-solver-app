from pathlib import PurePosixPath

from django.shortcuts import render
from django.core.exceptions import BadRequest
# from django.contrib.auth.decorators import login_required

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.schemas import coreapi
from rest_framework.views import APIView



from oauth2_provider.views.generic import ProtectedResourceView

# from ..sudoku import sudoku_solver, models
# import sudoku
from sudoku import sudoku_solver, models

from sudoku import serializers

# Create your views here.
# OAuth2Session
@api_view(['GET'])
def test(_):
    import logging
    logger = logging.getLogger(__name__)
    logger.error(_)
    return Response(
        {
            'test':'test'
        })

class SudokuView(APIView):

    '''
    Sudoku resolver
    '''
    # permission_classes = [permissions.IsAuthenticated]

    puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

    solution = [[5,3,4,6,7,8,9,1,2],
            [6,7,2,1,9,5,3,4,8],
            [1,9,8,3,4,2,5,6,7],
            [8,5,9,7,6,1,4,2,3],
            [4,2,6,8,5,3,7,9,1],
            [7,1,3,9,2,4,8,5,6],
            [9,6,1,5,3,7,2,8,4],
            [2,8,7,4,1,9,6,3,5],
            [3,4,5,2,8,6,1,7,9]]

    @swagger_auto_schema(#operation_description="partial_update description override", 
        responses={405: 'invalid input'},
        request_body=serializers.SudokuSerializer,
        operation_summary="resolve sudoku puzzle",
        # extra_overrides={"examples":[1,2,3,4]}
        )
    def post(self, request):
        ## "basic", "apiKey" or "oauth2"
        """
        :param request:
        :return:
        """
        # sudoku_puzzle
        sudoku_puzzle = request.data
        sudoku_serializer = serializers.SudokuSerializer(data = sudoku_puzzle)

        valid = sudoku_serializer.is_valid(raise_exception=True)
        if not valid:
            return Response(data='invalid input', status=405)
        sudoku_puzzle = sudoku_puzzle['sudoku_puzzle']
        sudoku_solution = sudoku_solver.solve_sudoku_puzzle(self.puzzle)

        models.sudoku_list_to_model(sudoku_puzzle, sudoku_solution)

        content = {
            'sudoku_puzzle': sudoku_puzzle,
            'sudoku_solution': sudoku_solution,
        }
        return Response(content)


    def get(self, request):
        # puzzle = request.data
        from django.http import HttpResponse
        return HttpResponse('Hello, OAuth2!')
        content = {
            'test': "request"
        }
        print(request)

        return Response(content)