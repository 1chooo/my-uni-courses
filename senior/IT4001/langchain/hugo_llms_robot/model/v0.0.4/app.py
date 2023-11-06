import gradio as gr

def greet(name):
    print(name)
    return "Hello " + name + "!"

with gr.Blocks() as demo:
    gr.Interface(fn=greet, inputs="text", outputs="text")

def launch():
    demo.launch(share=True, server_name="0.0.0.0", server_port=6006)   

if __name__ == "__main__":
    launch()
