# v0.0.4

這次的版本會根據上一版的結果，已修正傳入模型的類別，並非全部都一定要是 str，因此這個版本會嘗試加入更多 cubes 加入測試，考驗模型是否能從更多 cubes 中判斷已被抓取的物件，開始構建 `Gradio` User Interface。

Setting
---
```python
cubes = [
    {"position":[10, 10, 34, 34], "feature":{"color":"RED"}},
    {"position":[10, 30, 34, 54], "feature":{"color":"BLUE"}},
    {"position":[10, 20, 34, 44], "feature":{"color":"GREEN"}},
]

real_cubes = [
    {'position': [0.26, -0.36, 0.02], 'orientation': [1, 0, 0, 0], 'feature': {'color': 'Red'}}, 
    {'position': [0.48, -0.42, 0.02], 'orientation': [1, 0, 0, 0], 'feature': {'color': 'Blue'}}, 
    {'position': [0.49, 0.05, 0.02], 'orientation': [1, 0, 0, 0], 'feature': {'color': 'Green'}}, 
]
```

Promblems
---
目前拿完第一顆紅球都沒遇到狀況，不過後面都會以 `!=RED` 的方式檢索剩下的 cubes，不過可以知道在三個球的時候，只要拿完的 cube 是不會出現在模型儲存的變數 `real_cubes` 裡面，不過兩個球的時候模型不會自己移除已經被拿過的 cube。
- 更 1: 若三個 cubes 是成功的話又不會自己移除被拿過的 cube，時間會從原本兩個 cubes 的 50 秒左右，提升至 67 秒，在理論值之中，多拿一個 cube 會多出抓大概 6 x 3 秒。 
- 更 2: 上述模型會自己移除的情況是在拿完紅色 cube 後，檢索剩下的 cubes 時，使用 `!=RED` 造成找不到其他的方塊時，才會自己把 `real_cubes` 給移出 `red cube`。

Results
---
目前有兩顆球要放同一區時，都會放在重複的位置，這樣需要調整 `prompt` 告訴 cube 的大小，以及放置時需要注意保持一定間距。不過可以確定模型是有能力處理兩個以上的 cube，如此可以更吻合我們的情境，不過還是要考量到運行時間會疊上去，因為當有更多物件出現時，同時也意味著模型有更多的判斷需要去處理，也就是會多一步的思考過程，如此至少增加 5 至 6 秒。

Pass
---
### Scenario1
- [x] Scenario1: Place the red cubes in Area A, and place the remaining cubes in Area B.
- [x] Scenario1.1: Place the blue cubes in Area B, and place the remaining cubes in Area A.
- [x] Scenario1.2: Place the red cubes in Area B, and place the remaining cubes in Area A.
- [ ] Scenario1.3: Place the black cubes in Area A.
- [x] Scenario1.4: Place the black cubes in Area A, and place the remaining cubes in Area A.


### Scenario2
- [ ] Without considering colors, half cubes are placed in Area A, and the other half cubes are placed in Area B.


Successfully in Three cubes
---
Entering new AgentExecutor chain...
Thought: To achieve the task of placing the red cubes in Area A and the remaining cubes in Area B, I need to follow the steps that I have broken down. I also need to use specific tools to pick up and place the cubes. I should start by getting the scene information and then use the tools to detect all the cubesand find the specific red cubes. After that, I can pick up the red cubes and place them in Area A. Finally, I can pick up the remaining cubes and place them in Area B.

Action:
```
{
  "action": "get_scene",
  "action_input": {}
}
```


Observation:
        Scene captured and base64_str stored in scene_info.txt successfully!!!

Thought:Now that I have captured the scene information, I can use the `detect_all_cubes` tool to find all the cubes present in the scene.

Action:
```
{
  "action": "detect_all_cubes",
  "action_input": {
    "scene_info_file_path": "scene_info.txt"
  }
}
```
Observation:
            All cubes have been stored successfully.

            Total num of cube(s): 3

            The information of cubes: [{'position': [0.26, -0.36, 0.02], 'orientation': [1, 0, 0, 0], 'feature': {'color': 'Red'}}, {'position': [0.48, -0.42, 0.02], 'orientation': [1, 0, 0, 0], 'feature': {'color': 'Blue'}}, {'position': [0.49, 0.05, 0.02], 'orientation': [1, 0, 0, 0], 'feature': {'color': 'Green'}}]

Thought:Now that I have found all the cubes present in the scene, I can use the `get_specific_cube` tool to find the specific red cubes.

Action:
```
{
  "action": "get_specific_cube",
  "action_input": {
    "features": "color=Red",
    "real_cubes": [
      {
        "position": [0.26, -0.36, 0.02],
        "orientation": [1, 0, 0, 0],
        "feature": {"color": "Red"}
      },
      {
        "position": [0.48, -0.42, 0.02],
        "orientation": [1, 0, 0, 0],
        "feature": {"color": "Blue"}
      },
      {
        "position": [0.49, 0.05, 0.02],
        "orientation": [1, 0, 0, 0],
        "feature": {"color": "Green"}
      }
    ]
  }
}
```


Observation:
            Successfully retrieved the RED cube.

            {'position': [0.26, -0.36, 0.02], 'orientation': [1, 0, 0, 0], 'feature': {'color': 'Red'}}

Thought:Now that I have found the specific red cube, I can use the `pick_up_specific_cube` tool to pickit up.

Action:
```
{
  "action": "pick_up_specific_cube",
  "action_input": {
    "specific_cube": {
      "position": [0.26, -0.36, 0.02],
      "orientation": [1, 0, 0, 0],
      "feature": {"color": "Red"}
    }
  }
}
```


Observation: Pick up the Red cube successfully!!!
Thought:Now that I have picked up the specific red cube, I can use the `place_specific_cube` tool to place it in Area A.

Action:
```
{
  "action": "place_specific_cube",
  "action_input": {
    "area_info_x": 0.15,
    "area_info_y": 0.5,
    "specific_cube": {
      "position": [0.26, -0.36, 0.02],
      "orientation": [1, 0, 0, 0],
      "feature": {"color": "Red"}
    }
  }
}
```


Observation: Place the Red cube successfully!!!
Thought:Now that I have placed the specific red cube in Area A, I can repeat the process for the remaining cubes. I will use the `get_specific_cube` tool to find the specific blue and green cubes, pick them up using the `pick_up_specific_cube` tool, and place them in Area B using the `place_specific_cube` tool.

Action:
```
{
  "action": "get_specific_cube",
  "action_input": {
    "features": "color=Blue",
    "real_cubes": [
      {
        "position": [0.26, -0.36, 0.02],
        "orientation": [1, 0, 0, 0],
        "feature": {"color": "Red"}
      },
      {
        "position": [0.48, -0.42, 0.02],
        "orientation": [1, 0, 0, 0],
        "feature": {"color": "Blue"}
      },
      {
        "position": [0.49, 0.05, 0.02],
        "orientation": [1, 0, 0, 0],
        "feature": {"color": "Green"}
      }
    ]
  }
}
```


Observation:
            Successfully retrieved the BLUE cube.

            {'position': [0.48, -0.42, 0.02], 'orientation': [1, 0, 0, 0], 'feature': {'color': 'Blue'}}

Thought:Now that I have found the specific blue cube, I can use the `pick_up_specific_cube` tool to pick it up.

Action:
```
{
  "action": "pick_up_specific_cube",
  "action_input": {
    "specific_cube": {
      "position": [0.48, -0.42, 0.02],
      "orientation": [1, 0, 0, 0],
      "feature": {"color": "Blue"}
    }
  }
}
```



Observation: Pick up the Blue cube successfully!!!
Thought:Now that I have picked up the specific blue cube, I can use the `place_specific_cube` tool to place it in Area B.

Action:
```
{
  "action": "place_specific_cube",
  "action_input": {
    "area_info_x": 0.5,
    "area_info_y": 0.2,
    "specific_cube": {
      "position": [0.48, -0.42, 0.02],
      "orientation": [1, 0, 0, 0],
      "feature": {"color": "Blue"}
    }
  }
}
```



Observation: Place the Blue cube successfully!!!
Thought:Now that I have placed the specific blue cube in Area B, I can repeat the process for the remaining green cube. I will use the `get_specific_cube` tool to find the specific green cube, pick it up using the `pick_up_specific_cube` tool, and place it in Area B using the `place_specific_cube` tool.

Action:
```
{
  "action": "get_specific_cube",
  "action_input": {
    "features": "color=Green",
    "real_cubes": [
      {
        "position": [0.26, -0.36, 0.02],
        "orientation": [1, 0, 0, 0],
        "feature": {"color": "Red"}
      },
      {
        "position": [0.48, -0.42, 0.02],
        "orientation": [1, 0, 0, 0],
        "feature": {"color": "Blue"}
      },
      {
        "position": [0.49, 0.05, 0.02],
        "orientation": [1, 0, 0, 0],
        "feature": {"color": "Green"}
      }
    ]
  }
}
```



Observation:
            Successfully retrieved the GREEN cube.

            {'position': [0.49, 0.05, 0.02], 'orientation': [1, 0, 0, 0], 'feature': {'color': 'Green'}}

Thought:Now that I have found the specific green cube, I can use the `pick_up_specific_cube` tool to pick it up.

Action:
```
{
  "action": "pick_up_specific_cube",
  "action_input": {
    "specific_cube": {
      "position": [0.49, 0.05, 0.02],
      "orientation": [1, 0, 0, 0],
      "feature": {"color": "Green"}
    }
  }
}
```



Observation: Pick up the Green cube successfully!!!
Thought:Now that I have picked up the specific green cube, I can use the `place_specific_cube` tool to place it in Area B.

Action:
```
{
  "action": "place_specific_cube",
  "action_input": {
    "area_info_x": 0.5,
    "area_info_y": 0.2,
    "specific_cube": {
      "position": [0.49, 0.05, 0.02],
      "orientation": [1, 0, 0, 0],
      "feature": {"color": "Green"}
    }
  }
}
```



Observation: Place the Green cube successfully!!!
Thought:Now that I have placed all the cubes in their respective areas, I have successfully achieved the task of placing the red cubes in Area A and the remaining cubes in Area B.

Action:
```
{
  "action": "Final Answer",
  "action_input": "I have successfully placed the red cubes in Area A and the remaining cubes in Area B."
}
```

> Finished chain.
Tokens Used: 27710
        Prompt Tokens: 26001
        Completion Tokens: 1709
Successful Requests: 12
Total Cost (USD): $0.0424195
Total second(s) used: 67.6929349899292