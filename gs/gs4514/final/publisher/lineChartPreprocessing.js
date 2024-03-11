let lineColor = {
    "NA_Sales": "#379CA9",
    "EU_Sales": "#44D3DD",
    "JP_Sales": "#FF99AA",
    "Global_Sales": "#FFA07A",
    "Other_Sales": "#F2D091"
}

export function formatTicks(d){ 
    
    return d3.format('~s')(d)
        .replace(d, `${d} mil`)
        .replace('k',' bil')
}

const parseNA = string => (string === '' ? undefined : string);
const parseDate = string => d3.timeParse('%Y-%m-%d')(string);

export function type(d) {
    const date = parseDate(d.release_date);

    return {
        Name: d.Name.trim(),
        Platform: d.Platform.trim(),
        Year_of_Release: +d.Year_of_Release,
        Genre: parseNA(d.Genre),
        Publisher: d.Publisher.trim(),
        // 遊戲銷售量（單位 百萬份）
        NA_Sales: parseFloat(d.NA_Sales),
        EU_Sales: parseFloat(d.EU_Sales),
        JP_Sales: parseFloat(d.JP_Sales),
        Other_Sales: parseFloat(d.Other_Sales),
        Global_Sales: parseFloat(d.Global_Sales),
        // 遊戲評分
        Critic_Score: parseFloat(d.Critic_Score),
        Critic_Count: parseFloat(d.Critic_Count),
        User_Score: parseFloat(d.User_Score),
        User_Count: parseFloat(d.User_Count),
    }
}

export function filterData(videoGameData) {
    return videoGameData.filter(
        d => {
            return (
                d.Global_Sales > 0 &&
                d.Platform && 
                d.Publisher &&
                d.Year_of_Release > 1980 &&
                d.Name
            );
        }
    );
}

function filterDataByPublisher(data , publisher) {
    return data.filter(
        d => {
            return d.Publisher == publisher;
        }
    )
}

function filterEmptyYear(data) {
    return data.filter(
        d => {
            return d[1] > 0;
        }
    )
}

export function prepareLineChartData(data , region , publisher) {
    
    const filterPublisherData = filterDataByPublisher(data , publisher);

    const groupByYear = d => d.Year_of_Release;

    let sumOfSales = 0;
    if (region == "NA_Sales") {
        sumOfSales = values => d3.sum(values , d => d.NA_Sales);
    }
    else if (region == "EU_Sales") {
        sumOfSales = values => d3.sum(values , d => d.EU_Sales);
    }
    else if (region == "JP_Sales") {
        sumOfSales = values => d3.sum(values , d => d.JP_Sales);
    }
    else if (region == "Global_Sales") {
        sumOfSales = values => d3.sum(values , d => d.Global_Sales);
    }
    else if (region == "Other_Sales") {
        sumOfSales = values => d3.sum(values , d => d.Other_Sales);
    }
    
    // 依年份加總銷量
    const sumOfSalesByYear = d3.rollup(filterPublisherData , sumOfSales , groupByYear);
    
    // 排序且濾掉沒有銷量的年分
    const salesArray = filterEmptyYear(Array.from(sumOfSalesByYear).sort((a,b)=>a[0]-b[0]));
    console.log("salesArray",salesArray);
    
    const parseYear = d3.timeParse('%Y');
    const dates = salesArray.map(d => parseYear(d[0]));
    

    // 找最大值
    const salesArray2 = salesArray.map(d => d[1]);
    const yMax = d3.max(salesArray2);
    
    // 最終資料回傳
    let lineData = {
        salesArray: salesArray,
        series:[
            {
                name: region,
                color: lineColor[region],
                values: salesArray.map(d => ({date:parseYear(d[0]),value:d[1]}))
            }
        ],
        dates: dates,
        yMax: yMax
    }
    
    return lineData;
}