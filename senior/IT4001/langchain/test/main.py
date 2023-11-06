import os
import requests
import openai
from client import capture_image
from agent import get_scene
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

# Create an instance of the CaptureScene tool
tools = []
tools.append(StructuredTool.from_function(get_scene))

# Initialize the agent with the CaptureScene tool
agent = initialize_agent(
    agent='chat-conversational-react-description',
    tools=tools,
    llm=llm,
    verbose=True,
    max_iterations=3,
    early_stopping_method='generate',
    memory=conversational_memory
)

# Run the agent with the initial prompt
agent("Act like the factory operator, now you need to capture the scene.")
