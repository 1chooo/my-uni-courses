def hw2_0(rows=3):
    output = ''
    # ======↓請在這個區域寫程式↓=====
    for i in range(1, rows + 1):
        for j in range(rows - i):
            output += " "

        for k in range(i):
            if i == rows and k == i - 1:
                output += "*"
            elif k == i - 1:
                output += "*\n"
            else:
                output += "* "
    # ======↑請在這個區域寫程式↑=====
    return output


print(hw2_0(5))
