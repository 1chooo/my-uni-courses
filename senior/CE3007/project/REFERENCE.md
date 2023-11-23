# Reference


## Go 

- [Computer Networking: a Top Down Approach](https://gaia.cs.umass.edu/kurose_ross/index.php)
- [Socket 程式設計](https://willh.gitbook.io/build-web-application-with-golang-zhtw/08.0/08.1)
- [Create A Real Time Chat App With Golang, Angular, And Websockets](https://www.thepolyglotdeveloper.com/2016/12/create-real-time-chat-app-golang-angular-2-websockets/)
- Building a Chat Application in Go with ReactJS
  - [Part 1: Initial Setup](https://tutorialedge.net/projects/chat-system-in-go-and-react/part-1-initial-setup/)
  - [Part 2: Simple Communication](https://tutorialedge.net/projects/chat-system-in-go-and-react/part-2-simple-communication/)
  - [Part 3: Designing our Frontend](https://tutorialedge.net/projects/chat-system-in-go-and-react/part-3-designing-our-frontend/)
  - [Part 4: Handling Multiple Clients](https://tutorialedge.net/projects/chat-system-in-go-and-react/part-4-handling-multiple-clients/)
  - [Part 5: Improving the Frontend](https://tutorialedge.net/projects/chat-system-in-go-and-react/part-5-improved-frontend/)
  - [Part 6: Dockerizing your Backend](https://tutorialedge.net/projects/chat-system-in-go-and-react/part-6-dockerizing-your-backend/)


## React

- [Complete Remove/Uninstall node form mac OS](https://dev.to/whovishnu/complete-removeuninstall-node-form-mac-os-1kln)
- [yarn: command not found error [Solved]](https://bobbyhadz.com/blog/npm-command-not-found-yarn)


```jsx
import React, { Component } from "react";
import "./Message.scss";

const animalNames = [
    "海鷗", "鴿子", "鶴", "老鷹", "麻雀", "燕子", "天鵝", "鵝", "啄木鳥", "鸚鵡", "烏鴉", "金絲雀", "紅鶴", "貓", "孔雀", "企鵝", "雞", "火雞", "鴨子", "黑面琵鷺", "美洲豹", "花豹", "雲豹", "石虎", "印度豹", "獵豹", "獅子", "老虎", "獾", "豬", "公豬", "熊", "浣熊", "棕熊", "灰熊", "北極熊", "鬣狗", "海豹", "海象", "海狗", "海獅", "水獺", "水豚", "鹿", "麋鹿", "馴鹿", "梅花鹿", "斑馬", "大象", "長頸鹿", "羚羊", "山羊", "綿羊", "羊駝", "草泥馬", "河馬", "袋鼠", "無尾熊", "天竺鼠", "倉鼠", "老鼠", "松鼠", "公牛", "母牛", "水牛", "犀牛", "小狗", "小貓", "兔子", "野兔", "狼", "雪貂", "穿山甲", "食蟻獸", "狐狸", "狐濛", "猴子", "大猩猩", "黑猩猩", "蝙蝠", "刺蝟", "鴨嘴獸", "土撥鼠", "驢子", "馬", "駱駝", "臭鼬", "熊貓", "馬來膜", "長臂猿", "鱷魚", "短吻鱷魚", "蛇", "眼鏡蛇", "大蟒蛇", "烏龜", "青蛙", "蟾蜍", "變色龍", "壁虎", "蜥蜴", "烏賊", "章魚", "鮪魚", "鮭魚", "牡蠣", "蛤蠣", "金魚", "蝦子", "螃蟹", "龍蝦", "魟魚", "扇貝", "鯨魚", "海馬", "水母", "海豚", "鯊魚", "蝴蝶", "毛毛蟲", "蜜蜂", "蚊子", "蒼蠅", "螞蟻", "蟑螂", "蜈蚣", "蜘蛛", "蠍子"
];

class Message extends Component {
    constructor(props) {
        super(props);
        let temp = JSON.parse(this.props.message);
        this.state = {
            message: {
                ...temp,
                username: this.getRandomAnimalName() // 在初始化時設置初始的動物名稱
            }
        };
    }

    getRandomAnimalName() {
        const randomIndex = Math.floor(Math.random() * animalNames.length);
        return animalNames[randomIndex];
    }

    render() {
        const { message } = this.state;
        let messageStyle = {};

        if (message.body === "New User Joined...") {
            messageStyle = { 
                color: "#7BAA40",
                fontWeight: "bold"
            };
            message.body = message.username + " Joined...";
        }
        else if (message.body === "User Disconnected...") {
            messageStyle = { 
                color: "#9F0047",
                fontWeight: "bold"
            };
            message.body = message.username + " " + message.body;
        }

        return (
            <div className="Message" style={messageStyle}>
                {message.body}
            </div>
        );
    };
}

export default Message;
```