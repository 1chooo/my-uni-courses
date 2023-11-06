from langchain.tools import BaseTool
from client import *
import base64
import json
import ast

def get_scene() -> str:
    """
    useful for when you need to capture the scene information
    
    goal: capture the scene information
    
    Output will be the execute status of this tool.
    """
    
    try:
        scene_info = capture_image()
        json_str = json.dumps(scene_info)
        base64_str = base64.b64encode(json_str.encode()).decode()
        
        scene_info_file_path = 'scene_info.txt'

        with open(scene_info_file_path, "w") as file:
            file.write(base64_str)

        result = f"""
        Scene captured and base64_str stored in {scene_info_file_path} successfully!!!
        """
    
        return result
    
    except Exception as e:
        result = f"""
        The exception message: {str(e)}
        """
        return result
    
def detect_all_cubes(scene_info_file_path:str) -> str:
    """
    useful for when you need to analyze the scene information to extract the 
    information about cubes present in the scene. You have to use get_scene()
    first to get the scene_info_file_path, or you do not have the data about
    the scene.
    
    goal: find all the cubes from the scene
    
    Output will be the execute status of this tool.
    """
    
    try:
        with open(scene_info_file_path, 'r') as file:
            scene_info_base64_str = file.read()
            
        decoded_bytes = base64.b64decode(scene_info_base64_str)
        decoded_str = decoded_bytes.decode('utf-8')
        decoded_list = ast.literal_eval(decoded_str)
        
        if decoded_list is not None:
            cubes = detect(decoded_list)
            
            cubes_num = len(cubes)
            cubes_str = str(cubes)
                
            result = f"""
            All cubes have been stored successfully.\n 
            Total num of cube(s): {cubes_num}\n
            The information of cubes: {cubes_str}
            """

            return result
        else:
            result = f"""
            Scene information is not available.
            Please ensure you have the data about the scene.
            """
            return result
    except Exception as e:
        result = f"""
        The exception message: {str(e)}
        """
        return result

def get_specific_cube(features: str, cubes_str) -> str:
    """
    useful for when you want to find the specific cube
    Make sure features in cube_str and ensure you have already 
    obtained the scene and all cubes before using this function.
    
    goal: find the specific cube from the scene
    
    Output will be the execute status of this tool.
    """

    cubes_list = ast.literal_eval(cubes_str)
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
    try: 
        
        result = []

        for cube in cubes_list:
            if 'feature' in cube and 'color' in cube['feature']:
                color = cube['feature']['color'].upper()
                if color == target_features:
                    result.append(get_objects_info(cube))
        
        if result:
            result_str = str(result)
            cube_str = str(result_str)
            result = f"""
            Successfully retrieved the specific cube.\n
            {cube_str}
            """

            return result
        else:
            result = f"""
            No cube with the specified features were found.
            """
            return result
    except Exception as e:
        result = f"""
        The exception message: {str(e)}
        """
        return result
    
def pick_up_specific_cube(cube_str:str):
    """
    useful for when you want to pick up the cube after getting the
    information of specific cube.
    
    goal: pick up the specific cubes
    
    Output will be the execute status of this tool.
    """
    try: 
        cube_list = ast.literal_eval(cube_str)

        position = cube_list[0]['position']
        orientation = cube_list[0]['orientation']
        feature = cube_list[0]['feature']

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
    
def place_specific_cube(area_info_x:float, area_info_y:float, cube_str:str):
    """
    useful for when you want to place the cube after picking
    up the cube, then place into the specific area.
    
    goal: place the specific cubes
    
    Output will be the execute status of this tool.
    """
    
    try: 
        cube_list = ast.literal_eval(cube_str)

        position = cube_list[0]['position']
        orientation = cube_list[0]['orientation']
        feature = cube_list[0]['feature']

        place_or_not = franka_place(
            x=area_info_x, y=area_info_y,
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
