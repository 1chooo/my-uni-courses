import os
import requests
import openai
import langchain
from langchain.tools import StructuredTool
from langchain.callbacks import get_openai_callback
from langchain.chat_models import ChatOpenAI
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain.agents import initialize_agent
from langchain.chains import LLMChain
from langchain.agents import initialize_agent, AgentType, tool, Tool
from langchain.tools import StructuredTool
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import SequentialChain
from langchain import PromptTemplate
from langchain.llms import OpenAI
import warnings
import time
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

def get_openai_secret_key(URL, PARAMS) -> str:
    data = requests.get(url=URL, params=PARAMS).json()
    return data["openai_secret_key"]

def get_agent(openai_key=None):
    URL = "http://172.18.212.81:32000/get_openai_secret_key"
    PARAMS = {'user_name': "Hugo_Lin"}
    openai.api_key = get_openai_secret_key(URL, PARAMS)
    # openai.api_key = "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"
        
    tools = []
    tools = [
        StructuredTool.from_function(detect_all_cubes),
        StructuredTool.from_function(pick_up_specific_cube),
        StructuredTool.from_function(place_specific_cube),
    ]

    llm = ChatOpenAI(
        openai_api_key=openai.api_key,
        temperature=0,
        model_name='gpt-3.5-turbo',
    )
    
    agent_executor = initialize_agent(
        agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
        tools=tools,
        llm=llm,
        verbose=True,
#         return_intermediate_steps=True,
    )
    
    return agent_executor


def get_examples() -> list:
#     [None, '*.wav', 'Scenario', 'lang']
    examples = [
        [None, None, 'Place the red cubes in Area A, and place the remaining cubes in Area B', 'en'],
        [None, None, 'Place the blue cubes in Area B, and place the remaining cubes in Area A.', 'en'],
        [None, None, 'Place the red cubes in Area B, and place the remaining cubes in Area A.', 'en'],
        [None, None, 'Place the black cubes in Area A, and place the remaining cubes in Area A.', 'en'],
        [None, None, 'Without considering colors, half cubes are placed in Area A, and the other half cubes are placed in Area B.', 'en'],
    ]
    
    return examples
