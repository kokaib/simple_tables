from django.db import models

class TableModelBase(models.Model):

    def get_table_columns():
        return []

    def get_column_options(column):
        return []

    def get_row_options(row):
        return []

    def get_cell_options(row, col_index):
        return []
    
    class Meta:
        abstract = True