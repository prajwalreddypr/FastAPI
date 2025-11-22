# def print_numbers(highest, lowest):
#      print("highest", highest)
#      print("lowest", lowest)
     
# print_numbers(lowest = 3, highest = 10)


# def multiply(a, b):
#     return a*b

# print(multiply(2,4))


#functions calling each other
def buy_item(cost_of_item):
    return cost_of_item + add_tax(cost_of_item)

def add_tax(cost_of_item):
    current_tax = 0.03
    return cost_of_item * current_tax

print(buy_item(50))