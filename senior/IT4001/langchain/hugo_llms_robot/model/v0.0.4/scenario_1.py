import os
import requests
import openai
from MyTools import *
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

warnings.filterwarnings("ignore")

URL = "http://172.18.212.81:32000/get_openai_secret_key"
PARAMS = {'user_name': "Hugo_Lin"}

def get_openai_secret_key(URL, PARAMS) -> str:
    data = requests.get(url=URL, params=PARAMS).json()
    return data["openai_secret_key"]

openai.api_key = get_openai_secret_key(URL, PARAMS)

# Initialize LLM (we use ChatOpenAI because we'll later define a `chat` agent)
llm = ChatOpenAI(
    openai_api_key=openai.api_key,
    temperature=0,
    model_name='gpt-3.5-turbo'
)

# Initialize conversational memory
conversational_memory = ConversationBufferWindowMemory(
    memory_key='chat_history',
    k=5,
    return_messages=True
)

# Create an instance of the CaptureScene tool
tools = [
    StructuredTool.from_function(get_scene),
    StructuredTool.from_function(detect_all_cubes),
    StructuredTool.from_function(get_specific_cube),
    StructuredTool.from_function(pick_up_specific_cube),
    StructuredTool.from_function(place_specific_cube),
]

# Initialize the agent with the CaptureScene tool
agent_executor = initialize_agent(
    agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    tools=tools,
    llm=llm,
    verbose=True,
)

break_down_example = f"""
Ths is the example to list the steps after you break down:
- step1: ...
- step2: ...
- ...
"""

cubes_list_example = f"""
1. Cube 1:
   - Position: ...
   - Color: ...

2. Cube 2:
   - Position: 
   - Color: ...
   
3. ...
"""

role = f"""
You are a cautious individual who divides tasks into smaller ones 
such as {break_down_example}
and continuously verifies that you are following the steps. 
Moreover, you select suitable tools to solve problems.
"""

A_area = f"""
Boundary:
- (X:0.3, Y:0.65)
- (X:0.3, Y:0.35)
- (X:0, Y:0.65)
- (X:0, Y:0.35)
Center:
- (X:0.15, Y:0.5)
"""
B_area = f"""
Boundary:
- (X:0.65, Y:0.35)
- (X:0.35, Y:0.35)
- (X:0.35, Y:0.05)
- (X:0.65, Y:0.05)
Center:
- (X:0.5, Y:0.2)
"""

scenario1 = f"""
Place the red cubes in Area A, and place the remaining cubes in Area B.
"""

start_time = time.time()

# langchain.debug=True

with get_openai_callback() as cb:
    agent_executor(
        f"""
        As the {role} you are, now your mission is to achieve the {scenario1} \
        Then you have to follow the steps that you have breaked down to use 
        the specific tools then achieve the {scenario1}.
        The information about A area is {A_area}, and B area is {B_area}. \
        Keep noticing how much cubes you need to pick and place.
        """
    )
    print(cb)

print(f"Total second(s) used: {time.time() - start_time}")
