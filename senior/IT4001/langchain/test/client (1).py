'''
第一區 X:0.3 Y:0.65 ,X:0 Y:0.35
第二區 X:0.65 Y:0.35, X:0.35 Y:0.05
範圍是0.3 *0.3 兩個平面中心點分別是0.5 0.2 跟 0.15 0.5
0.8 * 0.8
'''

def capture_image():
    '''
    __summary__ : the api will return the frame raw byte
    params : N/A
    return [640 x 640 x 3]
    '''
    # Dummy data
    # data = random.randint(0, 255)
    image = [[[1 for _ in range(3)] for _ in range(640)] for _ in range(640)]
    return image

def detect(img):
    '''
    __summary__ : the api will return all cubes position(pixel) and RGB data
    params : 
        image: [640 x 640 x 3]
    return [{"position":(
            x1: left top x pixel of the cube, 
            y1: left top y pixel of the cube, 
            x2: bottom right x pixel of the cube, 
            y2: bottom right y pixel of the cube
        ),
        "color":
            c: color of the cube
        }, ...]
    '''
#     # Dummy data
#     cubes = [
#         {"position": [10, 10, 34, 34], "color": "RED"},
# #         {"position": [10, 20, 34, 4], "color": "RED"}
#     ]
    cubes = [
        {"position": [10, 10, 34, 34], "color": "RED"},
        {"position": [10, 30, 34, 54], "color": "BLUE"},
        {"position": [10, 20, 34, 44], "color": "RED"},
    ]
    return cubes

def get_objects_info(object):
    '''
    __summary__ : the api will return the cube's coordinate and the quaternion
    params : 
        object:{
            "position":(
                x1: left top x pixel of the cube, 
                y1: left top y pixel of the cube, 
                x2: bottom right x pixel of the cube, 
                y2: bottom right y pixel of the cube
            ),
            "color":
                c: color of the cube
            }
    return 
        dict: A dictionary with the cube's position, orientation (quaternion), and color.
        {
        "position":(
            x: x coordinate of the cube, 
            y: y coordinate of the cube, 
            z: z coordinate of the cube
        ),
        "orientation":(
            qw: float, first quaternion param of the point
            qx: float, second quaternion param of the point
            qy: float, third quaternion param of the point
            qz: float, fourth quaternion param of the point
        )
        "color":
            c: color of the cube
        }
    '''
    data = obj

    # Dummy data
    cube_detail = {
        "position": [0.3, -0.35, -0.4014],
        "orientation": [1, 0, 0, 0],
        "color": "RED",
    }
    return cube_detail

