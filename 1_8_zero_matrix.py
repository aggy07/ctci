import unittest

def rotate_matrix(matrix):
    n = len(matrix) # might not need varable assignment
    for layer in range(n // 2):
        first, last = layer, n - layer -1
        for i in range(first, last):
            print(layer,i)
            # save top
            top = matrix[layer][i]
            # left -> top
            matrix[layer][i] = matrix[-i - 1][layer]    



            # bottom -> left
            matrix[-i - 1][layer] = matrix[-layer - 1][-i - 1]

            # right -> bottom
            matrix[-layer - 1][-i - 1] = matrix[i][- layer - 1]

            # top -> right
            matrix[i][- layer - 1] = top
            print(matrix)
    return matrix

def zero_matrix(matrix):
    # find 0 index
    for row in matrix:
        if 0 in row:
            row_index = matrix.index(row) # Row index
            col_index = row.index(0)      # Col index

    # set row to zero
    i = 0
    while i < len(matrix[row_index]):
        matrix[row_index][i] = 0
        i += 1

    # set col to zero
    i = 0
    while i < len(matrix):
        matrix[i][col_index] = 0
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
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
        ], [
            [ 1,  2,  3,  0,  5],
            [ 0,  0,  0,  0,  0],
            [11, 12, 13,  0, 15],
            [16, 17, 18,  0, 20],
        ])
    ]




    def test_zero_matrix(self):
        print('Zero matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.')

        for [test_matrix, expected] in self.data:
            actual = zero_matrix(test_matrix)
            self.assertEqual(actual, expected)

if __name__ == '__main__':            
    unittest.main()

# MISTAKES Misread problem assumed only 1 zero