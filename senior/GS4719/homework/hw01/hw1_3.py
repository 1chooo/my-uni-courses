def hw1_3():
    output = ""
    #-------------------------------
    # output = # ....
    for i in range(2, 10):
        for j in range(2, 10):
            x = i * j
            output += f"{i} * {j} = {x}\n"
        if i < 9:
            output += "==\n"
        # else:
        #     output += "\n"
    #-------------------------------
    return output

print(hw1_3())