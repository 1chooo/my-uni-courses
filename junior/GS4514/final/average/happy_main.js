import { 
    type, 
    filterData,
} from './utilities.js';
import {
    // 不同的set function
    SetHappyPieChart,
    setHappyFirstCanvas,
    setHappyLineChart,
    setEricBarChartCanvas,
    // tooltip的參數
    barcharttooltip,
    linecharttooltip
} from './happy_canvas/set_canvas.js'
import {
    // prepare不同形式的資料
    prepareHappyFirstBarChartData,
    prepareHappyLineChartData,
    prepareHappyPieChart,
    calculatePublisherSales
} from './happy_canvas/prepare_data.js'
import  {
    // 把資料分成5年為一個單位
    divideintofive,
    // 為select增加選項
    addSelect,
    addSelectGenre
} from "./happy_canvas/others.js"


function ready(videoGameData) {
    const videoGameClean = filterData(videoGameData);
    // 讀取資料
    const DataIntoFive = divideintofive(videoGameClean); 
    // array[obj]，其中content的部分是放分類過的資料。
    // obj{start, end, content}


    // 圖表一 顯示特定時間段不同遊戲種類平均收益比較
    // 綁定到div
    let bardiv = document.querySelector('#first-chart'); 
    bardiv.innerHTML = `${barcharttooltip}`;

    // 資料處理，回傳[[obj1],[obj2]]
    // obj1 : {Genre, Avg}
    // obj2 : {origin obj}，找到最大的物件並回傳
    let returnData = prepareHappyFirstBarChartData(DataIntoFive[0].content); 
    let HappyData = returnData[0];
    let maxObj = returnData[1];
    // 建立畫布並顯示
    setHappyFirstCanvas(DataIntoFive[0].content, HappyData,maxObj);
    
    // 建立select並且放到cnavas上面
    let barchartSelect = addSelect(DataIntoFive);
    let barwhere = document.body.querySelector(".select1");
    barwhere.appendChild(barchartSelect);

    // 綁定事件
    barchartSelect.addEventListener("change", function(event){
        let getValue = event.target.value;
        bardiv.innerHTML = `${barcharttooltip}`;
    	let returnData = prepareHappyFirstBarChartData(DataIntoFive[getValue].content); 
    	let HappyData = returnData[0];
    	let maxObj = returnData[1];
    	setHappyFirstCanvas(DataIntoFive[getValue].content, HappyData,maxObj);
    })

    // 圖表一結尾

    // 圖表二 分析不同種類的遊戲在不同間段出現的遊戲數量
    let genres = ['Sports','Platform','Racing','Role-Playing','Puzzle','Misc','Shooter','Simulation','Action','Fighting','Adventure','Strategy'];
    
    // 綁訂到特定div
    let linediv = document.querySelector('#line-chart');    
    linediv.innerHTML = `${linecharttooltip}`;

    // 回傳 [{obj}, [arr]]
    // obj : {Genre, [sub_obj]}
        // sub_obj : {year, count}，該genre在某年的數量計算
    let returnlineData = prepareHappyLineChartData(DataIntoFive);
    let HappyLineChartData = returnlineData[0];
    let maxSaleGameInthisFive = returnlineData[1];
    setHappyLineChart(HappyLineChartData, genres[0],maxSaleGameInthisFive);
    
    // 產生select並綁定
    let linechartselect = addSelectGenre(genres);
    let linewhere = document.body.querySelector(".select2");
    linewhere.appendChild(linechartselect);
    
    // 綁定事件
    linechartselect.addEventListener("change", function(event){
        let getValue = event.target.value;
        linediv.innerHTML = `${linecharttooltip}`;

        setHappyLineChart(HappyLineChartData, genres[getValue],maxSaleGameInthisFive);
    })

    // 圖表三 不同種類的遊戲在不同地區的銷售佔比的百分比較
    // [obj]
    // obj : {Genre, Sales : [arr1], SalesNumber : [arr2]}
    // arr1 : ['JP_Sales', 'NA_Sales', 'EU_Sales', 'Other_Sales']
    // arr2 : [Number1, Number2, Number3, Number4]
    let piechartData = prepareHappyPieChart(videoGameClean);
    SetHappyPieChart(piechartData, 0);
    // 獲得設定好選項的select
    let piechartselect = addSelectGenre(genres);
    // 綁訂到特定div
    let piediv = document.querySelector('#pie-chart');
    // 選定特定的class
    let piewhere = document.body.querySelector(".PutSelectHere");
    piewhere.appendChild(piechartselect);
    // 綁定事件
    piechartselect.addEventListener("change", function(event){
        let getValue = event.target.value;
        piediv.innerHTML = "";
        let HappypieChartData = piechartData;
        SetHappyPieChart(HappypieChartData, getValue);
    })

    // eric pic
    // 取得各發行商在不同地區的銷售量
    const publisherSalesData = calculatePublisherSales(videoGameClean);
  
    const select = d3.select('#region-select');
    const regions = ['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales'];
    
    const regionTable = {
        "NA_Sales": "North America",
        "EU_Sales": "Europe",
        "JP_Sales": "Japan",
        "Global_Sales": "Global",
        "Other_Sales": "Other Region"
    }
    
    select
        .selectAll('option')
        .data(regions)
        .enter()
        .append('option')
        .text(d => d);
    
    setEricBarChartCanvas(publisherSalesData, regions[0]);
  }
// 資料讀取和entry point和data cleaning
d3.csv('./data/Video_Games_Sales_as_at_22_Dec_2016.csv', type).then(
    result => {
        ready(result)
    }
  )
  

