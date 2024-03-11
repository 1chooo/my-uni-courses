def hw1_0():
    string1 = "小明花105元買了蘋果"
    string2 = "小華花130元買了香蕉"
    #-------------------------------
    # 注意cost為字串(string)的型別
    # cost = # ...
    price1 = int(string1[3:6])
    price2 = int(string2[3:6])
    
    cost = price1 + price2
    cost = str(cost)
    #-------------------------------
    return "小明和小華共花了" + cost + "元買水果"
