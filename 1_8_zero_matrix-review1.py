import unittest

def zero_matrix(matrix):
    # find 0 index
    row_index = []
    col_index = []
    for row in matrix:
        if 0 in row:
            row_index.append(matrix.index(row)) # Row indices
            col_index.append(row.index(0))      # Col indices

    # set row to zero
    for idx in row_index:
        i = 0
        while i < len(matrix[idx]):
            matrix[idx][i] = 0
            i += 1

    # set col to zero
    for idx in col_index:
        i = 0
        while i < len(matrix):
            matrix[i][idx] = 0
            i += 1

    print_matrix(matrix)
    return matrix

def print_matrix(matrix):
    for row in matrix:
        for col in row:
           pad = 3 - len(str(col))
           print(' ' * pad + str(col), end='')
        print('\n')
 

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ([
            [ 1,  2,  3,  4, 5],
            [ 6,  7,  8,  0, 10],
            [11,  0, 13, 14, 15],
            [16, 17, 18, 19, 20],
        ], [
            [ 1,  0,  3,  0,  5],
            [ 0,  0,  0,  0,  0],
            [ 0,  0,  0,  0,  0],
            [16,  0, 18,  0, 20],
        ])
    ]




    def test_zero_matrix(self):
        print('Zero matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.')

        for [test_matrix, expected] in self.data:
            actual = zero_matrix(test_matrix)
            self.assertEqual(actual, expected)

if __name__ == '__main__':            
    unittest.main()

# MISTAKES Misread problem assumed only 1 zero, could have used functions to increase readability of nested loops, space complexity optimization - use first row as tracker