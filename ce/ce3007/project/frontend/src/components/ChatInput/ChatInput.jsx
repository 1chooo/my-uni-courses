import React, { Component } from "react";
import "./ChatInput.scss";

class ChatInput extends Component {
    handleKeyDown = (event) => {
        if (event.key === "Enter" && !event.shiftKey) {
            // 如果按下的是 Enter 鍵，並且沒有按下 Shift 鍵，觸發發送事件
            event.preventDefault(); // 防止 Enter 預設行為（提交表單）
            this.props.send(event);
        }
    };
    
    render() {
        return (
            <div className="ChatInput">
                {/* <input onKeyDown={this.handleKeyDown} placeholder="Type a message... Hit Enter to Send 🔥"/> */}
                <textarea
                    onKeyDown={this.handleKeyDown}
                    placeholder="Type a message... Hit Enter to Send 🔥"
                />
            </div>
        );
    }
}

export default ChatInput;
