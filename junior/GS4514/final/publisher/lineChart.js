import {
    formatTicks,
    type,
    filterData,
    prepareLineChartData
} from "./lineChartPreprocessing.js";

function setupLineChartCanvas(lineChartData , dataClean) {
    /* 建構svg */
    const svg_width = 1700;
    const svg_height = 800;
    const chart_margin = {
        top:150,
        right:80,
        bottom:100,
        left:100
    };
    const chart_width = svg_width - (chart_margin.left + chart_margin.right);
    const chart_height = svg_height - (chart_margin.top + chart_margin.bottom);

    const this_svg = d3.select(".line-chart-container").append("svg")
                    .attr("preserveAspectRatio", "xMidYMid meet")
                    .attr("viewBox", `0 0 ${svg_width} ${svg_height}`)
                    .append('g')
                    .attr("transform",`translate(${chart_margin.left},${chart_margin.top})`);


    /* 選擇不同地區、開發商 */
    let metricR = "Global_Sales";
    let metricP = "Activision";
    function clickRegion() {
        metricR = this.value;
        console.log(metricR);
        const newLineData = prepareLineChartData(dataClean , metricR , metricP);
        
        update(newLineData);        
    }
    function clickPublisher() {
        metricP = this.value;
        const newLineData = prepareLineChartData(dataClean , metricR , metricP);

        console.log(metricP);
        update(newLineData);
    }

    d3.select(".region").on("click" , clickRegion);
    d3.select(".publisher").on("click" , clickPublisher);

   

    /* 更新圖表 */
    function update(data) {
        xExtent = d3.extent(data.dates);
        xScale = d3.scaleTime().domain(xExtent).range([0 , chart_width]);
        yScale = d3.scaleLinear().domain([0 , data.yMax]).range([chart_height , 0]);
        
        /* Transition Setting */
        const defaultDelay = 1000
        const transitionDelay = d3.transition().duration(defaultDelay);

        /* line generator */
        lineGen = d3.line()
                    .x(d => xScale(d.date))
                    .y(d => yScale(d.value))
        
        /* update axis */
        xAxisDraw.transition(transitionDelay).call(xAxis.scale(xScale));
        yAxisDraw.transition(transitionDelay).call(yAxis.scale(yScale));
    
        /* 加入資料圓點 */
        console.log("data",data);
    
        dotGroup.selectAll("circle")
                .data(data.salesArray)
                .join("circle")
                .attr('r', '8').transition(transitionDelay)
                .attr('cx', d => xScale(d3.timeParse('%Y')(d[0])))
                .attr('cy', d => yScale(d[1]))
                .attr('fill', data.series[0].color)
                .attr('stroke', data.series[0].color)
                .attr('stroke-width', '2')
                .style('cursor', 'pointer')

        /* 圓點互動 */
        const tip = d3.select('.lineChartTip');
            
        /* cursor 指向圓點顯示資訊 */
        function mouseover(e) {
            const thisLineData = d3.select(this).data()[0];
            console.log(thisLineData);

            const bodyData = [
                ["Year" , thisLineData[0]],
                ["Sales" , formatTicks(Math.round(thisLineData[1]*100)/100)]
            ]

            tip.style('left',(e.clientX+15)+'px')
                .style('top',e.clientY+'px')
                .style('opacity',0.98)
            tip.selectAll("p").data(bodyData)
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

        d3.selectAll("circle")
            .on("mouseover", mouseover)
            .on("mousemove" , mousemove)
            .on("mouseout" , mouseout);
        /* update line */
        chartGroup.selectAll(".line-series").data(data.series).join(
            enter => {
                enter.append("path")
                        .attr("class" , d => `line-series ${d.name.toLowerCase()}`)
                        .attr("d" , d => lineGen(d.values))
                        .style("fill" , "none").style("stroke" , d => d.color);
            },

            update => {
                update.transition(transitionDelay)
                        .delay((d,i) => i*20)
                        .attr("d" , d => lineGen(d.values))
                        .style("stroke" , d => d.color)
            },
            exit => {
                exit.transition().duration(defaultDelay/2)
                    .style("fill-opacity" , 0)
                    .remove()
            }
        )

        /* update header */
        const regionTable = {
            "NA_Sales": "North America",
            "EU_Sales": "Europe",
            "JP_Sales": "Japan",
            "Global_Sales": "Global",
            "Other_Sales": "Other Region"
        }
        
        headerLine.text(`${regionTable[metricR]} Sales for ${metricP}`)
                    .attr("font-size" , "2em");
    }

    /* scale */
    let xExtent = d3.extent(lineChartData.dates);
    let xScale = d3.scaleTime().domain(xExtent).range([0,chart_width]);
    let yScale = d3.scaleLinear().domain([0,lineChartData.yMax]).range([chart_width,0]);

    /* line generator */
    let lineGen = d3.line()
                        .x(d => xScale(d.date))
                        .y(d => yScale(d.value))
    
    /* draw line */
    const chartGroup = this_svg.append("g").attr("class" , "line-chart");
    chartGroup.selectAll(".line-series").data(lineChartData.series).enter()
                .append("path")
                .attr("class" , d => `line-series ${d.name.toLowerCase()}`)
                .attr("d" , d => lineGen(d.values))
                .style("fill" , "none").style("stroke" , d => d.color);


    /* draw x axis */
    let xAxis = d3.axisBottom(xScale).tickSizeOuter(0);
    let xAxisDraw = this_svg.append("g").attr("class" , "x axis")
                            .attr("transform" , `translate(0,${chart_height})`)
                            .style("font-size", "0.8em");

    /* draw y axis */
    let yAxis = d3.axisLeft(yScale).tickFormat(formatTicks)
                    .tickSizeInner(-chart_width).tickSizeOuter(0);
    let yAxisDraw = this_svg.append("g").attr("class", "y axis").style("font-size", "1em");
    
    /* draw dot */
    const dotGroup = this_svg.append("g").attr("class" , "dot");

    /* draw header */
    const headerLine = this_svg.append("g")
                                .attr("class" , "header")
                                .attr("transform" , `translate(0 , ${-chart_margin.top/2})`)
                                .append("text");
    headerLine.append("tspan").text(`${metricR} for ${metricP}`);

    update(lineChartData);
}

function ready(videoGameData) {
    const videoGameClean = filterData(videoGameData);
    
    const lineChartData = prepareLineChartData(videoGameClean , "Global_Sales" , "Activision");
    console.log("lineChartData",lineChartData);

    setupLineChartCanvas(lineChartData , videoGameClean);
}

d3.csv("data/Video_Games_Sales_as_at_22_Dec_2016.csv" , type).then(
    res => {
        ready(res);
    }
)