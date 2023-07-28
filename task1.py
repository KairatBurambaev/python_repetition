matrix = [[1,2,3],['a','b','c']]

def transpose_matrix(matrix):

    rows = len(matrix)
    cols = len(matrix[0])
    
    transposed_matrix = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            transposed_matrix[j][i] = matrix[i][j]
    
    return transposed_matrix

print(transpose_matrix(matrix))