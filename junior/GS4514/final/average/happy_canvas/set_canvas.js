const parseNA = string => (string === '' ? undefined : string);
const parseDate = string => d3.timeParse('%Y-%m-%d')(string);
export const barcharttooltip = `
<div class = "tooltip">
<div class = "tip-header">
    <h3></h3>
    <h4></h4>
    <h5></h5>
</div>
<div class = "tip-body"></div>
</div>`
export const linecharttooltip = `
<div class = "tooltip1">
<div class = "tip-header1">
    <h1></h1>
    <h2></h2>
</div>
<div class = "tip-body1"></div>
</div>`
function formatTicks(d){ 
    return d3.format('~s')(d) 
        .replace('M','mil') 
        .replace('G','bil') 
        .replace('T','tri')
}
export function setHappyFirstCanvas(originData,barChartData,maxObj) {
    // 需要originData裡面的年份資訊
    
    // 存放目前的年份
    const YearRange = d3.extent(originData, d=>d.Year_of_Release);
    const start = YearRange[0];
    const end = YearRange[1]; 
    
    const svg_width = 1700;
    const svg_height = 800;
    const chart_margin = {
        top: 120,
        right: 80,
        bottom: 40,
        left: 140
    };
    const chart_width = svg_width - (chart_margin.left + chart_margin.right);
    const chart_height = svg_height - (chart_margin.top + chart_margin.bottom);
    const this_svg = d3.select('.happy-chart-container')
        .append('svg')
        .attr("preserveAspectRatio", "xMidYMid meet")
        .attr("viewBox", `0 0 ${svg_width} ${svg_height}`)
        .append('g')
        .attr('transform', `translate(${chart_margin.left},${chart_margin.top})`);
    //scale
    // //V1.d3.extent find the max & min in Global_Sales
    // const xExtent = d3.extent(barChartData, d => d.Avg);
  
    const xMax = d3.max(barChartData, d => d.Avg);
    const xScale = d3.scaleLinear([0, xMax], [0, chart_width]);
    const yScale = d3.scaleBand()
        .domain(barChartData.map(d => d.Genre))
        .rangeRound([0, chart_height])
        .paddingInner(0.25);
  
    const bars = this_svg.selectAll('.bar')
        .data(barChartData)
        .enter()
        .append('rect')
        .attr('class', 'bar')
        .attr('x', 0)
        .attr('y', d => yScale(d.Genre))
        .attr('width', d => xScale(d.Avg))
        .attr('height', yScale.bandwidth())
        .style('fill', 'LightSteelBlue');
  
    //Draw header
    const header = this_svg.append('g')
        .attr('class', 'bar-header')
        .attr('transform', `translate(0,${-chart_margin.top / 2})`)
        .append('text');
    header.append('tspan')
        .text(`Average Global Sales by Genre`)
        .style("font-size", "1.5em")
        .style('font-weight', 'bold');
    header.append('tspan')
        .text('Every Thousand in US$')
        .style("font-size", "1em")
        .attr('x', 0)
        .attr('y', 25)
        .style('font-size', '0.8em')
        .style('fill', '#555');
    header.append('tspan')
        .text(`From : ${start} to ${end}`)
        .style("font-size", "1em")
        .attr('x', 180)
        .attr('y', 25)
        .style('font-size', '0.8em')
        .style('fill', '#555');
  
    const xAxis = d3.axisTop(xScale)
        .tickFormat(formatTicks)
        .tickSizeInner(-chart_height)
        .tickSizeOuter(0);
    const xAxisDraw = this_svg.append('g')
        .attr('class', 'x axis')
        .style("font-size", "0.8em")
        .call(xAxis);
    const yAxis = d3.axisLeft(yScale)
        .tickSize(0);
    const yAxisDraw = this_svg.append('g')
        .attr('class', 'y axis')
        .style("font-size", "1em")
        .call(yAxis);
    yAxisDraw.selectAll('text')
        .attr('dx', '-0.6em');
    const tip =d3.select('.tooltip')
    function mouseover (e){
      const thisBarData = d3.select(this).data()[0]
      let Salesnumber;  
      let MaxSaleGame;
    	for(let i =0; i< maxObj.length;i++)
      {
      	if(maxObj[i].Genre == thisBarData.Genre)
        {
        	MaxSaleGame = maxObj[i].which;
        }
      }
      if(parseInt(MaxSaleGame.Global_Sales)/10<1)
      {
        Salesnumber = (MaxSaleGame.Global_Sales*100).toFixed(0);
      }
      else 
      {
        Salesnumber = (parseInt(MaxSaleGame.Global_Sales)/10).toFixed(1)+'k';
      }
      let bodydata=[
          ['GlobalSales',Salesnumber],
          ['Platform',MaxSaleGame.Platform],
          ['Publisher',MaxSaleGame.Publisher],
        ] 
      tip.style('left',(e.clientX+15)+'px')
        .style('top',e.clientY+'px')
        .style('opacity',0.98)
      tip.select('h3').html(`${MaxSaleGame.Name}`);
      tip.select('h4').html("Genre: "+`${MaxSaleGame.Genre}`);
      tip.select('h5').html("ReleaseYear: "+`${MaxSaleGame.Year_of_Release}`);
      d3.select('.tip-body').selectAll('p').data(bodydata)
          .join('p').attr('class', 'tip-info')
          .html(d=>`${d[0]} : ${d[1]}`);  
    }
    function mousemove (e){
      tip.style('left',e.clientX+'px')
        .style('top',e.clientY+'px')
        .style('opacity',0.98)          
    }
    function mouseout(){
      tip.style('opacity',0);
    }
    d3.selectAll('.bar')
      .on('mouseover',mouseover)  
      .on('mousemove',mousemove)
      .on('mouseout',mouseout)
}

export function setHappyLineChart(LineChartData, current,maxSaleGameInthisFive) {
  // input資料是一個[genere:array[8]]的陣列，分別代表每個種類和不同時間段的遊戲數量。    
  let xData = [];
  let yData = [];
  for (let x = 0; x < LineChartData[current].length; x++){
      xData.push(parseInt(LineChartData[current][x].year));
      yData.push(parseInt(LineChartData[current][x].count));
  }
  // console.log(xData);
  // console.log(yData);
  
  const width = 1700;
  const height = 800;
  const margin = { top: 150, right: 80, bottom: 100, left: 100 };
  const innerWidth = width - margin.left - margin.right;
  const innerHeight = height - margin.top - margin.bottom;
  
  // 創建SVG元素
  const svg = d3.select(".happy-linechart-container")
    .append("svg")
    .attr("preserveAspectRatio", "xMidYMid meet")
    .attr("viewBox", `0 0 ${width} ${height}`)
    .append('g');
    
  // 創建圖表標題
  svg.append("text")
      .attr("class", "chart-title")
    .attr("x", margin.left)
    .attr("y", margin.top-50)
      .style("font-size", "1.5em")
      .style("font-weight", "bold")
    .text(`Numbers of ${current} Games in Different Segements`);
  // 創建內部容器
  const g = svg.append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");
  
  // 定義x軸的比例尺
  const xScale = d3.scaleLinear()
    .domain([d3.min(xData)-2, d3.max(xData)])
    .range([0, innerWidth]);
  
  // 定義y軸的比例尺
  const yScale = d3.scaleLinear()
    .domain([d3.min(yData), d3.max(yData) + 20])
    .range([innerHeight, 0]);

  
  // 繪製散點
  g.selectAll("circle")
    .data(xData)
    .enter()
    .append("circle")
    .attr("cx", (d, i) => xScale(d))
    .attr("cy", (d, i) => yScale(yData[i]))
    .attr("r", 10)
    .attr("fill", "steelblue");
  
  // 添加x軸
  g.append("g")
      .attr("class", "axis")
      .style("font-size", "1em")
      .attr("transform", `translate(0,${innerHeight})`)
    .call(d3.axisBottom(xScale));
  
  // 添加y軸
  g.append("g")
      .attr("class", "axis")
      .style("font-size", "1em")
    .call(d3.axisLeft(yScale));
  
  // 添加標點
  // hover時再顯示數值
  g.selectAll(".dot")
    .data(xData)
    .enter()
    .append("text")
    .attr("class", "dot")
    .attr("x", (d, i) => xScale(d))
    .attr("y", (d, i) => yScale(yData[i]) - 20)
//      .text((d, i) => "(" + d + ", " + yData[i] + ")");
// 連接點與點的線段
const line = d3.line()
.x((d, i) => xScale(xData[i]))
.y((d, i) => yScale(yData[i]));

// 繪製連接線
g.append("path")
.datum(xData)
.attr("fill", "none")
.attr("stroke", "steelblue")
.attr("stroke-width", 2)
.attr("d", line);
const tip1 = d3.select('.tooltip1')
function mouseover(e){
  const thisLineData = d3.select(this).data()[0]
  let SelectPoint;
  for(let i =0; i<xData.length ;i++)
  {
    if(thisLineData == xData[i])
      SelectPoint=[xData[i],yData[i]];
  }
  tip1.style('left',(e.clientX+15)+'px')
      .style('top',e.clientY+'px')
      .style('opacity',0.98)
      .html("("+`${SelectPoint[0]}`+','+`${SelectPoint[1]}`+")");
}
function mouseout(){
  tip1.style('opacity',0);
}
d3.selectAll("circle")
  .on('mouseover',mouseover)
  .on('mouseout',mouseout);
}

export function SetHappyPieChart(Data, which){
  // 傳入整理好的資料和要用哪一個來作圖(數字表示)
  let region = Data[which]["Sales"];
  let Sales = Data[which]["SalesNumber"];
  console.log(Data)
  let data = region.map(function(label, index) {
    return {
      label: label,
      value: Sales[index]
    };
  });


  const svgWidth = 1700,
  svgHeight = 900,
  margin = 100;
  
    const svg = d3.select(".happy-piechart-container")
        .append("svg")
        .attr("preserveAspectRatio", "xMidYMid meet")
        .attr("viewBox", `0 0 ${svgWidth} ${svgHeight}`);
  svg.append("g")
  .attr("class", "slices")
  .attr('transform', `translate(${svgWidth / 2}, ${svgHeight / 2})`);
  svg.append("g")
  .attr("class", "labels");
  svg.append("g")
  .attr("class", "lines");
  svg.append("text")
  .attr("class", "chart-title")
  .attr("x", svgWidth / 2 - margin*2)
      .attr("y", svgHeight - margin/2.5)
      .style("font-size", "1.5em")
      .style("font-weight", "bold")
  .text(`${Data[which].Genre} Sales in Different Region`);
  const color = d3.scaleOrdinal()
                .range(["#0bbc17","#F96262", '#ffbe32', '#e271fc']);
  const radius = Math.min(svgWidth, svgHeight) / 2 - margin;
  const piechart = d3.pie().value(d => d.value);
  const arc = d3.arc()
              .innerRadius(0)
              .outerRadius(radius)
              .padAngle(.02)
  const outerArc = d3.arc()
                   .outerRadius(radius * 0.9)
                   .innerRadius(radius * 0.9)
  const data_ready = piechart(data) 
  const total = d3.sum(data, d => d.value)
  data.forEach(d => {
    d.percentage = Math.round((d.value/total)*100)
  })
// 建立pie
const cutePie = svg.select('.slices')
        .selectAll('g')
        .data(data_ready)
        .enter()
        .append('g')
        .attr('class', 'arc')

 cutePie.append('path')
        .attr('d', arc)
        .attr('fill', color)
        .attr("stroke", "#fff")
        .style("stroke-width", "2px")
        .style("opacity", 1);
const arcText = d3.arc()
    .innerRadius(radius)
    .outerRadius(radius - 10);
    
const regionTable = {
    "NA_Sales": "North America Sales",
    "EU_Sales": "Europe Sales",
    "JP_Sales": "Japan Sales",
    "Global_Sales": "Global Sales",
    "Other_Sales": "Other Region Sales"
}
    
const itemText = cutePie.append('text')
              .attr('transform', d => `translate(${arcText.centroid(d)})`)
              .text(d => regionTable[d.data.label] + ' ' + d.data.percentage + '%')
              .style('text-anchor', 'middle')
              .style('font-size', "2em")
              .style('fill', 'black')
              d3.selectAll('.arc path')
              .style('cursor', 'pointer')
              .on('mouseover', function(){
                 d3.select(this)
                   .transition()
                   .duration(500)
                   .style("filter", "drop-shadow(2px 4px 6px black)")
                   .style('transform', 'scale(1.1)')
              })
              .on('mouseleave', function(){
                d3.select(this)
                  .transition()
                  .duration(500)
                  .style("filter", "drop-shadow(0 0 0 black)")
                  .style('transform', 'scale(1)')
              })
}



export function setEricBarChartCanvas(data, region) {
  const svgWidth = 1700;
  const svgHeight = 800;
  const margin = { top: 120, right: 60, bottom: 40, left: 400 };
  const chartWidth = svgWidth - margin.left - margin.right;
  const chartHeight = svgHeight - margin.top - margin.bottom;

  // 移除舊的圖表元素
  d3.select('#bar-chart-container svg').remove();

  const filteredData = data.filter(d => d[region] > 0)
    .sort((a, b) => b[region] - a[region])
    .slice(0, 20);

const svg = d3
  .select('#bar-chart-container')
    .append('svg')
    .attr("preserveAspectRatio", "xMidYMid meet")
    .attr("viewBox", `0 0 ${svgWidth} ${svgHeight}`);

const chart = svg.append('g').attr('transform', `translate(${margin.left},${margin.top})`);

const xScale = d3
  .scaleLinear()
  .domain([0, d3.max(filteredData, d => d[region])])
  .range([0, chartWidth]);

const yScale = d3
  .scaleBand()
  .domain(filteredData.map(d => d.publisher))
  .range([0, chartHeight])
  .paddingInner(0.1);

const xAxis = d3.axisBottom(xScale).ticks(10).tickFormat(d => `${d} M`);

chart.append('g').style("font-size", "1em").attr('transform', `translate(0,${chartHeight})`).call(xAxis);

const yAxis = d3.axisLeft(yScale);
chart.append('g').style("font-size", "1em").call(yAxis);

// 設定顏色比例尺
const colorScale = d3.scaleOrdinal(d3.schemeCategory10);

// 更新圖表元素之前的動畫處理
chart
  .selectAll('.bar')
  .data(filteredData, d => d.publisher)
  .join(
    enter =>
      enter
        .append('rect')
        .attr('class', 'bar')
        .attr('x', 0)
        .attr('y', d => yScale(d.publisher))
        .attr('width', 0)
        .attr('height', yScale.bandwidth())
        .attr('fill', d => colorScale(d.publisher)),
    update => update,
    exit =>
      exit
        .transition()
        .duration(1000)
        .attr('opacity', 0)
        .remove()
  )
  .transition()
  .duration(800)
  .attr('width', d => xScale(d[region]))
  .attr('y', d => yScale(d.publisher))
  .attr('opacity', 1);

    
const regionTable = {
    "NA_Sales": "North America",
    "EU_Sales": "Europe",
    "JP_Sales": "Japan",
    "Global_Sales": "Global",
    "Other_Sales": "Other Region"
}
    
// 添加圖表標題
svg
  .append('text')
  .attr('class', 'chart-title')
  .attr('x', svgWidth / 2)
  .attr('y', margin.top / 2)
    .attr('text-anchor', 'middle')
    .style('font-size', '1.5em')
  .style('font-weight', 'bold')
  .text(`Top 20 Publishers for ${regionTable[region]} Sales`);
  
// 添加副標題
svg
  .append('text')
  .attr('class', 'sub-title')
  .attr('x', svgWidth / 2)
  .attr('y', margin.top / 2 + 30) // 調整 y 座標位置以避免重疊
    .attr('text-anchor', 'middle')
    .style('font-size', '1.2em')
  .style('fill', 'rgba(0, 0, 0, 0.7)')
  .text('Years: 1980~2020s');

// 添加 x 軸標籤
chart
  .append('text')
  .attr('class', 'unit-label')
  .attr('x', chartWidth - margin.right - 60)
  .attr('y', chartHeight - margin.top + 65)
  .attr('text-anchor', 'middle')
  .style('font-weight', 'bold') // 加粗字體
  .text('Average Sales (in millions)');

// 添加 y 軸標籤
chart
  .append('text')
  .attr('class', 'unit-label')
  .attr('x', -margin.left + 310)
  .attr('y', -margin.top / 4)
    .attr('text-anchor', 'start')
    .style('font-weight', 'bold')
  .style('fill', 'rgba(220, 20, 20, 1)')
  .text('Publisher');

  // 更新下拉式選單的事件處理程序
  d3.select('#region-select').on('change', function() {
    const selectedRegion = this.value;

    setEricBarChartCanvas(data, selectedRegion);
  });


//interactive 互動處理
const tip = d3.select('.erictooltip');

function mouseover(e) {
  //get data
  const thisBarData = d3.select(this).data()[0];
  // 輸出數據到控制台
  // debugger;
  tip
    .style('left', e.clientX + 15 + 'px')
    .style('top', e.clientY + 'px')
    .transition()
    .style('opacity', 0.98);

  tip.select('h3').html(`${thisBarData.publisher}`);
  tip.select('h4').html(
    `<strong>Sales:</strong><br>NA: ${thisBarData.NA_Sales.toFixed(3)}M<br>EU: ${thisBarData.EU_Sales.toFixed(3)}M<br>
    JP: ${thisBarData.JP_Sales.toFixed(3)}M<br>Other: ${thisBarData.Other_Sales.toFixed(3)}M`
  );
}

function mousemove(e) {
  tip.style('left', e.clientX + 15 + 'px').style('top', e.clientY + 'px');
}
function mouseout(e) {
  tip.transition()
    .style('opacity', 0);
}

//interactive 新增監聽
chart
  .selectAll('.bar')
  .on('mouseover', mouseover)
  .on('mousemove', mousemove)
  .on('mouseout', mouseout);

}