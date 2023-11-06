import os
import requests
import openai
from agent import *
import langchain
from langchain.tools import StructuredTool
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
import warnings

warnings.filterwarnings("ignore")

URL = "http://172.18.212.81:32000/get_openai_secret_key"
PARAMS = {'user_name': "Hugo_Lin"}

def get_openai_secret_key() -> str:
    data = requests.get(url=URL, params=PARAMS).json()
    return data["openai_secret_key"]

openai.api_key = get_openai_secret_key()

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

global_scene_info = None
gloabe_cubes = None
global_specific_cubes = None

# Create an instance of the CaptureScene tool
tools = [
    StructuredTool.from_function(get_scene),
    StructuredTool.from_function(detect_all_cubes),
    StructuredTool.from_function(get_specific_cubes),
]

# Initialize the agent with the CaptureScene tool
agent_executor = initialize_agent(
    agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    tools=tools,
    llm=llm,
    verbose=True,
    max_iterations=5,
    early_stopping_method='generate',
    memory=conversational_memory
)

scenario = f"""
Place the red blocks in Area A, and place the remaining blocks in Area B.

Ths steps after you break down:
- step1: ...
- step2: ...
- ...
"""

role = f"""
As the Factory Operator, your primary objective is to efficiently navigate through various scenarios and tasks within the factory. Your problem-solving skills will be crucial as you analyze challenges and break them down into manageable tasks. You'll be equipped with a range of tools to tackle the issues at hand, and your ability to utilize these tools wisely will determine the successful completion of your work.

Remember, each tool at your disposal has the potential to solve the problems you encounter. Your expertise and resourcefulness will play a key role in ensuring the smooth and effective functioning of the factory. As the Factory Operator, you will need to think critically and creatively, making informed decisions to achieve optimal results.

Your role requires adaptability and quick thinking, as you may encounter various situations that demand different approaches. Through your actions and problem-solving prowess, you'll contribute significantly to the overall productivity and success of the factory operations. Keep in mind that your proficiency in using the tools and your ability to strategize will be pivotal in accomplishing the tasks efficiently.
"""

# Run the agent with the initial prompt
# agent_executor(f"""
# As the {role} you are, now you need to find the RED cubes \
# and tell me the amount of the RED cubes. Please make sure \
# you have stored the results to the next step.
# """)
agent_executor(f"""
As the {role} you are, now your mission is to finish the {scenario} \
Please show me the steps you have analyzed. You can store the scene in \
{global_scene_info}, store the cubes in {gloabe_cubes}, store the specific \
in {global_specific_cubes} to finish the jobs.
""")
langchain.debug=True

print(global_scene_info)
print(gloabe_cubes)