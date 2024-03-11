def p07(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    # 创建一个新的矩阵，用于存储旋转后的图像
    rotated_matrix = [[0] * rows for _ in range(cols)]

    # 通过迭代将输入矩阵旋转90度
    for i in range(rows):
        for j in range(cols):
            rotated_matrix[j][rows - 1 - i] = matrix[i][j]

    return rotated_matrix

# 示例测试
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result1 = p07(matrix1)
# print("Example 1:")
print(result1)  # 应输出 [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

matrix2 = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
result2 = p07(matrix2)
# print("Example 2:")
print(result2)  # 应输出 [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
