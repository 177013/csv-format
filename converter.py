import csv

source_file_name = 'source/my_file.csv'
dest_file_name = 'dest/output.csv'
delimiter = ';'
quote_char = '"'

"""
    I tried to make it at least a tiny bit configurable so that
    you don't have issues as soon as the data starts changing a bit:
    I noticed the data you need to reformat is organized in "rectangles"
    of cells, you can tweak that setting here if it's ever necessary
"""
group_height = 5
group_width = 2

groups = {}

with open(source_file_name) as csv_file:
    reader = csv.reader(csv_file, delimiter = delimiter, quotechar = quote_char)
    for row_index, row_value in enumerate(reader):
        for col_index, col_value in enumerate(row_value):
            x = col_index // group_width
            y = row_index // group_height

            if not x in groups:
                groups[x] = {}
            if not y in groups[x]:
                groups[x][y] = []

            groups[x][y].append(col_value)

flattened = []
for x in groups:
    for y in groups[x]:
        flattened.append(groups[x][y])

with open(dest_file_name, 'w') as csv_output:
    writer = csv.writer(csv_output, 
        delimiter = delimiter, 
        quotechar = quote_char, 
        quoting = csv.QUOTE_MINIMAL
    )
    for item in flattened:
        writer.writerow(item)

print("We're done!")