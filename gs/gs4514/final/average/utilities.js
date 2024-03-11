export function countColumnTypes(data, columnName) {

    const types = d3.group(data, d => d[columnName]);
    console.log(`${columnName} types: ${types.size}`);
    types.forEach((value, key) => {
        console.log(`- ${key}`);
    });
}

export function formatTicks(d){ 
    
    return d3.format('~s')(d) 
        .replace('M','mil') 
        .replace('G','bil') 
        .replace('T','tri')
}

const parseNA = string => (string === '' ? undefined : string);
const parseDate = string => d3.timeParse('%Y-%m-%d')(string);

export function type(d) {

    const date = parseDate(d.release_date);

    return {
        Name: d.Name.trim(),
        Platform: d.Platform.trim(),
        Year_of_Release: +d.Year_of_Release,
        // Genre: d.Genre.trim(),
        Genre: parseNA(d.Genre),
        Publisher: d.Publisher.trim(),
        NA_Sales: parseFloat(d.NA_Sales),
        EU_Sales: parseFloat(d.EU_Sales),
        JP_Sales: parseFloat(d.JP_Sales),
        Other_Sales: parseFloat(d.Other_Sales),
        Global_Sales: parseFloat(d.Global_Sales),
        Critic_Score: parseFloat(d.Critic_Score),
        Critic_Count: parseFloat(d.Critic_Count),
        User_Score: parseFloat(d.User_Score),
        User_Count: parseFloat(d.User_Count),
        Developer: d.Developer.trim(),
        Rating: parseFloat(d.Rating),
        // 增加一個變數用來等等計算電玩數量(資料本身沒有的)
        Counting: 1,
    }
}

export function filterData(videoGameData) {

    // console.log(typeof (videoGameData))       // object

    return videoGameData.filter(
        d => {
            return (
                // we want to observe the data in ten years 
                // 有記錄的資料都抓取下來
                d.Global_Sales > 0 &&
                d.Platform &&
                d.Name
            );
        }
    );
}