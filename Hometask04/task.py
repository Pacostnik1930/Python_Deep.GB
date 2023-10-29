def transpose_matrix(matrix):
    """
    Transposes a matrix.
    :param matrix: A 2D matrix.
    :return: The transposed matrix.
    """
    rows = len(matrix)
    cols = len(matrix[0])
    transposed_matrix = [[0 for j in range(rows)] for i in range(cols)]
    for i in range(rows):
        for j in range(cols):
            transposed_matrix[j][i] = matrix[i][j]
    return transposed_matrix


def key_value_dict(**kwargs):
   
    result_dict = {}
    result_dict.update({'key1': 'value1', 'key2': 'value2'})
    result_dict['key3'] = 'value3'

    for key, value in kwargs.items():
        if hash(key) is not None:
            result_dict[value] = key
        else:
            result_dict[str(value)] = key
    return result_dict