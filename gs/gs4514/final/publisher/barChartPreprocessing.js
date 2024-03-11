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

export function chooseTop15(metric, data) {
    const data_15 = data.sort((a,b) => b[metric] - a[metric]).filter((d,i) => i < 15);
    return data_15;
}

export function PrepareBarChartData(data) {
    let NA_Map = d3.rollup(
        data,
        v => d3.sum(v , leaf => leaf.NA_Sales),
        d => d.Publisher
    )
    let NA = Array.from(NA_Map, d => ({ Publisher: d[0], NA_Sales: d[1] }));
    
    let EU_Map = d3.rollup(
        data,
        v => d3.sum(v , leaf => leaf.EU_Sales),
        d => d.Publisher
    )
    let EU = Array.from(EU_Map, d => ({ Publisher: d[0], EU_Sales: d[1] }));
    
    let JP_Map = d3.rollup(
        data,
        v => d3.sum(v , leaf => leaf.JP_Sales),
        d => d.Publisher
    )
    let JP = Array.from(JP_Map, d => ({ Publisher: d[0], JP_Sales: d[1] }));
    
    let Other_Map = d3.rollup(
        data,
        v => d3.sum(v , leaf => leaf.Other_Sales),
        d => d.Publisher
    )
    let Other = Array.from(Other_Map, d => ({ Publisher: d[0], Other_Sales: d[1] }));
    
    let Global_Map = d3.rollup(
        data,
        v => d3.sum(v , leaf => leaf.Global_Sales),
        d => d.Publisher
    )
    let Global = Array.from(Global_Map, d => ({ Publisher: d[0], Global_Sales: d[1] }));
    
    let dataArray = [];

    for (let i = 0; i < NA.length; i++) {
        dataArray.push(
            {
                ...NA[i],
                ...EU[i],
                ...JP[i],
                ...Other[i],
                ...Global[i]
            }
        );
    }

    return dataArray;
}

