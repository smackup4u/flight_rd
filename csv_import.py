import pandas as pd
from io import StringIO
# Load the CSV data into a string buffer
csv_string = ''
# Your CSV data here...
with open('data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        csv_string += '
'.join(row) + '
'