from langchain.tools import BaseTool
from client import capture_image

def get_scene(input_data:str) -> bool:
    """
    This function is used to capture the scene by calling an API and check if the scene is successfully obtained.

    Returns:
        Tuple[bool, str or None]: A tuple containing a boolean indicating whether the scene is successfully obtained,
                                  and a string message describing the scene if obtained, or None if not obtained.
    """
    global global_scene_info
    
    try:
        scene_info = capture_image()
        global_scene_info = scene_info
        
        print(f"Scene captured successfully{input_data}")
        return True
    
    except Exception as e:
        print(str(e))
        return False
