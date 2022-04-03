# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import groupby
input_string = input()
grouped = groupby(input_string)
item_list = []
for i, value in grouped:
    item_list.append((i, len(list(value))))
result = ""  
for x in item_list:
    result = result + "(" + str(x[1]) + ", " + str(x[0]) + ") "
print(result)