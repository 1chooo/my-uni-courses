export function prepareFirstBarChartData(videoGameData) {

    console.log(videoGameData);

    const dataMap = d3.rollup(
        videoGameData,
        v => d3.sum(v, leaf => leaf.Global_Sales), // Sum up the Global_Sales.
        d => d.Genre // categorize the movie with groupby
    );
    const dataArray = Array.from(
        dataMap,
        d => ({ Genre: d[0], Global_Sales: d[1] })
    );

    return dataArray;
}


export function prepareSecondBarChartData(videoGameData) {

    console.log(videoGameData);

    const dataMap = d3.rollup(
        videoGameData,
        v => d3.sum(v, leaf => leaf.Global_Sales), // Sum up the Global_Sales.
        d => d.Platform // categorize the movie with groupby
    );
    const dataArray = Array.from(
        dataMap,
        d => ({ Platform: d[0], Global_Sales: d[1] })
    );

    return dataArray;
}

export function prepareThirdBarChartData(videoGameData) {
    console.log(videoGameData);

    const filteredData = videoGameData.filter(d => d.Platform === "PS2");

    const dataMap = d3.rollup(
        filteredData,
        v => d3.sum(v, leaf => leaf.Global_Sales),
        d => d.Genre
    );

    const dataArray = Array.from(dataMap, d => ({
        Genre: d[0],
        Global_Sales: d[1]
    }));

    return dataArray;
}

export function prepareForthBarChartData(videoGameData) {
    console.log(videoGameData);

    const dataMap = d3.rollup(
        videoGameData,
        v => d3.mean(v, leaf => leaf.User_Score),
        d => d.Genre
    );

    const dataArray = Array.from(dataMap, d => ({
        Genre: d[0],
        User_Score: d[1]
    }));

    return dataArray;
}