# Online Anonymous Multi-User Message Board

https://github.com/1chooo/socket-programming/assets/94162591/18f5680f-6982-4b40-861d-5a2fa4c3975a



## Initial Setup

```shell
# Frontend with ReactJS
$ mkdir frontend
$ cd frontend
$ npm install -g create-react-app
$ npx create-react-app .
$ yarn add node-sass

# Backend with GO
$ mkdir backend
$ cd backend
$ go mod init github.com/1chooo/socket-programming
$ go get github.com/gorilla/websocket
```

### Frontend Dependencies

```shell
$ npm i @fortawesome/fontawesome-free
$ npm i @fortawesome/fontawesome-svg-core
$ npm install react-syntax-highlighter
```

### 作業要求:
- 每位同學需製作出 TCP or UDP Socket 的程式 (50%/80%) 剩下的30%會是加分項目
- 一分PDF實驗報告，需詳細解釋出程式的功能(20%)
- 不限制任何的程式語言

### 加分項目:
- GUI介面、多Client連接(Multithreading)、Non blocking socket、功能完整、有創意均可加分

### DEMO方式:
- 需自備筆電，若沒有筆電需要跟同學借，助教的電腦不開放Demo
- 來實驗室Demo的時間以及截止時間尚未決定，之後會公布在eeclass
- 助教在Demo時會問問題，這個也會算在評分內
- Demo若有出現問題的話，會被扣分

## License
Released under [MIT](./LICENSE) by [Hugo ChunHo Lin](https://github.com/1chooo).

This software can be modified and reused without restriction.
The original license must be included with any copies of this software.
If a significant portion of the source code is used, please provide a link back to this repository.
