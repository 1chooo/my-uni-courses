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
        
        real_cubes = []
        
        if decoded_list is not None:
            cubes = detect(decoded_list)
            for cube in cubes:
                real_cubes.append(get_objects_info(cube))
            
            cubes_num = len(real_cubes)
            cubes_str = str(real_cubes)
                
            result = f"""
            All cubes have been stored successfully.\n 
            Total num of cube(s): {cubes_num}\n
            The information of cubes: {real_cubes}
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

def get_specific_cube(features: str, real_cubes: list) -> str:
    """
    useful for when you want to find the specific cube.
    Make sure type of features in real_cubes and ensure you have already 
    obtained the scene and all cubes before using this function.
    
    example of features:
    - color=COLOR_NAME
    - color:COLOR_NAME
    
    goal: find the specific cube from the scene
    
    Output will be the execute status of this tool.
    """
    
    try: 
        if not features.strip():
            raise ValueError("Features cannot be an empty string.")
        
        color_value = None
        if features.startswith('color='):
            color_value = features.split('=', 1)[-1]
        elif features.startswith('color:'):
            color_value = features.split(':', 1)[-1]
        else:
            raise ValueError(f"""
            Invalid features format: {features}
            
            Features should be in one of the following formats:
            - color=COLOR_NAME
            - color:COLOR_NAME
            """
            )

        target_features = color_value.upper()
                    
        specific_cube = None
        color = None

        for cube in real_cubes:
            if 'feature' in cube and 'color' in cube['feature']:
                color = cube['feature']['color'].upper()
                if color == target_features:
                    specific_cube = cube
                    break

        if specific_cube:
            result = f"""
            Successfully retrieved the {color} cube.\n
            {specific_cube}
            """
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
    
def pick_up_specific_cube(specific_cube: dict):
    """
    useful for when you want to pick up the cube after getting the
    information of specific cube.
    
    goal: pick up the specific cubes
    
    Output will be the execute status of this tool.
    """
    try: 

        position = specific_cube['position']
        orientation = specific_cube['orientation']
        feature = specific_cube['feature']

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
    
def place_specific_cube(area_info_x: float, area_info_y: float, specific_cube: dict):
    """
    useful for when you want to place the cube after picking
    up the cube, then place into the specific area.
    
    goal: place the specific cubes
    
    Output will be the execute status of this tool.
    """
    
    try: 

        position = specific_cube['position']
        orientation = specific_cube['orientation']
        feature = specific_cube['feature']

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
