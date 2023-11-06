# v0.0.3

這次的版本主要想嘗試把 detect 物件的時候，一起存出來的 list 改成是直接拿到真實座標，因此兩個 tool `detect_all_cubes`, `get_specific_cube` 將直接改寫，並且把 LLMs 的輸入從原先的 `str` 改成直接用原本的型態，略過 `str` 的型別轉換。

Detail
---
1. 避免使用過多 `ast` 將 `str` 轉換成 `dict`
2. 調整回傳給模型的型別，非必要為 `str` 則照原本型別

Problems
---
### `features` 會找不到
解法:直接給我想處理的字串樣式
```python
example of features:
- color=COLOR_NAME
- color:COLOR_NAME
```

### 同樣的 prompts，同樣的描述，有時候能執行完成，有時候會直接斷掉(知道下一步該怎麼做的情況)
後來，就又沒什麼遇到了

Pass
---
### Scenario1
- [x] Scenario1: Place the red cubes in Area A, and place the remaining cubes in Area B.
- [x] Scenario1.1: Place the blue cubes in Area B, and place the remaining cubes in Area A.
- [x] Scenario1.2: Place the red cubes in Area B, and place the remaining cubes in Area A.

### Scenario2
- [x] Without considering colors, half cubes are placed in Area A, and the other half cubes are placed in Area B.

這條會過，不過`get_specific_cube` 這個 Tool 會完全沒用到，間接證明了模型其實可以在已經知道有哪些 cubes 的情境自行去查找想要 `pick` 的目標 -> 或許可以改進 Tool 的寫法，如此可以優化 `get_specific_cube`。

Final
---
這版的特色，修正後會發現自己傳入 Tools 的變數不對，並且具有能力自行修正進下一次執行，不過仍然無法擴充 `adjust_brightness`, `reset`。下一版的嘗試會先將 cubes 的數量提升做嘗試，測試是否能辨識已經被抓過的 cube。