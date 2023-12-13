def hw2_0(rows=3):
    output = ''
    # ======↓請在這個區域寫程式↓=====
    for i in range(0, rows):
        if i != (rows-1):
            output += " " * (rows - i-1) + " *" * (i + 1) + '\n'
        else:
            output += " " * (rows - i-1) + " *" * (i + 1)

    # ======↑請在這個區域寫程式↑=====
    return output

print(hw2_0(5))