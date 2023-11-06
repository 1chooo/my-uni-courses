'''
第一區 X:0.3 Y:0.65 ,X:0 Y:0.35
第二區 X:0.65 Y:0.35, X:0.35 Y:0.05
範圍是0.3 *0.3 兩個平面中心點分別是0.5 0.2 跟 0.15 0.5
0.8 * 0.8
'''

def capture_image():
    # Dummy data
    # data = random.randint(0, 255)
    image = [[[1 for _ in range(3)] for _ in range(640)] for _ in range(640)]
    return image

def detect(img):
    # Dummy data
    cubes = [
        {"position":[10, 10, 34, 34], "feature":{"color":"RED"}},
        {"position":[10, 30, 34, 54], "feature":{"color":"BLUE"}},
#         {"position":[10, 20, 34, 44], "feature":{"color":"RED"}},
    ]
    return cubes

def get_objects_info(obj):

    data = obj

    if 'feature' in data and 'color' in data['feature']:
        color = obj['feature']['color'].upper()
        if color == "RED":
            cube_detail = {
                "position": [0.3, -0.35, -0.4014],
                "orientation": [1, 0, 0, 0],
                "feature": {
                    "color": "RED"
                } 
            }
        else:
            cube_detail = {
                "position": [0.4, -0.3, -0.4014],
                "orientation": [1, 0, 0, 0],
                "feature": {
                    "color": "BLUE"
                } 
            }

    return cube_detail

def franka_pick(x, y, z, qw, qx, qy, qz):
    data = {
        "coordinates": {"x": x, "y": y, "z": z},
        "orientation": {"qw": qw, "qx": qx, "qy": qy, "qz": qz},
    }

    return True

def franka_place(x, y):
    data = {
        "coordinates": {"x": x, "y": y, "z": -0.4014},
        "orientation": {"qw": 1, "qx": 0, "qy": 0, "qz": 0},
    }
    
    return True

'''
real object info
'''
tmp = [
    {'position': [0.482307986551555, -0.42978072275558304, 0.02480004768371602], 'orientation': [1, 0, 0, 0], 'feature': {'color': 'Blue'}}, 
    {'position': [0.49581541132948515, 0.4567955294820938, 0.02480004768371602], 'orientation': [1, 0, 0, 0], 'feature': {'color': 'Blue'}}, 
    {'position': [0.49335950752062585, 0.05034575166628679, 0.02480004768371602], 'orientation': [1, 0, 0, 0], 'feature': {'color': 'Green'}}, 
    {'position': [0.6407128868625993, -0.372067315605667, 0.02480004768371602], 'orientation': [1, 0, 0, 0], 'feature': {'color': 'Green'}}, 
    {'position': [0.2612778980783508, -0.3646996329281328, 0.02480004768371602], 'orientation': [1, 0, 0, 0], 'feature': {'color': 'Red'}}, 
    {'position': [0.25513820763376555, 0.6373034451258054, 0.02480004768371602], 'orientation': [1, 0, 0, 0], 'feature': {'color': 'Red'}}
]