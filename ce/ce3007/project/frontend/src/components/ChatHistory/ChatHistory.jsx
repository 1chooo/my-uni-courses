import React, { Component, createRef } from "react";
import "./ChatHistory.scss";
import Message from '../Message/Message';

class ChatHistory extends Component {
    constructor(props) {
        super(props);
        this.chatHistoryRef = createRef();
    }

    componentDidMount() {
        this.scrollToBottom();
    }

    componentDidUpdate(prevProps) {
        if (prevProps.chatHistory.length !== this.props.chatHistory.length) {
            this.scrollToBottom();
        }
    }

    scrollToBottom() {
        if (this.chatHistoryRef.current) {
            this.chatHistoryRef.current.scrollTop = this.chatHistoryRef.current.scrollHeight;
        }
    }

    render() {
        const messages = this.props.chatHistory.map(
            (msg, index) => <Message key={index} message={msg.data} />
        );

        return (
            <div className='ChatHistory' style={{ height: "310px", overflowY: "auto" }} ref={this.chatHistoryRef}>
                {messages}
            </div>
        );
    }
}

export default ChatHistory;
