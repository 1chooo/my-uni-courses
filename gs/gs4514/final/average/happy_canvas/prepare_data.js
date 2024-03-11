export function prepareHappyFirstBarChartData(videoGameData) {
    // 輸入{origin_obj}, 輸出這些origin_obj裡面的平均銷售額跟分類，以及每個種類銷售額最好的遊戲
    let ArrayData = [];
    let dif_genre = [];
    for (let i = 0;i < videoGameData.length; i++){
        let name = videoGameData[i]['Genre'];
        if (dif_genre.includes(name)){
            ArrayData[dif_genre.indexOf(name)]["Count"] += 1;
            ArrayData[dif_genre.indexOf(name)]["Sales"] += videoGameData[i]['Global_Sales'];
        } else {
            let obj = {"Genre":name, "Count":1, "Sales":0, "Avg":0};
            obj["Count"] = videoGameData[i]['Counting'];
            obj["Sales"] = videoGameData[i]['Global_Sales'];
            ArrayData.push(obj);
            dif_genre.push(name);
        }
    }
    
    // 這裡把銷售額的單位從百萬變成一千(不然平均的時候除不了)
    for (let i = 0; i < ArrayData.length; i++){
        ArrayData[i]["Avg"] = ArrayData[i]["Sales"]  * 1000 / ArrayData[i]["Count"];
    }
    const dataMap = d3.rollup(
        ArrayData,
        v => d3.sum(v, leaf=>leaf.Avg),
        d => d.Genre
    )
    const dataArray = Array.from(
        dataMap,
        d => ({ Genre: d[0], Avg: d[1] })
    ).sort((a, b)=>{
        return d3.descending(a.Avg, b.Avg);
    });

    // 尋找最大值
    const dA = videoGameData.sort((a,b)=>{
        return d3.descending(a.Global_Sales,b.Global_Sales);
    });
    let maxObj = [];
    let genres = [];
    // 由於前面已經排序過了，所以每個種類第一次出現的遊戲的銷售最大值就是該種類的銷售最大的遊戲
    for (let i = 0;i < dA.length; i++){
    	if (genres.includes(dA[i].Genre)) {
      		if (maxObj[genres.indexOf(dA[i].Genre)].Global_Sales < dA[i].Global_Sales){
          	maxObj[genres.indexOf(dA[i].Genre)].Global_Sales = dA[i].Global_Sales;
            maxObj[genres.indexOf(dA[i].Genre)].which = dA[i];
          }
      } else {
      	let obj = {Genre:dA[i].Genre, Global_Sales:dA[i].Global_Sales, which:dA[i]};
        genres.push(dA[i].Genre);
        maxObj.push(obj);
      }
    }
    return [dataArray,maxObj];
    
}



export function prepareHappyLineChartData(DataIntoFive) {
    // 讀進{origin_obj}，每個種類每年的數量統計
    let genres = ['Shooter','Role-Playing','Puzzle','Platform','Racing','Sports','Misc','Fighting','Action','Simulation','Adventure','Strategy'];
    let consequence = {};
    var maxSaleGameInthisFive =[];
    for (let i = 0;i < genres.length; i++){
        let arr = [];
        let currentGenre = genres[i];
        for (let j = 0;j < DataIntoFive.length; j++){
            let count = 0; 
            for (let z = 0; z < DataIntoFive[j].content.length; z++){
                if (DataIntoFive[j].content[z]['Genre'] == currentGenre) {
                    count += 1;
                }
            }
            let obj = {year: `${1980+5*j}`, count:count};
            arr.push(obj);
        }
        consequence[currentGenre] = arr;
    }
    for(let i = 0 ; i <DataIntoFive.length; i++)
    {
        const dB = DataIntoFive[i].content.sort((a,b)=>{
            return d3.descending (a.Global_Sales,b.Global_Sales);
        }) //五年內最賺錢的遊戲排行
        maxSaleGameInthisFive.push(dB[0]);
    }

    return [consequence,maxSaleGameInthisFive];
}

export function prepareHappyPieChart(videoGameData){
    // 先用總和的資料來做分布
    let ArrayData = [];
    let dif_genre = [];
    let Sales = ["JP_Sales", "NA_Sales", "EU_Sales", "Other_Sales"];
    for (let i = 0;i < videoGameData.length; i++){
        let name = videoGameData[i]['Genre'];
        if (dif_genre.includes(name)){
            ArrayData[dif_genre.indexOf(name)].SalesNumber[0] += videoGameData[i]['JP_Sales'];
            ArrayData[dif_genre.indexOf(name)].SalesNumber[1] += videoGameData[i]['NA_Sales'];
            ArrayData[dif_genre.indexOf(name)].SalesNumber[2] += videoGameData[i]['EU_Sales'];
            ArrayData[dif_genre.indexOf(name)].SalesNumber[3] += videoGameData[i]['Other_Sales'];
            
        } else {
            let obj = {"Genre":name, Sales, SalesNumber:[]};
            obj.SalesNumber.push(videoGameData[i]["EU_Sales"]);
            obj.SalesNumber.push(videoGameData[i]["NA_Sales"]);
            obj.SalesNumber.push(videoGameData[i]["JP_Sales"]);
            obj.SalesNumber.push(videoGameData[i]["Other_Sales"]);
            ArrayData.push(obj);
            dif_genre.push(name);
        }
    }
    for (let i = 0;i < ArrayData.length; i++){
        ArrayData[i].SalesNumber = ArrayData[i].SalesNumber.map((k)=>{return parseInt(k);});
    }
    // 回傳一個 [{種類, 地區銷售額1, 地區銷售額2...}]的資料
    return ArrayData;
}


export function calculatePublisherSales(videoGameClean) {
  const publisherSalesData = [];

  // 使用 d3.group 依發行商分組
  const publishers = d3.group(videoGameClean, d => d.Publisher);

  publishers.forEach((games, publisher) => {
    const totalSales = {
      publisher: publisher,
      NA_Sales: d3.sum(games, d => d.NA_Sales),
      EU_Sales: d3.sum(games, d => d.EU_Sales),
      JP_Sales: d3.sum(games, d => d.JP_Sales),
      Other_Sales: d3.sum(games, d => d.Other_Sales)
    };

    // 統計遊戲款數
    const gameCount = games.length;

    // 計算平均銷售量
    const averageSales = {
      publisher: publisher,
      NA_Sales: totalSales.NA_Sales / gameCount,
      EU_Sales: totalSales.EU_Sales / gameCount,
      JP_Sales: totalSales.JP_Sales / gameCount,
      Other_Sales: totalSales.Other_Sales / gameCount
    };

    publisherSalesData.push(averageSales);
  });

  // 回傳處理過的資料

  return publisherSalesData;
}
  