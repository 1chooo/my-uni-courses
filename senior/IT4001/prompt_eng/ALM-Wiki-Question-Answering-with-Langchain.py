# %% [markdown]
# ## Implement a Wiki Question Answering with Tools Application
# - Learning How to Use Langchain Agent to Implement an ALM Application
#     - Reasoning: Build-in Prompt Template
#     - Action: Tool Desciption 
#         - Wiki API
#         - Calculator
# 
# <img src="./imgs/QA_with_tool.PNG" alt="QA with Tools" width="600" height="300" style="float: left; margin-right: 10px;">

# %%
# !pip install langchain
# !pip install openai
# !pip install wikipedia

# %%
# %set_env OPENAI_API_KEY=OPEN_API_KEY

# %%
import os

import langchain
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
from langchain.utilities import WikipediaAPIWrapper
from langchain.agents.tools import Tool
from langchain import LLMMathChain
from langchain.agents import initialize_agent, AgentType

# %%
### set openai api key ###
# os.environ["OPENAI_API_KEY"] = ### put your own key here
###

# %% [markdown]
# ## ALM = LLM + Reasoning + Action

# %% [markdown]
# ### 1. Prepare LLM
# #### [Ref: Chat mode LLM model from Langchain](https://python.langchain.com/docs/modules/model_io/models/chat/)
# #### [Ref: LLM model from Langchain](https://python.langchain.com/docs/modules/model_io/models/llms/)

# %%
### openai model: GPT3.5-Turbo
chat_llm = ChatOpenAI(temperature=0)

### another openai model: text-davinci-003
llm = OpenAI(temperature=0)

# %% [markdown]
# ### 2. Prepare tools
# #### [Ref: Wikipedia tool from Langchain](https://python.langchain.com/docs/modules/agents/tools/integrations/wikipedia)
# #### [Ref: Math tool from Langchain](https://python.langchain.com/docs/modules/chains/additional/llm_math)
# #### [Ref: Tools from Langchain ](https://python.langchain.com/docs/modules/agents/tools/how_to/custom_tools)

# %%
### tool for Wikipedia
wikipedia = WikipediaAPIWrapper()

### for math tool
llm_math_chain = LLMMathChain.from_llm(llm=llm, verbose=True)

# %%
### 
# Define tools you need and relatived information for agent(LLM) to read
# 1. Prepare tool name
# 2. Prepare tool function
# 3. Prepare tool description  
###

###
# method 1: 
###

tools = [
    Tool(
        name = "Wikipedia",
        func=wikipedia.run,
        description="""A wrapper around Wikipedia.\ 
        Useful for when you need to answer general questions about people, places, companies, facts, historical events,\ 
        or other subjects. Input should be a search query."""
    ),
    Tool(
        name="Calculator",
        func=llm_math_chain.run,
        description="useful for when you need to answer questions about math"
    ),
]

# %%
###
# method 2: 
###
# tools = load_tools(["llm-math","wikipedia"], llm=llm)

# %% [markdown]
# ### 3. Prepare build-in component: Agent, which have build-in reasoning prompt template
# #### [Ref: build-in reasoning prompt template - agent, from Langchain](https://python.langchain.com/docs/modules/agents/agent_types/react)

# %%
agent = initialize_agent(tools, llm, agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

# %% [markdown]
# ### 4. Prepare your input  question and run 

# %% [markdown]
# #### Question1. Math only

# %%
question1 = "What is the 25% of 300?"

agent.run(question1)

# %% [markdown]
# #### Question2. Wiki Search only

# %%
question2 = "Who is Leo DiCaprio's girlfriend?"

agent.run(question2)

# %% [markdown]
# #### Question3. Wiki Search and calculate 

# %%
question3 = "Who is Leo DiCaprio's girlfriend? What is her current age raised to the 0.43 power?"

agent.run(question3)

# %%



