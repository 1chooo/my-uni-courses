def p08(matrix):
    n = len(matrix)
    
    # 创建新的 n x n 矩阵来存储旋转后的图像
    rotated_matrix = [[0 for _ in range(n)] for _ in range(n)]
    
    # 对原始矩阵进行旋转操作
    for i in range(n):
        for j in range(n):
            rotated_matrix[j][n - 1 - i] = matrix[i][j]
    
    return rotated_matrix

# 示例输入
input_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 调用函数并打印输出结果
output_matrix = p08(input_matrix)
for row in output_matrix:
    print(row)
