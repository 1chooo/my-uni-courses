import {
  formatTicks,
} from './utilities.js';

export function setupPSCanvas(barChartData) {

  const svg_width = 600;
  const svg_height = 500;
  const chart_margin = {
    top: 80,
    right: 40,
    bottom: 40,
    left: 80
  };
  const chart_width = svg_width - (chart_margin.left + chart_margin.right);
  const chart_height = svg_height - (chart_margin.top + chart_margin.bottom);
  const this_svg = d3.select('.bar-chart-container-final')
    .append('svg')
    .attr('width', svg_width)
    .attr('height', svg_height)
    .append('g')
    .attr('transform', `translate(${chart_margin.left},${chart_margin.top})`);
  //scale
  //V1.d3.extent find the max & min in Global_Sales
  const xExtent = d3.extent(barChartData, d => d.Global_Sales);

  const xMax = d3.max(barChartData, d => d.Global_Sales);
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
    .attr('width', d => xScale(d.Global_Sales))
    .attr('height', yScale.bandwidth())
    .style('fill', 'dodgerblue');

  //Draw header
  const header = this_svg.append('g')
    .attr('class', 'bar-header')
    .attr('transform', `translate(0,${-chart_margin.top / 2})`)
    .append('text');
  header.append('tspan')
    .text('Total Global_Sales by Genre only PS platform')
    .style('font-weight', 'bold');
  header.append('tspan')
    .text('(in Million $US)')
    .attr('x', 0)
    .attr('y', 20)
    .style('font-size', '0.8em')
    .style('fill', '#555');

  const xAxis = d3.axisTop(xScale)
    .tickFormat(formatTicks)
    .tickSizeInner(-chart_height)
    .tickSizeOuter(0);
  const xAxisDraw = this_svg.append('g')
    .attr('class', 'x axis')
    .call(xAxis);
  const yAxis = d3.axisLeft(yScale)
    .tickSize(0);
  const yAxisDraw = this_svg.append('g')
    .attr('class', 'y axis')
    .call(yAxis);
  yAxisDraw.selectAll('text')
    .attr('dx', '-0.6em');


  //interactive 互動處理
  const tip = d3.select('.tooltip');
  function mouseover(e) {

    const thisBarData = d3.select(this).data()[0];
    console.log(thisBarData);


    tip.style('left', (e.clientX + 15) + 'px')
      .style('top', e.clientY + 'px')
      .transition()
      .style('opacity', 0.98);
    tip.select('h3').html("PS Platform");

    const globalSales = parseFloat(thisBarData.Global_Sales).toFixed(2);

    tip.select('h4')
      .html(`${globalSales} million $US`);
    d3.select('.tip-body')
      .selectAll('p')
      .data([thisBarData.Genre])
      .join('p')
      .attr('class', 'tip-info')
      .html(d => `Genre: ${d}`);



  }
  function mousemove(e) {
    tip.style('left', (e.clientX + 15) + 'px')
      .style('top', e.clientY + 'px')
  }
  function mouseout(e) {
    tip.transition()
      .style('opacity', 0)
  }
  //interactive 新增監聽
  d3.selectAll('.bar')
    .on('mouseover', mouseover)
    .on('mousemove', mousemove)
    .on('mouseout', mouseout);

}

