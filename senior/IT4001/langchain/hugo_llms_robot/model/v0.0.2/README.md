# v0.0.2

In this version, Scenario 1 is successful. The only change made is in the `MyTools.py` file. The descriptions and prompts for `role`, `scenario`, `break_down_example`, `A_area`, `B_area`, and `agent_executor` remain unchanged.

How to succeed
---
### Catch the probally type when `get_specific_cube()`
```python
def get_specific_cube(features: str, cubes_str) -> str:
if features[:6] == 'color=':
    color_value = features[6:]
    target_features = color_value.upper()
elif features[:6] == 'color:':
    color_value = features[6:]
    target_features = color_value.upper()
else:
    feature_dict = ast.literal_eval(features)
    color_value = feature_dict['color']
    target_features = color_value.upper()
```

### Change prompts in Tools

The beginning of the prompts in the tools change into "useful for when you need to ..."

Pass
---
- [x] Scenario1: Place the red cubes in Area A, and place the remaining cubes in Area B.
- [x] Scenario1.1: Place the blue cubes in Area B, and place the remaining cubes in Area A.
- [x] Scenario1.2: Place the red cubes in Area B, and place the remaining cubes in Area A.

New Found
---
1. We can give the LangChain with the `float` type variables instead of only in `str` type.
2. If show up `color!=RED` it will occur Error!

Future Work
---
1. Still need to improve the tools.
2. add more cubes in the scenarios.
3. The beginning step of LLM is to check the brightness.