import {
    formatTicks,
    type,
    filterData,
    chooseTop15,
    removeGlobalSales,
    PrepareBarChartData,
} from "./stackBarChartPreprocessing.js";

// RWD
function drawStackBarChart(data) {
    // 刪除原本的svg.charts，重新渲染改變寬度的svg
    d3.select(".test-stack-bar-chart-container svg").remove();

    const rwdSvgWidth = 1700;
    const rwdSvgHeight = 1000;
    const margin = 25;
    const marginBottom = 100;

    const svg = d3
        .select(".test-stack-bar-chart-container")
        .append("svg")
        .attr("preserveAspectRatio", "xMidYMid meet")
        .attr("viewBox", `0 0 ${rwdSvgWidth} ${rwdSvgHeight}`)
        .append('g')
        .attr("transform", `translate(${margin},${margin})`);

    // map 資料集
    const xData = data.map((i) => i["Publisher"]);
    const subgroups = Object.keys(data[0]).slice(1);

    // 設定要給 X 軸用的 scale 跟 axis
    const xScale = d3
        .scaleBand()
        .domain(xData)
        .range([margin*2, rwdSvgWidth - margin]) // 寬度
        // .rangeRound([0, rwdSvgWidth-margin*2])
        .padding(0.5);

    const xAxis = d3.axisBottom(xScale);

    // 呼叫繪製x軸、調整x軸位置
    const xAxisGroup = svg
        .append("g")
        .style("font-size", "0.5em")
        .call(xAxis)
        .attr("transform", `translate(0,${rwdSvgHeight - marginBottom})`);

    // 設定要給 Y 軸用的 scale 跟 axis
    const yScale = d3
        .scaleLinear()
        .domain([0, 1800])
        .range([rwdSvgHeight - marginBottom, margin])
        .nice(); // 補上終點值

    const yAxis = d3.axisLeft(yScale).ticks(5).tickSize(3).tickFormat(formatTicks);

    // 呼叫繪製y軸、調整y軸位置
    const yAxisGroup = svg
        .append("g")
        .style("font-size", "0.8em")
        .call(yAxis)
        .attr("transform", `translate(${margin * 2},0)`);

    // 用 d3.stack() 把資料堆疊起來
    const stackedData = d3.stack().keys(subgroups)(data);
    // console.log(stackedData)

    // 設定不同 subgorup bar的顏色
    const color = d3
        .scaleOrdinal()
        .domain(subgroups)
        .range(["#379CA9", "#44D3DD", "#FF99AA", "#F2D091"]);

    // 開始建立長條圖
    const bar = svg
        .append("g")
        .selectAll("g")
        .data(stackedData)
        .join("g")
        .attr("fill", (d) => color(d.key))
        .selectAll("rect")
        .data((d) => d)
        .join("rect")
        .attr("x", (d) => xScale(d.data["Publisher"]))
        .attr("y", (d) => yScale(d[1]))
        .attr("height", (d) => yScale(d[0]) - yScale(d[1]))
        .attr("width", xScale.bandwidth())
        .style("cursor", "pointer")
        .on("mouseover", handleMouseOver)
        .on("mouseleave", handleMouseLeave);

    // 設定文字標籤
    const textTag = svg
        .append("text")
        .attr("class", "infoText")
        .style("fill", "#000")
        .style("font-size", "18px")
        .style("font-weight", "bold")
        .style("text-anchor", "middle")
        .style("opacity", "0");

    function handleMouseOver(d, i) {
        const pt = d3.pointer(event, svg.node());

        d3.select(this).style("opacity", "0.5");

        // 加上文字標籤
        textTag
            .style("opacity", "1")
            .attr("x", pt[0])
            .attr("y", pt[1] - 20)
            .text(formatTicks(Math.round(d.target.__data__[1]) - Math.round(d.target.__data__[0])));
    }

    function handleMouseLeave() {
        d3.select(this).style("opacity", "1");

        textTag.style("opacity", "0");
    }

    // 加上辨識標籤
    const tagsWrap = svg
        .append("g")
        .selectAll("g")
        .attr("class", "tags")
        .data(subgroups)
        .enter()
        .append("g");

    if (window.innerWidth < 780) {
        tagsWrap.attr("transform", "translate(-70,0)");
    }

    tagsWrap
        .append("rect")
        .attr("x", (d, i) => (i) * marginBottom * 2 + 110)
        .attr("y", rwdSvgHeight - marginBottom / 1.5)
        .attr("width", 20)
        .attr("height", 20)
        .attr("fill", (d) => color(d));

    const regionTable = {
        "NA_Sales": "North America",
        "EU_Sales": "Europe",
        "JP_Sales": "Japan",
        "Global_Sales": "Global",
        "Other_Sales": "Other Region"
    }

    tagsWrap
        .append("text")
        .attr("x", (d, i) => (i) * marginBottom * 2 + 140)
        .attr("y", rwdSvgHeight - marginBottom / 1.5 + 16)
        .style("fill", "#000")
        .style("font-size", "1em")
        .style("font-weight", "bold")
        .style("text-anchor", "left")
        .text(d => regionTable[d]);
}

function ready(videoGameData) {
    const videoGameClean = filterData(videoGameData);
    console.log('S_videoGameClean', videoGameClean);
    
    const barChartData = PrepareBarChartData(videoGameClean);
    console.log('S_barChartData', barChartData);

    const Top15Data = chooseTop15("Global_Sales", barChartData);
    console.log('S_Top15Data', Top15Data);

    const stackBarData = removeGlobalSales(Top15Data);
    console.log('S_StackBarData', stackBarData);

    drawStackBarChart(stackBarData);
}

//load data
d3.csv('data/Video_Games_Sales_as_at_22_Dec_2016.csv', type).then(
    res => {
        ready(res);
    }
)