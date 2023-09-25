def flatten_list(nested_list):
    flattened = [item for sublist in nested_list for item in sublist]
    return flattened

nested_list = [[1,2,3], [4,5], [6,7,8,9]]

flattened_list = flatten_list(nested_list)
print(flattened_list)