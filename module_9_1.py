def apply_all_func(int_list, *functions):
    result_dict = {}
    for _function in functions:
        result_dict[_function.__name__] = _function(int_list)

    return result_dict


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
