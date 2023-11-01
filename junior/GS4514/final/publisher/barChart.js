// 導入外部函式
import {
    formatTicks,
    type,
    filterData,
    chooseTop15,
    PrepareBarChartData
} from './barChartPreprocessing.js';

// 初始資料集
d3.csv('data/Video_Games_Sales_as_at_22_Dec_2016.csv').then(
    res => {
        console.log('initialData', res);
    }
)
// 資料過濾
d3.csv('data/Video_Games_Sales_as_at_22_Dec_2016.csv', type).then(
    res => {
        console.log('afterFilterData', res);
    }
)

function setupCanvas(barChartData) {
    // interactive
    const tip = d3.select('.barChartTip');

    function mouseover(e) {
        const thisBarData = d3.select(this).data()[0];
        const bodyData = [
            ["North America", formatTicks(Math.round(thisBarData.NA_Sales))],
            ["Europe", formatTicks(Math.round(thisBarData.EU_Sales))],
            ["Japan", formatTicks(Math.round(thisBarData.JP_Sales))],
            ["Other Region", formatTicks(Math.round(thisBarData.Other_Sales))],
            ["Global", formatTicks(Math.round(thisBarData.Global_Sales))]
        ]
        tip.select('h3').html(`${thisBarData.Publisher}`);
        tip.style('left',(e.clientX+15)+'px')
            .style('top',e.clientY+'px')
            .style('opacity',0.98)
        d3.select(".tip-body").selectAll("p").data(bodyData)
            .join("p").attr("class" , "tip-info")
            .html(d => `${d[0]} : ${d[1]}`);
    }

    function mousemove(e) {
        tip.style("left",(e.clientX+15)+"px")
            .style("top",e.clientY+"px")
    }

    function mouseout(e) {
        tip.style("opacity" , 0)
    }
    
    let metric = "Global_Sales";
    barChartData = chooseTop15(metric, barChartData);

    function click() {
        metric = this.dataset.name;
        console.log('click this',this);

        const thisData = chooseTop15(metric, barChartData);
        console.log('thisData', thisData);
        update(thisData);
    }

    d3.selectAll("button").on("click", click);
    
    function update(data) {
        xMax = d3.max(data, d => d[metric]);
        xScale = d3.scaleLinear([0 , xMax] , [0 , chart_width]);
                    
        yScale = d3.scaleBand().domain(data.map(d => d.Publisher))
            .rangeRound([0, chart_height])
            .paddingInner(0.25);
        
        // Transition Setting
        const defaultDelay = 1000;
        const transitionDelay = d3.transition().duration(defaultDelay);

        // update axis
        xAxisDraw.transition(transitionDelay).call(xAxis.scale(xScale));
        yAxisDraw.transition(transitionDelay).call(yAxis.scale(yScale));

        // update header
        const regionTable = {
            "NA_Sales": "North America",
            "EU_Sales": "Europe",
            "JP_Sales": "Japan",
            "Global_Sales": "Global",
            "Other_Sales": "Other Region"
        }

        header.select("tspan").text(`Top 15 Publisher of Sales in ${regionTable[metric]}`);

        const colorTable = {
            "NA_Sales": "#379CA9",
            "EU_Sales": "#44D3DD",
            "JP_Sales": "#FF99AA",
            "Global_Sales": "#FFA07A",
            "Other_Sales": "#F2D091"
        }

        // update bar
        bars.selectAll(".bar").data(data, d => d.Publisher).join(
            enter => {
                enter.append("rect")
                    .attr("class", "bar")
                    .attr("x", 0).attr("y", d => yScale(d.Publisher))
                    .attr("height", yScale.bandwidth())
                    .style("fill", "lightcyan")
                    .transition(transitionDelay)
                    .delay((d, i) => i * 20)
                    .attr("width", d => xScale(d[metric]))
                    .style("fill", `${colorTable[metric]}`)
            },
            update => {
                update.transition(transitionDelay)
                    .delay((d, i) => i * 20)
                    .attr("y", d => yScale(d.Publisher))
                    .style("fill", `${colorTable[metric]}`)
                    .attr("width", d => xScale(d[metric]))
            },
            exit => {
                exit.transition().duration(defaultDelay / 2)
                    .style("fill-opacity", 0)
                    .remove()
            }
        );

        // listen
        d3.selectAll('.bar')
            .on('mouseover',mouseover)
            .on("mousemove",mousemove)
            .on("mouseout",mouseout);
    }

    // 畫布尺寸
    const svg_width = 1700;
    const svg_height = 800;
    const chart_margin = {
        top: 120,
        right: 80,
        bottom: 40,
        left: 400
    };
    const chart_width = svg_width-(chart_margin.left+chart_margin.right);
    const chart_height = svg_height-(chart_margin.top+chart_margin.bottom);

    const this_svg = d3.select(".bar-chart-container").append("svg")
                        .attr("preserveAspectRatio", "xMidYMid meet")
                        .attr("viewBox", `0 0 ${svg_width} ${svg_height}`)
                        .append('g')
                        .attr("transform",`translate(${chart_margin.left},${chart_margin.top})`);

    //scale
    const xExtent = d3.extent(barChartData , d => d.NA_Sales);
    let xMax = d3.max(barChartData , d => d.NA_Sales);
    let xScale = d3.scaleLinear([0,xMax] , [0, chart_width]);
    let yScale = d3.scaleBand()
        .domain(barChartData.map(d=>d.Publisher))
        .rangeRound([0,chart_height])
        .paddingInner(0.25);
    
    // draw bars
    const bars = this_svg.append('g')
        .attr('class', 'bars');

    // draw header
    let header = this_svg.append("g")
        .attr("class" , "bar-header")
        .attr("transform" , `translate(0,${-chart_margin.top/2})`)
        .append("text");
    
    header.append("tspan").text("Top 15 Publisher of Sales in North America")
        .style("font-size", "1.5em");
    header.append("tspan").text(`Years: 1980 - 2016`)
        .attr("x", 0).attr("y", 30).style("font-size", "1em").style("fill", "#555");
    
    // handle axis
    let xAxis = d3.axisTop(xScale)
        .ticks(5)
        .tickFormat(formatTicks)
        .tickSizeInner(-chart_height)
        .tickSizeOuter(0);
    let xAxisDraw = this_svg.append("g").attr("class" , "x axis").style("font-size", "0.8em");

    let yAxis = d3.axisLeft(yScale).tickSize(0);
    let yAxisDraw = this_svg.append("g").attr("class", "y axis").style("font-size", "1em");
    yAxisDraw.selectAll("text").attr("dx" , "-0.6em");
    update(barChartData);

}

function ready(videoGameData) {
    const videoGameClean = filterData(videoGameData);
    console.log('videoGameClean', videoGameClean);
    
    const barChartData = PrepareBarChartData(videoGameClean);
    console.log('barChartData', barChartData);

    const Top15Data = chooseTop15("Global_Sales", barChartData);
    console.log('Top15Data', Top15Data);
    setupCanvas(barChartData);
}

//load data
d3.csv('data/Video_Games_Sales_as_at_22_Dec_2016.csv', type).then(
    res => {
        ready(res);
    }
)