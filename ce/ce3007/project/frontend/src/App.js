import React, { Component } from "react";
import "./App.css";
import { connect, sendMsg } from "./api";
import Header from './components/Header/Header';
import ChatHistory from './components/ChatHistory/ChatHistory';
import ChatInput from './components/ChatInput/ChatInput';
import Footer from "./components/Footer/Footer";

class App extends Component {
	constructor(props) {
		super(props);
		this.state = {
			chatHistory: []
		}
	}

	componentDidMount() {
		connect((msg) => {
			console.log("New Message")
			this.setState(prevState => ({
				chatHistory: [...this.state.chatHistory, msg]
			}))
			console.log(this.state);
		});
	}

	send(event) {
		if (event.keyCode === 13) {		// Enter key
			sendMsg(event.target.value);
			event.target.value = "";
		}
	}

	render() {
		return (
			<div>
				<div className="App">
					<Header />
					<ChatHistory chatHistory={this.state.chatHistory} />
					<br />
					<ChatInput send={this.send} />
					<br />
				</div>

				<div>
					<Footer/>
				</div>
			</div>
		);
	}
}

export default App;

