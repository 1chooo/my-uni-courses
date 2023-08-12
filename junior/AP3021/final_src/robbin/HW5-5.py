def gauss_jordan(aug, m, n, x):

    # ------------------------------ find the pivot
    j_pivot = 0
    for i_pivot in range(0, m):
        while aug[i_pivot][j_pivot] == 0:  # leading 1, not 0
            j_pivot += 1
        pivot = aug[i_pivot][j_pivot]

        # -------------------------- normalize the row by dividing it by pivot
        for j2 in range(0, n):
            aug[i_pivot][j2] /= pivot

        # -------------------------- eliminate
        for i3 in range(0, m):
            if i3 != i_pivot:
                factor = aug[i3][j_pivot]
                for j3 in range(j_pivot, n):
                    aug[i3][j3] -= factor * aug[i_pivot][j3]

    # ------------------------------ find the answer
    for i_ans in range(0, m):
        x.append(aug[i_ans][n - 1])

    return x


a = [[1.0, 2.0, -1.0, 2.0], [5.0, 2.0, 2.0, 9.0], [-3.0, 5.0, -1.0, 1.0]]
a_row_number = len(a)
a_column_number = len(a[0])
x_ans = []
gauss_jordan(a, a_row_number, a_column_number, x_ans)


count = 1
for i in x_ans:
    print("x%d = %f" % (count, i))
    count += 1
