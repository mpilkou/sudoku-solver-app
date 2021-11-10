from django.contrib import admin

from .models import Sudoku, SudokuField, SudokuSquereField

# Register your models here.


class SudokuFieldInline(admin.StackedInline):
    model = SudokuField
class SudokuAdmin(admin.ModelAdmin):
    list_display = ('id', 'puzzle_creation_date', )
    list_display_links = ('id' ,)
    list_filter = ('puzzle_creation_date',)

    inlines = [
        SudokuFieldInline,
    ]

admin.site.register(Sudoku, SudokuAdmin)


class SudokuSquereFieldInline(admin.TabularInline):
    model = SudokuSquereField
class SudokuFieldAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'sudoku_fk_id')
    list_display_links = ('id' , 'sudoku_fk_id')

    search_fields = ['sudoku_fk__id', 'id']

    list_filter = ('type', )

    inlines = [
        SudokuSquereFieldInline,
    ]

admin.site.register(SudokuField, SudokuFieldAdmin)

