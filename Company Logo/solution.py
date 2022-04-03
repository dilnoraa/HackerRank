#!/bin/python3
import collections


if __name__ == '__main__':
    s = input()
    counter_dict = collections.Counter(sorted(s))
    sorted_dict = sorted(counter_dict.items(), key=lambda item: item[1], reverse=True)
    count = 0
   
    for i in sorted_dict:
        if count == 3:
            break
        print("{} {}".format(i[0], i[1]))
        count = count + 1
