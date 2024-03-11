import { 
  formatTicks, 
} from './utilities.js';

export function setupFirstCanvas(barChartData) {

  const svg_width = 400;
  const svg_height = 500;
  const chart_margin = {
      top: 80,
      right: 40,
      bottom: 40,
      left: 80
  };
  const chart_width = svg_width - (chart_margin.left + chart_margin.right);
  const chart_height = svg_height - (chart_margin.top + chart_margin.bottom);
  const this_svg = d3.select('.bar-chart-container')
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
      .text('Total Global_Sales by Genre ')
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
}

export function setupSecondCanvas(barChartData) {

  const svg_width = 400;
  const svg_height = 500;
  const chart_margin = {
      top: 80,
      right: 40,
      bottom: 40,
      left: 80
  };
  const chart_width = svg_width - (chart_margin.left + chart_margin.right);
  const chart_height = svg_height - (chart_margin.top + chart_margin.bottom);
  const this_svg = d3.select('.bar-chart-container')
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
      .domain(barChartData.map(d => d.Platform))
      .rangeRound([0, chart_height])
      .paddingInner(0.25);

  const bars = this_svg.selectAll('.bar')
      .data(barChartData)
      .enter()
      .append('rect')
      .attr('class', 'bar')
      .attr('x', 0)
      .attr('y', d => yScale(d.Platform))
      .attr('width', d => xScale(d.Global_Sales))
      .attr('height', yScale.bandwidth())
      .style('fill', 'DarkCyan');

  //Draw header
  const header = this_svg.append('g')
      .attr('class', 'bar-header')
      .attr('transform', `translate(0,${-chart_margin.top / 2})`)
      .append('text');
  header.append('tspan')
      .text('Total Global_Sales by Platform ')
      .style('font-weight', 'bold');
  header.append('tspan')
      .text('Global_Sales > 100(in Million $US)')
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
}

export function setupThirdCanvas(barChartData) {

  const svg_width = 400;
  const svg_height = 500;
  const chart_margin = {
      top: 80,
      right: 40,
      bottom: 40,
      left: 80
  };
  const chart_width = svg_width - (chart_margin.left + chart_margin.right);
  const chart_height = svg_height - (chart_margin.top + chart_margin.bottom);
  const this_svg = d3.select('.bar-chart-container')
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
      .style('fill', 'DarkGreen');

  //Draw header
  const header = this_svg.append('g')
      .attr('class', 'bar-header')
      .attr('transform', `translate(0,${-chart_margin.top / 2})`)
      .append('text');
  header.append('tspan')
      .text('PS2 Global_Sales by Genre ')
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
}

export function setupForthCanvas(barChartData) {

  const svg_width = 400;
  const svg_height = 500;
  const chart_margin = {
      top: 80,
      right: 40,
      bottom: 40,
      left: 80
  };
  const chart_width = svg_width - (chart_margin.left + chart_margin.right);
  const chart_height = svg_height - (chart_margin.top + chart_margin.bottom);
  const this_svg = d3.select('.bar-chart-container')
      .append('svg')
      .attr('width', svg_width)
      .attr('height', svg_height)
      .append('g')
      .attr('transform', `translate(${chart_margin.left},${chart_margin.top})`);
  //scale
  //V1.d3.extent find the max & min in Global_Sales
  const xExtent = d3.extent(barChartData, d => d.User_Score);

  const xMax = d3.max(barChartData, d => d.User_Score);
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
      .attr('width', d => xScale(d.User_Score))
      .attr('height', yScale.bandwidth())
      .style('fill', 'LightSteelBlue');

  //Draw header
  const header = this_svg.append('g')
      .attr('class', 'bar-header')
      .attr('transform', `translate(0,${-chart_margin.top / 2})`)
      .append('text');
  header.append('tspan')
      .text('PS2 Users_Score by Genre ')
      .style('font-weight', 'bold');
  header.append('tspan')
      .text('')
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
}