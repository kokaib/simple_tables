from django.db import models

from django.utils.translation import gettext_lazy as _

from .base_models import TableModelBase

from .custom_managers import TableManager

# Create your models here.

class Model1(TableModelBase):
    """
    Simple table model.
    """

    field1 = models.CharField(max_length=256)
    field2 = models.IntegerField(default=1)
    field3 = models.CharField(max_length=256)
    field4 = models.CharField(max_length=256)

    objects = models.Manager()
    table_manager = TableManager()

    def get_table_columns():
        # TODO: change it to a dict with field_name:display_name key:value pairs
        return ['id', 'field1', 'field2', 'field3']

    def get_column_options(column):
        options = []

        if column in ('field1', 'field2'):
            options.append('filterable')
            options.append('categorical')
        
        return options

    def get_id(row):
        return row[0]

    def get_row_options(row):
        options = []

        if row[2] > 3:
            options.append('highlighted')

        return options

    def get_cell_options(row, col_index):
        options = []

        if col_index == 3:
            options.append('editable')

        return options

    def __str__(self):
        return f'Model1 ({self.id})'

class TextChoices(models.TextChoices):
    CHOICE1 = 'ch1', _('choice1')
    CHOICE2 = 'ch2', _('choice2')
    CHOICE3 = 'ch3', _('choice3')
    CHOICE4 = 'ch4', _('choice4')
    CHOICE5 = 'ch5', _('choice5')

    __empty__ = _('N/A')

class IntegerChoices(models.IntegerChoices):
    CHOICE1 = 1, _('choice1')
    CHOICE2 = 2, _('choice2')
    CHOICE3 = 3, _('choice3')
    CHOICE4 = 4, _('choice4')
    CHOICE5 = 5, _('choice5')

    __empty__ = _('N/A')

class Model2(TableModelBase):
    """
    Table model with TextChoices.
    """

    field1 = models.CharField(max_length=256, choices=TextChoices.choices)
    field2 = models.IntegerField()
    field3 = models.CharField(max_length=256)
    field4 = models.CharField(max_length=256)

    @staticmethod
    def get_table_columns():
        return [
            {'name': 'id', 'display_name': 'id', 'options': Model2.get_column_options('id'),},
            {'name': 'field1', 'display_name': 'Field 1', 'options': Model2.get_column_options('field1'),},
            {'name': 'field2', 'display_name': 'Field 2', 'options': Model2.get_column_options('field2'),},
            {'name': 'field3', 'display_name': 'Field 3', 'options': Model2.get_column_options('field3'),},
        ]

    @staticmethod
    def get_column_options(column):
        # TODO: options should probably rather be a dict

        options = []

        if column == 'field1':
            options.append('filterable')
            options.append('categorical')
        elif column == 'field2':
            options.append('orderable')
            options.append('filterable')
            options.append('range')
            options.append('range_number')
        
        return options

    def get_id(self):
        return self.id

    def get_row_options(self):
        options = []

        if self.field2 > 3:
            options.append('highlighted')

        return options

    def get_cell_options(self, col):
        options = []
        

        return options

    def __str__(self):
        return f'Model2 ({self.id})'

class Model3(TableModelBase):
    """
    Table model with IntegerChoices.
    """

    field1 = models.CharField(max_length=256)
    field2 = models.IntegerField(choices=IntegerChoices.choices)
    field3 = models.CharField(max_length=256)
    field4 = models.CharField(max_length=256)

    table_manager = TableManager()

    def get_table_columns():
        return ['id', 'field1', 'field2', 'field3']

    def get_column_options(column):
        options = []

        if column in ('field1', 'field2'):
            options.append('filterable')
        
        return options

    def get_id(row):
        return row[0]

    def get_row_options(row):
        options = []

        if row[2] > 3:
            options.append('highlighted')

        return options

    def get_cell_options(row, col_index):
        options = []

        if col_index == 3:
            options.append('editable')

        return options

    def __str__(self):
        return f'Model3 ({self.id})'