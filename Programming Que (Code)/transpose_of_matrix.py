def transposeOf(mat):
    '''
    Non inplace
    '''
    def a1():
        col_count = len(mat[0])
        row_count = len(mat)
        return [[mat[j][i] for j in range(row_count)] for i in range(col_count)]

    def a2():  # Best 1 Liner
        return zip(*mat) # Transpose of a matrix