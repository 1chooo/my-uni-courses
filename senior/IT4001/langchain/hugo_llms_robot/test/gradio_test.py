import gradio as gr

def greet(name):
    return "Hello " + name + "!"

demo = gr.Interface(fn=greet, inputs="text", outputs="text")
    
demo.launch(enable_queue=False, server_name="0.0.0.0", server_port=6006)   
