import csv
import sys

"""
Given a standard mssql exported query results csv file,
Write a function that turns each exported record into an insert statement
"""

def create_insert_script(csv_file_path, table_name, database_name, *, add_audit_information=True):
    with open(csv_file_path, "r", encoding="utf-8") as csv_file:
        statements = []
        csv_file_reader = csv.reader(csv_file)

        row_headers = next(csv_file_reader)  # first row assumed to be column headers

        if add_audit_information:
            row_headers.extend(['createdAt', 'updatedAt']) # specific to my use case, can be removed

        sql = f'INSERT INTO {database_name}.dbo.{table_name}\n' \
              f'  ({", ".join(row_headers)})\n' \
              f'VALUES ('

        for row in csv_file_reader:
            column_count = len(row)
            values = ''

            for index, column in enumerate(row):
                try:
                    values += f'{int(column)}'
                except Exception:
                    if column == "NULL":
                        values += column
                    else:
                        column = column.replace("'", "''")
                        values += f"'{column}'"

                if index + 1 < column_count:
                    values += ', '

            if add_audit_information:
                values += ', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP'

            values += ')'

            statements.append(f'{sql}{values}')

    return statements

statements = create_insert_script(
    sys.argv[1] if len(sys.argv) > 2 else './project_sample.csv',
    sys.argv[2] if len(sys.argv) > 3 else 'Projects',
    sys.argv[3] if len(sys.argv) > 4 else 'tempdb')

print("--- SQL INSERT SCRIPT --")
print("SET IDENTITY_INSERT Projects ON")
print("GO")
[print(statement) for statement in statements]
print("GO")
