from langchain.tools import BaseTool
from client import *
import base64
import json
import ast

def get_scene() -> str:
    """
    useful for the first when you need to capture the scene information
    
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
    Useful for when you need to analyze the scene information 
    to extract details about the cubes present. To access the 
    scene data, you must first utilize get_scene() to obtain 
    the scene_info_file_path; otherwise, you won't have the 
    necessary scene data.
    
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
    
def pick_up_specific_cube(specific_cube: dict):
    """
    useful for when you want to pick up the specific cube. 
    You have to realize which cube to pick first.
    
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
