def create_nested_list(array:list, row_lenght:int):
    '''
    Create a nested list or a matrix from a list, given the list
    and the row lenght or lenght of the sub_list.
    '''
    matrix = []
    i = 0
    while i < len(array):
        matrix.append(array[i:i+row_lenght])
        i += row_lenght
    return matrix