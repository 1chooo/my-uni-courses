from langchain.tools import BaseTool
from client import capture_image
from client import detect
from client import get_objects_info

# The input will be the str type, therefore it might need to rewrite the function

def get_scene() -> bool:
    """
    This function is used to capture the scene by calling an API and check if the scene is successfully obtained.

    Returns: bool: A boolean indicating whether the scene is successfully obtained.
    """
    global global_scene_info
    
    try:
        scene_info = capture_image()
        global_scene_info = scene_info
        
        print(f"Scene captured successfully")

        return True
    
    except Exception as e:
        print(str(e))
        return False

def detect_all_cubes(scene_info) -> bool:
    """
    This function analyzes the provided scene information to detect and extract
    information about cubes present in the scene. However, you have to use get_scene()
    before you detect all the cubes, or you do not have the data about the scene
    
    Params:
        - image: size: 640 x 640 x 3: The scene information containing data about the
          current scene.

    Returns:
        - bool: Returns True if the detection and extraction of cubes from the
          scene information is successful and the cubes have been stored
          globally. Returns False if an error occurs during the process.
    """
    global global_cubes
    
    try:
        if scene_info is not None:
            cubes = detect(scene_info)
            global_cubes = cubes

            print("All cubes have been stored successfully.")
            return True
        else:
            print("Scene information is not available. Please ensure you have the data about the scene.")
            return False
    except Exception as e:
        print(str(e))
        return False
    
def get_specific_cubes(global_cubes, cube_color_to_find) -> bool:
    """
    This function retrieves information about all cubes with the given color from the global list of cubes.
    Therefore, ensure you have already obtained the scene and all cubes before using this function.
    
    Params:
        - global_cubes (list): The global list containing information about all the cubes.
        - cube_color_to_find (str): The color of the specific cubes to retrieve. Only RED, BLUE, GREEN.

    Returns:
        - bool: Returns True if the retrieval of the specific cubes' information is successful and stored
          globally. Returns False if no cubes with the given color are found or an error occurs during the process.
    """
    
    global global_specific_cubes
    
    try:
        if global_cubes is not None:
            specific_cubes = []
            print(global_cubes)
            print(type(global_cubes))
            for cube in global_cubes:
                if cube.get("color") == cube_color_to_find:    # get() cannot use in string
                    specific_cubes.append(get_objects_info(cube))

            if specific_cubes:
                global_specific_cubes = specific_cubes
                print(f"Successfully retrieved information for '{cube_color_to_find}' cubes.")
                return True
            else:
                print(f"No cubes with the color '{cube_color_to_find}' were found.")
                return False
        else:
            print("Scene information is not available. Please ensure you have obtained the data about all the cubes.")
            return False
    except Exception as e:
        print(str(e))
        return False
    
def break_down_tasks(scenario: str) -> list:
    """
    This function is designed to analyze the information about the given scenario, which represents the goal to be achieved. 
    The function returns a list of steps that you need to follow in order to fulfill the specified goal.
    
    Parameters:
        - scenario (str): A description of the scenario, outlining the main mission that needs to be accomplished.
    
    Returns:
        - steps (list): A list containing the sequential steps required to achieve the goal.
    """
    
    break_down_list = []
    
    
    return break_down_list
        