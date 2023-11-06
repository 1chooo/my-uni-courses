from HugoAgent import get_agent, get_examples

break_down_example = f"""
Ths is the example to list the steps after you break down:
- step1: ...
- step2: ...
- ...
"""

role = f"""
You are a cautious individual who divides tasks into smaller ones 
and continuously verifies that you are following the steps. 
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

scenario1 = f"""
Place the red cubes in Area A, and place the remaining cubes in Area B
"""

scenario1_1 = f"""
Place the blue cubes in Area B, and place the remaining cubes in Area A.
"""

scenario1_2 = f"""
Place the red cubes in Area B, and place the remaining cubes in Area A.
"""

scenario1_3 = f"""
Place the black cubes in Area A, and place the remaining cubes in Area A.
"""

scenario2 = f"""
Without considering colors, half cubes are placed in Area A, and the other half cubes are placed in Area B.
"""

executor_command_prompt = f"""
        As the {role} you are, now your mission is to achieve the {scenario1}.
        Then you have to follow the steps that you have breaked down to use 
        the specific tools then achieve the {scenario1}.
        
        The information about A area is {A_area}, and B area is {B_area}.
        
        Keep noticing how much cubes you need to pick and place.
        """

class TextAgent:
    def __init__(self, openai_key=None):
        if openai_key is None:
            openai_key = "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"
        self.openai_key = openai_key
        self.agent_executor = get_agent(self.openai_key)
        

    def __call__(self, scenario):
        response = self.agent_executor(get_prompts(scenario))
        return response
    
    def get_prompts(scenario):
        role = f"""
You are a cautious individual who divides tasks into smaller ones 
and continuously verifies that you are following the steps. 
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

        executor_command_prompt = f"""
        As the {role} you are, now your mission is to achieve the {scenario}.
        Then you have to follow the steps that you have breaked down to use 
        the specific tools then achieve the {scenario}.
        
        The information about A area is {A_area}, and B area is {B_area}.
        
        Keep noticing how much cubes you need to pick and place.
        """
        return executor_command_prompt
    
    def get_examples(self):
        examples = get_examples()
        return examples
