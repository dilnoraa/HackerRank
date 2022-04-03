# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
if __name__ == '__main__':
    shoes_amount = raw_input()
    sizes = raw_input()
    customer_amount = int(raw_input())
    size_list = [int(x) for x in sizes.split(" ")]
    size_list_counter = Counter(size_list)
    earned_money = 0
    for i in range(0, customer_amount):
        price = raw_input()
        price = [int(x) for x in price.split(" ")]
        desired_size = price[0]
        price_for_shoe = price[1]
        if desired_size in size_list_counter.keys() and size_list_counter[desired_size] > 0:
            earned_money = earned_money + price_for_shoe
            size_list_counter[desired_size] -= 1
  
    print earned_money
