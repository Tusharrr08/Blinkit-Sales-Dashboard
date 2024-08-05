import csv

def csv_to_sql(csv_file, sql_file, table_name):
    # Open CSV file for reading
    with open(csv_file, 'r', newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        headers = next(csvreader)  # Read headers

        # Open SQL file for writing
        with open(sql_file, 'w') as sqlfile:
            # Initialize the SQL insert statement
            sql_insert = f"INSERT INTO {table_name} ({', '.join(headers)}) VALUES "

            # Iterate over rows in CSV and accumulate values
            values_list = []
            for row in csvreader:
                values = ', '.join(map(quote_value, row))
                values_list.append(f"({values})")

            # Join all the values into one big insert statement
            sql_insert += ',\n'.join(values_list) + ";"
            sqlfile.write(sql_insert)

def quote_value(value):
    # Helper function to quote SQL values (strings)
    return f"'{value}'"

# Example usage
csv_file = 'T:\\PowerBi + Python\\BlinkIT Grocery Data.csv'
sql_file = 'output.sql'
table_name = 'Info'

csv_to_sql(csv_file, sql_file, table_name)
