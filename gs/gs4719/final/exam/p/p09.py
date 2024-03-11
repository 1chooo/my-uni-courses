def rotate_matrix(matrix, angle):
    n = len(matrix)
    rotated_matrix = [[0 for _ in range(n)] for _ in range(n)]

    # 计算实际旋转角度
    actual_angle = angle % 360

    if actual_angle == 0:
        return matrix

    # 旋转矩阵
    if actual_angle == 90 or actual_angle == -270:
        for i in range(n):
            for j in range(n):
                rotated_matrix[j][n - 1 - i] = matrix[i][j]
    elif actual_angle == 180 or actual_angle == -180:
        for i in range(n):
            for j in range(n):
                rotated_matrix[n - 1 - i][n - 1 - j] = matrix[i][j]
    elif actual_angle == 270 or actual_angle == -90:
        for i in range(n):
            for j in range(n):
                rotated_matrix[n - 1 - j][i] = matrix[i][j]
    elif actual_angle == 360 or actual_angle == -360:
        return matrix  # 不需要旋转
    else:
        return None  # 不支持的角度

    return rotated_matrix

def p09(matrix, angle):
    # 检查输入参数是否符合要求
    valid_angles = {-360, -270, -180, -90, 0, 90, 180, 270, 360}
    if angle not in valid_angles:
        return "Invalid angle"

    rotated_matrix = rotate_matrix(matrix, angle)
    return rotated_matrix

# 示例输入
input_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
input_angle = 90

# 调用函数并打印输出结果
output_matrix = p09(input_matrix, input_angle)
if isinstance(output_matrix, list):
    for row in output_matrix:
        print(row)
else:
    print(output_matrix)
