def get_products_of_all_ints_except_at_index(int_list):

    # Make a list of the products
    # store_f = int_list[0]
    # store_r = int_list[len(int_list) - 1]
    store_f = 1
    store_r = 1
    final = [1] * len(int_list)
    
    print("about to go forward")
    for index, value in enumerate (int_list):
        print(index)
        print(value)
        final[index] = store_f
        
        store_f *= value;
        print(final)
    
    print("about to reverse")    
    for index, value in  reversed(list(enumerate(int_list))):
        print(index)
        print(value)
        final[index] *= store_r
        store_r *= value
        print(final)

    return final


int_list = [1, 7, 3, 4]
print get_products_of_all_ints_except_at_index(int_list)
