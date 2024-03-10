def gauss(a, b, n):
    # a: augmented matrix's left-hand side in systems of linear equations
    # b: augmented matrix's right-hand side in systems of linear equations
    # n: row's and column's numbers of matrix a and row's numbers of matrix b
    x = []
    elimination(a, b, n)
    x = substitution(a, b, n)
    return x


def elimination(a, b, n):
    for row_pivot in range(0, n - 1):
        pivoting(a, b, n, row_pivot)
        for row_eliminate in range(row_pivot + 1, n):
            factor = a[row_eliminate][row_pivot] / a[row_pivot][row_pivot]
            for column_eliminate in range(row_pivot + 1, n):
                a[row_eliminate][column_eliminate] -= factor * a[row_pivot][column_eliminate]
            b[row_eliminate] -= factor * b[row_pivot]


def substitution(a, b, n):
    # --------------------- initialize x with 0
    x = []
    for i in range(0, n):
        x.append(0)

    x[n - 1] = b[n - 1] / a[n - 1][n - 1]
    for j in range(n - 2, -1, -1):
        b_sum = b[j]
        for k in range(j + 1, n):
            b_sum -= a[j][k] * x[k]
        x[j] = b_sum / a[j][j]

    return x


def pivoting(a, b, n, row):
    pivot_row = row
    # -------------------------------- find the maximum element in different row
    max_element = abs(a[row][row])
    for peek_row in range(row + 1, n):
        max_dummy = abs(a[peek_row][peek_row])
        if max_dummy > max_element:
            max_element = max_dummy
            pivot_row = peek_row
    # -------------------------------- switch
    if pivot_row != row:
        # switch a
        for switch_column in range(row, n):
            temp = a[pivot_row][switch_column]
            a[pivot_row][switch_column] = a[row][switch_column]
            a[row][switch_column] = temp
        # switch b
        temp = b[pivot_row]
        b[pivot_row] = b[row]
        b[row] = temp


matrix_a = [[1.0, 2.0, -1.0], [5.0, 2.0, 2.0], [-3.0, 5.0, -1.0]]
matrix_b = [2.0, 9.0, 1.0]
a_row_number = len(matrix_a)
x_ans = gauss(matrix_a, matrix_b, a_row_number)

count = 1
for ii in x_ans:
    print("x%d = %f" % (count, ii))
    count += 1