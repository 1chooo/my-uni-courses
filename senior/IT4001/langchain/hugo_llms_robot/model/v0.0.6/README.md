# v0.0.6

此版本對 cube 的上限有所突破，能夠支援最多 4 個 cubes 的夾取，並且能夠實現放置在 A, B 區不同位置，更能成功對接機械手臂。

解決問題
---
1. 方塊放置只能在中心點，調整為固定四個點可以放置
2. 模型可支援 2, 3, 4 cubes 的操作
3. 拿掉 `get_scene`，減少模型原地打轉的可能性，也是此版能成功的最大因素!

待改善問題
---
1. 模型還不知道放過的點不能再放，有時候會出錯
2. 有遇到以完成夾取又多做一次夾空氣

Pass
---
### Scenario1
- [x] Scenario1: Place the red cubes in Area A, and place the remaining cubes in Area B.
- [x] Scenario1.1: Place the blue cubes in Area B, and place the remaining cubes in Area A.
- [x] Scenario1.2: Place the red cubes in Area B, and place the remaining cubes in Area A.
- [x] Scenario1.3: Place the black cubes in Area A, and place the remaining cubes in Area A.


### Scenario2
- [ ] Without considering colors, half cubes are placed in Area A, and the other half cubes are placed in Area B.
