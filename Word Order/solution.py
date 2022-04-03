# Enter your code here. Read input from STDIN. Print output to STDOUT
line_amount = int(input())
words_dict = {}
for i in range(line_amount):
    word = input()
    if not word in words_dict:
        words_dict[word] = 1
    else:
        words_dict[word] = words_dict[word] + 1
        
print(len(words_dict))
result = " ".join(str(i) for i in words_dict.values())
print(result)
