import operator, functools,copy
def highest_product_of_3(list_of_ints):
    # Calculate the highest product of 3 integers
    max_product = float('-inf')
    min_list = []
    max_list = []
    for i in list_of_ints:
        print(max_product)
        print(min_list)
        print(max_list)
        print("made it")
        min_list.append(i)
        max_list.append(i)
        cur_max =  max(_mult_list(min_list), _mult_list(max_list))
        del min_list[-1]
        del max_list[-1]
        if cur_max > max_product:
            max_product = cur_max
        max_list = min_2_nums(max_list, i)
        min_list = max_2_nums(min_list, i)
    return max_product

    # return functools.reduce(operator.mul, product_ints, -1)

def _mult_list(list_of_ints):
    return functools.reduce(operator.mul, list_of_ints)

def min_2_nums(int_list, i):
    if int_list and len(int_list) == 2:
        not_min = max(int_list)
        if i < not_min:
            int_list[int_list.index(not_min)] = i
    elif int_list or len(int_list) < 2:
        int_list.append(i)
    return int_list

def max_2_nums(int_list, i):
    if int_list and len(int_list) == 2:
        not_max = min(int_list)
        if i > not_max:
            int_list[int_list.index(not_max)] = i
    elif int_list or len(int_list) < 2:
        int_list.append(i)
    return int_list

list_of_ints = [-10, -10, 1, 3, 2]
print(highest_product_of_3(list_of_ints))



# def track_2_nums(int_list, i):
#     if int_list and len(int_list >= 2):
#         signless_list = []
#         val_map = {}
#         for x in int_list:
#             mag = abs(x)
#             signless_list.append(x)
#             val_map[mag] = x
# 
#         min_magnitude = min(signless_list)
#         i_magnitude = abs(i)
#         if max(min_magnitude, i_magnitude) == i_magnitude:
#             int_list.remove(val_map[min_magnitude])
#             int_list.append(i)
#         return int_list
#     elif len(int_list < 2):
#         int_list.append(i)
