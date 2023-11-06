import os
import requests
import openai
import gradio as gr
from TextAgent import TextAgent
from langchain.tools import StructuredTool
from langchain import PromptTemplate
from langchain.callbacks.base import BaseCallbackHandler
from langchain.callbacks import get_openai_callback
from HugoAgent import *
import logging
from typing import Any, Dict

role = """\
You are a cautious individual who divides tasks into smaller ones \
and continuously verifies that you are following the steps. \
Moreover, you select suitable tools to solve problems.
"""

A_area = f"""
Placement Points:
- (X:0.45, Y:0.25)
- (X:0.45, Y:0.15)
- (X:0.55, Y:0.25)
- (X:0.55, Y:0.15)
"""

B_area = f"""
Placement Points:
- (X:0.1, Y:0.45)
- (X:0.1, Y:0.55)
- (X:0.2, Y:0.45)
- (X:0.2, Y:0.55)
"""

def output_html(history):
    step = 1
    html = ''
    html += '<div class="title_block"><h1 class="title">Scenario:</h1></div>'
    html += '<div class="scenario_block"><div class="scenario">{}</div></div>'.format(history["scenario"])
    html += '<div class="actions">'
    for action in history["actions"]:
        html += '<h2 class="step"> Step: {}</h2>'.format(step)
        step += 1
        html += '<div class="action">'
        html += '<div class="thought_block">'
        html += '<div class="thought">Thought: {}</div>'.format(action["function_call"]["thought"])
        html += '<div class="function_call">'
        html += '<div class="function_name">Action: {}</div>'.format(action["function_call"]["function_name"])
        html += '<div class="parameters">'
        parameters = action["function_call"]["parameters"]
        if isinstance(parameters, dict):
            for key, value in parameters.items():
                html += '<div class="parameter">Action Input: {}={}</div>'.format(key, value)
        elif isinstance(parameters, list):
            for item in parameters:
                html += '<div class="parameter">Action Input: {}</div>'.format(str(item))
        else:
            html += '<div class="parameter">Action Input: {}</div>'.format(str(parameters))
        html += '</div>' #class="parameters"
        html += '<div class="return_block"><div class="function_return">Observation: {}</div></div>'.format(str(action["function_return"]))
        html += '</div>' #class="function_call"
        html += '</div>' #class="action"
        html += '</div>' #class="thought"
    html += '</div>' #class="actions"
    html += '<div class="answer_block"><div class="answer">{}</div></div>'.format(history["answer"])
    return html


def get_openai_secret_key(URL, PARAMS) -> str:
    data = requests.get(url=URL, params=PARAMS).json()
    
    return data["openai_secret_key"]

def call_franka(micro_path, file_path, scenario):
    # URL = "http://172.18.212.81:32000/get_openai_secret_key"
    # PARAMS = {'user_name': "Hugo_Lin"}
    # openai.api_key = get_openai_secret_key(URL, PARAMS)
    openai.api_key = "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"

#     try:
#         requests.get("http://localhost:8211/scene_reset")
#     except Exception as e:
#         print("Reset scene failed!")
        
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
        return_intermediate_steps=True,
    )
    
    executor_command_prompt = f"""
{role}
Now your mission is to achieve the {scenario}.
Then you have to follow the steps that you have breaked down to use \
the specific tools then achieve the {scenario}.

The information about A area is {A_area}, and B area is {B_area}

Keep noticing how much cubes you need to pick and place.
    """
    
    print(executor_command_prompt)
    
    with get_openai_callback() as cb:
        response = agent_executor(executor_command_prompt)
        print(cb)
        
#     print(response["intermediate_steps"][0])
    
    actions = []
    for item in response["intermediate_steps"]:
        action = {
            "function_call": {},
            "function_return": ""
        }
        
        action["function_call"]["function_name"] = item[0].tool  
        action["function_call"]["thought"] = item[0].log.split('\n\nAction:')[0].split('Thought:')[-1].strip()
        action["function_call"]["parameters"] = item[0].tool_input  
        action["function_return"] = item[1]
        actions.append(action)

    history = {}
    history["scenario"] = scenario
    history["actions"] = actions
    history["answer"] = response["output"]
#     print(history)
    html = output_html(history)

    return html

def get_examples() -> list:
    examples = [
        [None, None, 'Place the red cubes in Area A, and place the remaining cubes in Area B'],
        [None, None, 'Place the blue cubes in Area B, and place the remaining cubes in Area A'],
        [None, None, 'Place the red cubes in Area B, and place the remaining cubes in Area A'],
        [None, None, 'Place the black cubes in Area A, and place the remaining cubes in Area A'],
        [None, None, 'Without considering colors, half cubes are placed in Area A, and the other half cubes are placed in Area B'],
    ]
    
    return examples

def main() -> None:
    examples = get_examples()

    inputs = [
        gr.Audio(source="microphone", type="filepath"),
        gr.Audio(source="upload", type="filepath"),
        gr.Textbox(type="text", label="Scenario"),
    ]
    
    outputs = [
#         "text",
        gr.HTML(elem_id="container"),
    ]
    
    css = ""
    with open('style.css', 'r') as f:
        css = f.read()
    demo = gr.Blocks(css=css)
    
    # with gr.Blocks(css=css) as demo:
    #     gr.Markdown("""
    #     # LLMs with Isaac Sim Robot by model v0.0.8
        
    #     PEGATRON CORP. 23\" Summer Internship
    #     """)
    #     with gr.Row():
    #         with gr.Column():
    #             # 創建音頻元素
    #             microphone = gr.Audio(source="microphone", type="filepath")
    #             file_path = gr.Audio(source="upload", type="filepath")
    #             scenario = gr.Textbox(type="text", label="Scenario")
            
    #         # 第二個 Column
    #         with gr.Column():
    #             # 添加示例
    #             gr.Examples(
    #                 examples, 
    #                 inputs=[microphone, file_path, scenario],
    #             )
                
    #     # 第二個 Row
    #     with gr.Row():
    #         with gr.Column():
    #             # 創建清除按鈕
    #             clear_btn = gr.Button("Clear")
                
    #             # 當按鈕被點擊時清除輸入和輸出
    #             def clear_button_clicked():
    #                 microphone.clear()
    #                 file_path.clear()
    #                 scenario.clear()
    #             clear_btn.click(clear_button_clicked)
            
    #         with gr.Column():
    #             # 創建運行按鈕
    #             run_btn = gr.Button("Run")
                
    #             # 當運行按鈕被點擊時執行 call_franka 函數
    #             def run_button_clicked():
    #                 return call_franka(
    #                     microphone,
    #                     file_path,
    #                     scenario,
    #                 )
    #             result = run_btn.click(run_button_clicked)
    #     with gr.Row():
    #         with gr.Column():
    #             gr.HTML(result, elem_id="container")

        # with gr.Row():
        #     with gr.Column():
        #         gr.HTML(
        #             outputs=result,
        #             elem_id="container"
        #         ) 
    with demo:
        gr.Interface(
            fn=call_franka, 
            inputs=inputs,
            outputs=outputs,
            examples=examples,
            title="LLMs with Isaac Sim Robot by model v0.0.8",
            description=(
                "PEGATRON CORP. 23\" Summer Internship"
            ),
            allow_flagging="never",
        )

    demo.launch(
        share=True, 
        server_name="0.0.0.0", 
        server_port=6006
    ) 
    
if __name__ == '__main__':
    main()