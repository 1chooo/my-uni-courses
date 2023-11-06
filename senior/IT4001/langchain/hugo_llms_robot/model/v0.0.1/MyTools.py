from langchain.tools import BaseTool
from client import *
import base64
import json
import ast

def get_scene() -> str:

    """
    This function is used to capture the scene information \
    by calling an API that retrieves the necessary data. 
    The captured scene info is stored in a global variable \
    and the specific file_path for future access.
    
    goal: capture the scene information
    
    Output will be the execute status of this tool.
    """
    
    try:
        scene_info = capture_image()
        
        json_str = json.dumps(scene_info)

        base64_str = base64.b64encode(json_str.encode()).decode()

        with open("scene_info.txt", "w") as file:
            file.write(base64_str)

        result = f"""
        Scene captured and base64_str stored successfully!!!
        """
    
        return result
    
    except Exception as e:
        result = f"""
        The exception message: {str(e)}
        """
        return result
    
def detect_all_cubes(scene_info_path='scene_info.txt') -> str:
    """
    This function analyzes the provided scene information to detect and extract
    information about cubes present in the scene. In other words, you have to use get_scene()
    before you detect all the cubes, or you do not have the data about the scene
    
    goal: find all the cubes from the scene
    
    Output will be the execute status of this tool.
    """
    
    try:
        with open(scene_info_path, 'r') as file:
            scene_info_base64_str = file.read()
            
        decoded_bytes = base64.b64decode(scene_info_base64_str)
        decoded_str = decoded_bytes.decode('utf-8')
        decoded_list = ast.literal_eval(decoded_str)
        
        if decoded_list is not None:
            cubes = detect(decoded_list)
            
            cubes_num = len(cubes)
            cubes_str = str(cubes)
            cubes_bytes = cubes_str.encode('utf-8')
            cubes_base64_str = base64.b64encode(cubes_bytes).decode('utf-8')

            # Save the base64 representation of 'cubes' to a txt file
            with open('all_cubes_output.txt', 'w') as output_file:
                output_file.write(cubes_base64_str)
                
            result = f"""
            All cubes have been stored successfully.\n 
            Total num of cubes: {cubes_num}\n
            The information of cubes: {cubes_str}
            """

            return result
        else:
            result = f"""Scene information is not available. \
            Please ensure you have the data about the scene."""
            return result
    except Exception as e:
        result = f"""
        The exception message: {str(e)}
        """
        return result

def get_specific_cube(features: str, cubes_str) -> str:
    """

    Make sure features in cube_str and ensure you have already 
    obtained the scene and all cubes before using this function.
    
    goal: find the specific cube from the scene
    
    Output will be the execute status of this tool.
    """
    
#     color:black

#     This function retrieves information about all cubes with the given 
#     features from the list of cubes. Therefore, 
    try: 
#         with open('all_cubes_output.txt', 'r') as file:
#             cubes = file.read()

#         cubes_bytes = base64.b64decode(cubes)
#         cubes_str = cubes_bytes.decode('utf-8')
#         cubes_list = ast.literal_eval(cubes_str)
        
        cubes_list = ast.literal_eval(cubes_str)
        feature_dict = ast.literal_eval(features)
        color_value = feature_dict['color']
        target_features = color_value.upper()
        
        result = []

        for cube in cubes_list:
            if 'feature' in cube and 'color' in cube['feature']:
                color = cube['feature']['color'].upper()
                if color == target_features:
                    result.append(get_objects_info(cube))
        
        if result:
            result_str = str(result)
            cube_str = str(result_str)
            cubes_bytes = cube_str.encode('utf-8')
            cubes_base64_str = base64.b64encode(cubes_bytes).decode('utf-8')
            with open('specific_cubes_output.txt', 'w') as output_file:
                output_file.write(cubes_base64_str)
            return f"Successfully retrieved the specific cube(s).\n{cube_str}"
        else:
            return "No cubes with the specified features were found."
    except Exception as e:
        result = f"""
        The exception message: {str(e)}
        """
        return result
    
def pick_up_specific_cube():
    """
    This function is used to pick up the cube after getting the
    information of specific cube.
    
    goal: pick up the specific cubes
    
    Output will be the execute status of this tool.
    """
    try: 
        with open('specific_cubes_output.txt', 'r') as file:
            cubes = file.read()

        cubes_bytes = base64.b64decode(cubes)
        cubes_str = cubes_bytes.decode('utf-8')
        cubes_list = ast.literal_eval(cubes_str)

        position = cubes_list[0]['position']
        orientation = cubes_list[0]['orientation']
        feature = cubes_list[0]['feature']

        pick_or_not = franka_pick(
            x=position[0], y=position[1], z=position[2],
            qw=orientation[0], qx=orientation[1], 
            qy=orientation[2], qz=orientation[3]
        )
        if pick_or_not:
            result = f"Pick up the {feature['color']} cube successfully!!!"
            return result
        else:
            result = f"Pick up the {feature['color']} cube Failure!!!"
            return result
    except Exception as e:
        result = f"""
        The exception message: {str(e)}
        """
        return result 
    
def place_specific_cube(area_info_x, area_info_y):
    """
    This function is used to place the cube after picking
    up the cube, then place into the specific area.
    
    goal: place the specific cubes
    
    Output will be the execute status of this tool.
    """
    try: 
        with open('specific_cubes_output.txt', 'r') as file:
            cubes = file.read()

        cubes_bytes = base64.b64decode(cubes)
        cubes_str = cubes_bytes.decode('utf-8')
        cubes_list = ast.literal_eval(cubes_str)

        position = cubes_list[0]['position']
        orientation = cubes_list[0]['orientation']
        feature = cubes_list[0]['feature']
        
#         print(area_info_x)
#         print(type(area_info_x))

        place_or_not = franka_place(
            x=float(area_info_x), y=float(area_info_y),
#             x=float(area_info_x['default']), y=float(area_info_y['default']),
        )
        if place_or_not:
            result = f"Place the {feature['color']} cube successfully!!!"
            return result
        else:
            result = f"Place the {feature['color']} cube Failure!!!"
            return result
    except Exception as e:
        result = f"""
        The exception message: {str(e)}
        """
        return result 
            
def break_down_scenario(scenario: str) -> str:
    """
    This function analyzes the provided scenario, representing the goal to be achieved, 
    and breaks down the big mission into smaller tasks.
    
    goal: break down the big mission into small pieces
    
    Output will be the break down tasks of the scenario
    """
    
    try:
        result = f"The scenario has been breaked down!!!"
        return result
    except Exception as e:
        result = f"""
        The exception message: {str(e)}
        """
        return result


def decode_base64_to_list(base64_str):
    try:
        decoded_bytes = base64.b64decode(base64_str)
        decoded_str = decoded_bytes.decode('utf-8')
        decoded_list = ast.literal_eval(decoded_str)

        return decoded_list
    except Exception as e:
        print("Error while decoding base64 string:", e)
        return []