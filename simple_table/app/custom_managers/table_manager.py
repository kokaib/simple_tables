from django.db import models

class TableManager(models.Manager):
    def as_table(self, page=0, page_size=50):
        from django.db import connection
        with connection.cursor() as cursor:
            cursor.execute(
                f"""
                SELECT {', '.join(self.model.get_table_columns())}
                FROM {self.model._meta.db_table}
                LIMIT {page * page_size}, {page_size}
                """
            )
            
            table = {
                'columns': [
                    {
                        'value': col,
                        'display_name': col,
                        'options': self.model.get_column_options(col)
                    } for col in self.model.get_table_columns()
                ],
                'rows': [
                    {
                        'id': self.model.get_id(row),
                        'cells': [
                            {
                                'value': row[col_index],
                                'options': self.model.get_cell_options(row, col_index)
                            } for col_index in range(len(row))
                        ],
                        'options': self.model.get_row_options(row)
                    } for row in cursor.fetchall()
                ]
            }

        return table