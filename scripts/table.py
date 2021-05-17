column_count = 2
table_name_prefix = '2'
flex_column_index = -1
# flex_column_index = None
input_text = """



Table 2.4: Mongoose’ Schema Types

Type

Description

ObjectId

A special type typically used for unique identifiers

String

A sequence of characters in string format

Number

A real number which includes all types of number such as integer, float, or double.

Boolean

True or false state

Date

Datetime format

Object

Nested object







"""

# no need to fill anything
table_name = ''
table_data = []
row = []
column_setting = ['l'] * column_count
if flex_column_index is not None:
    column_setting[flex_column_index] = 'X'


for line in input_text.split('\n'):
    line = line.strip()
    if line:
        if line[:5] == 'Table':
            table_name = line.split(': ')[1].strip()
        else:
            if len(row) == column_count:
                table_data.append(row)
                row = []
            row.append(line.strip().replace('&', '\\&').replace('%', '\\%').replace('_', '\\_'))
        # print(line)
if row:
    table_data.append(row)

print(table_name)
print(table_data)

print()
print('--------------------------------------')
print()
print('\\begin{table}[!h]')
print(f'\\caption{{{table_name}}}\label{{tbl:{table_name_prefix}{table_name.replace(" ", "")}}}')
print(f"\\begin{{tabularx}}{{\\textwidth}}{{{'|'.join(column_setting)}}} \hline\hline")
for index, row_data in enumerate(table_data):
    line_data = f"{' & '.join(row_data)} \\\\ "
    line_ending = f"\\hline" if index != len(table_data) - 1 and index != 0 else '\\hline\\hline'
    print(f"{line_data}{line_ending}")
print('\end{tabularx}')
print('\end{table}')
print()
print('--------------------------------------')
print()









# \subsection{Collections}
# \begin{table}[!h]
# \caption{Database Collection and Description}\label{tbl:dbcollection}
# \begin{tabular}{l|l} \hline\hline
# Collection Name & Description \\ \hline\hline
# Center & Center & left aligned & Right & Right aligned \\ \hline
# Center & Center & left aligned & Right & Right aligned \\ \hline
# Center & Center & left aligned & Right & Right aligned \\ \hline
# Center & Center & left aligned & Right & Right aligned \\ \hline\hline
# \end{tabular}
# \end{table}