import React, { Component } from "react";
import "./Message.scss";

class Message extends Component {
    constructor(props) {
        super(props);
        let temp = JSON.parse(this.props.message);
        this.state = {
            message: temp
        };
    }

    render() {
        const { message } = this.state;
        let messageStyle = {};

        if (message.body === "New User Joined...") {
            messageStyle = {
                color: "#7BAA40",
                fontWeight: "bold"
            };
        } else if (message.body === "User Disconnected...") {
            messageStyle = {
                color: "#9F0047",
                fontWeight: "bold"
            };
        }

        let messageContent;
        if (message.body.startsWith("```") && message.body.endsWith("```")) {
            const codeContent = message.body.substring(3, message.body.length - 3);
            messageContent = <code>{codeContent}</code>;
        } else if (message.body.startsWith("`") && message.body.endsWith("`")) {
            const codeContent = message.body.substring(1, message.body.length - 1);
            messageContent = <code>{codeContent}</code>;
        } else {
            messageContent = message.body;
        }


        return (
            <div className="Message" style={messageStyle}>
                {messageContent}
            </div>
        );
    }
}

export default Message;
