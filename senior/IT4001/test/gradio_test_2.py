with gr.Blocks(css=css) as demo:
    # 第一個 Row
    with gr.Row():
        with gr.Column():
            # 創建音頻元素
            microphone = gr.Audio(source="microphone", type="filepath")
            file_path = gr.Audio(source="upload", type="filepath")
            scenario = gr.Textbox(type="text", label="Scenario")
        
        # 第二個 Column
        with gr.Column():
            # 添加示例
            examples = gr.Examples()
            examples.add_example(inputs=[microphone, file_path, scenario], outputs=[result])
    
    # 第二個 Row
    with gr.Row():
        with gr.Column():
            # 創建清除按鈕
            clear_btn = gr.Button("Clear")
            
            # 當按鈕被點擊時清除輸入和輸出
            def clear_button_clicked():
                microphone.clear()
                file_path.clear()
                scenario.clear()
                result.clear()
            clear_btn.click(clear_button_clicked)
        
        with gr.Column():
            # 創建運行按鈕
            run_btn = gr.Button("Run")
            
            # 當運行按鈕被點擊時執行 call_franka 函數
            def run_button_clicked():
                call_franka(
                    microphone.get_value(),  # 獲取音頻輸入值
                    file_path.get_value(),   # 獲取文件路徑輸入值
                    scenario.get_value(),    # 獲取情境輸入值
                    result  # 傳遞結果元素用於更新結果
                )
            run_btn.click(run_button_clicked)
    
    # 第三個 Row
    with gr.Row():
        result = gr.HTML(elem_id="container")  # 創建 HTML 元素用於顯示結果