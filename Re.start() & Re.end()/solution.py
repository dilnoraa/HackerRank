# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
string = raw_input()
substring = raw_input()
substring_len = len(substring)
m = re.search(substring, string)
tuple_list = []
for x in range(0, len(string)):
    end = x + substring_len
    m = re.search(substring, string[x:end])
    if m:
        tupl = (m.start()+x, m.start()+x+substring_len-1)
        tuple_list.append(tupl)
if len(tuple_list) == 0:
    tuple_list.append((-1, -1))
        
for item in tuple_list:
    print item
