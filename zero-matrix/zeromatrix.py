"""Given an NxM matrix, if a cell is zero, set entire row and column to zeroes.

A matrix without zeroes doesn't change:

    >>> zero_matrix([[1, 2 ,3], [4, 5, 6], [7, 8, 9]])
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

But if there's a zero, zero both that row and column:

    >>> zero_matrix([[1, 0, 3], [4, 5, 6], [7, 8, 9]])
    [[0, 0, 0], [4, 0, 6], [7, 0, 9]]

Make sure it works with non-square matrices:

    >>> zero_matrix([[1, 0, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    [[0, 0, 0, 0], [5, 0, 7, 8], [9, 0, 11, 12]]

FiveStars example:
Given a N & M matrix containing 0s and 1s,
For every "0" in the matrix,
Replace that entire row and column with
0s, and return the new matrix

 1 1 1 1           1 0 1 0
 1 0 1 1           0 0 0 0
 1 1 1 1    --->   1 0 1 0
 1 1 1 0           0 0 0 0
 1 1 1 1           1 0 1 0

    >>> zero_matrix([[1, 1, 1, 1], [1, 0, 1, 1], [1, 1, 1, 1], [1, 1, 1, 0], [1, 1, 1, 1]])
    [[1, 0, 1, 0], [0, 0, 0, 0], [1, 0, 1, 0], [0, 0, 0, 0], [1, 0, 1, 0]]
"""


def zero_matrix(matrix):
    """Given an NxM matrix, for cells=0, set their row and column to zeroes."""

# Convention represents M as rows and N as columns

    if not matrix:
        return []

    m_rows = len(matrix)
    n_cols = len(matrix[0])

    clear_rows = [False] * m_rows
    clear_cols = [False] * n_cols

    # Find which rows and columns to clear
    for y in range(m_rows):
        for x in range(n_cols):
            if matrix[y][x] == 0:
                clear_rows[y] = True
                clear_cols[x] = True

    # Actually clear rows and columns
    for y in range(m_rows):
        for x in range(n_cols):
            if clear_rows[y] or clear_cols[x]:
                matrix[y][x] = 0

    return matrix


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** TESTS PASSED! YOU'RE DOING GREAT!\n"
