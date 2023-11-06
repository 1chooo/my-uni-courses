from langchain.tools import BaseTool
from client import *
import base64
import json
import ast

def detect_all_cubes(scene_info_file_path: str) -> str:
    """
    Useful for when you need to analyze the scene information
    to extract details about the cubes present. 

    goal: find all the cubes from the scene

    Output will be the execute status of this tool.
    """

    try:
        scene_info = capture_image()
        print(f'''
        Get Image Successfully and Ready to detect all cubes!!! 
        ''')
        json_str = json.dumps(scene_info)
        base64_str = base64.b64encode(json_str.encode()).decode()
        decoded_bytes = base64.b64decode(base64_str)
        decoded_str = decoded_bytes.decode("utf-8")
        decoded_list = ast.literal_eval(decoded_str)

        real_cubes = []

        if decoded_list is not None:
            cubes = detect(decoded_list)
            for cube in cubes:
                real_cubes.append(get_object_info(cube))

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

    goal: pick up the specific cube

    Output will be the execute status of this tool.
    """
    try:
        position = specific_cube["position"]
        orientation = specific_cube["orientation"]
        feature = specific_cube["feature"]

        pick_or_not = franka_pick(
            position[0],
            position[1],
            position[2],
            orientation[0],
            orientation[1],
            orientation[2],
            orientation[3],
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

    goal: place the specific cube

    Output will be the execute status of this tool.
    """

    try:
        position = specific_cube["position"]
        orientation = specific_cube["orientation"]
        feature = specific_cube["feature"]

        place_or_not = franka_place(
            area_info_x,
            area_info_y,
            position[2],
            orientation[0],
            orientation[1],
            orientation[2],
            orientation[3],
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
