def p11(citations=[]):
    citations.sort(reverse=True)  # 將 citations 列表從大到小進行排序
    
    h_index = 0
    for i, citation in enumerate(citations, start=1):
        if citation >= i:  # 如果引用次數大於等於文章篇數，則更新 H-Index
            h_index = i
        else:
            break  # 如果不滿足條件，跳出迴圈
    
    return h_index

# 測試
print(p11([3, 0, 6, 1, 5]))  # 輸出：3
print(p11([1, 3, 1]))       # 輸出：1
