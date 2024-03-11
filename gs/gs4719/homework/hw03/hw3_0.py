def hw3_0():
    # ======請在這個區域寫程式=====
    output = [
        [
            f'{i} * {j} = {i * j}' for j in range(2, 10)
        ] for i in range(2, 10)
    ]
    # ============================
    return output


print(hw3_0())