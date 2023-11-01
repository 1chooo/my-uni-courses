// Data utilities
// '===' is the judgement of the data type.
// if we meet the data type which is 'NA', 
// we change it into the 'undefined',
// or we keep the original string.
const parseNA = string => (string === 'NA' ? undefined : string);
// Solving the format of the date.
const parseDate = string => d3.timeParse('%Y-%m-%d')(string);


function type(d) {
    const date = parseDate(d.release_date);
    return {
        budget: +d.budget,
        genre: parseNA(d.genre),
        genres: JSON.parse(d.genres).map(d => d.name),
        homepage: parseNA(d.homepage),
        id: +d.id,
        imdb_id: parseNA(d.imdb_id),
        original_language: parseNA(d.original_language),
        overview: parseNA(d.overview),
        popularity: +d.popularity,
        poster_path: parseNA(d.poster_path),
        production_countries: JSON.parse(d.production_countries),
        release_date: date,
        release_year: date.getFullYear(),
        revenue: +d.revenue,
        runtime: +d.runtime,
        tagline: parseNA(d.tagline),
        title: parseNA(d.title),
        vote_average: +d.vote_average,
        vote_count: +d.vote_count,
    }
}

//Data selection
function filterData(data) {
    console.log(typeof (data))       // object
    return data.filter(
        d => {
            return (
                // we want to observe the data in ten years 
                d.release_year > 1999 &&
                d.release_year < 2010 &&
                // After we filter the data, we only pick up 
                // the type we can visualize.
                d.revenue > 0 &&
                d.budget > 0 &&
                d.genre &&
                d.title
            );
        }
    );
}

function prepareBarChartData(data) {
    console.log(data);
    const dataMap = d3.rollup(
        data,
        v => d3.sum(v, leaf => leaf.revenue), // Sum up the revenue.
        d => d.genre // categorize the movie with groupby
    );
    const dataArray = Array.from(dataMap, d => ({ genre: d[0], revenue: d[1] }));
    return dataArray;
}

function formatTicks(d) {
    return d3.format('~s')(d).
        replace('M', 'mil')
        .replace('G', 'bil')
        .replace('T', 'tri')
}



function setupCanvas(barChartData, movieClean) {
    //一開始預設指標是revenue
    let metric = 'revenue';

    function click() {
        metric = this.dataset.name;
        const thisData = chooseData(metric, movieClean);

        update(thisData);
    }

    d3.selectAll('button').on('click', click);

    function update(data) {
        console.log(data);
        //Update Scale
        xMax = d3.max(data, d => d[metric]);
        xScale_v3 = d3.scaleLinear([0, xMax], [0, barchart_width]);
        yScale = d3.scaleBand()
            .domain(data.map(d => d.title))
            .rangeRound([0, barchart_height])
            .paddingInner(0.25);
        //Transition Settings
        const defaultDelay = 1000
        const transitionDelay = d3.transition()
            .duration(defaultDelay);
        //Update axis
        xAxisDraw.transition(transitionDelay)
            .call(xAxis.scale(xScale_v3));
        yAxisDraw.transition(transitionDelay)
            .call(yAxis.scale(yScale));
        //Update Header
        header.select('tspan')
            .text(`Top 15 ${metric} movies ${metric === 'popularity' ? '' : 'in $US'}`);
        //Update Bar
        bars.selectAll('.bar')
            .data(data, d => d.title)
            .join(
                enter => {
                    enter.append('rect')
                        .attr('class', 'bar')
                        .attr('x', 0)
                        .attr('y', d => yScale(d.title))
                        .attr('height', yScale.bandwidth())
                        .style('fill', 'lightcyan')
                        .transition(transitionDelay).delay((d, i) => i * 20)
                        .attr('width', d => xScale_v3(d[metric]))
                        .style('fill', 'dodgerblue')
                },
                update => {
                    update.transition(transitionDelay)
                        .delay((d, i) => i * 20)
                        .attr('y', d => yScale(d.title))
                        .attr('width', d => xScale_v3(d[metric]))
                },
                exit => {
                    exit.transition()
                        .duration(defaultDelay / 2)
                        .style('fill-opacity', 0)
                        .remove()
                }
            );
    }

    const svg_width = 700;
    const svg_height = 500;
    const barchart_margin = {
        top: 80,
        right: 80,
        bottom: 40,
        left: 250
    };
    const barchart_width = svg_width - (barchart_margin.left + barchart_margin.right);
    const barchart_height = svg_height - (barchart_margin.top + barchart_margin.bottom);
    const this_svg = d3.select('.bar-chart-container')
        .append('svg')
        .attr('width', svg_width)
        .attr('height', svg_height)
        .append('g')
        .attr('transform', `translate(${barchart_margin.left},${barchart_margin.top})`);
    //scale
    //V1.d3.extent find the max & min in revenue
    const xExtent = d3.extent(barChartData, d => d.revenue);
    const xScale_v1 = d3.scaleLinear().domain(xExtent).range([0, barchart_width]); //V2.0 ~ max
    let xMax = d3.max(barChartData, d => d.revenue);
    const xScale_v2 = d3.scaleLinear().domain([0, xMax]).range([0, barchart_width]); //V3.Short writing for v2
    let xScale_v3 = d3.scaleLinear([0, xMax], [0, barchart_width]);
    //垂直空間的分配 - 平均分布給各種類
    // const yScale = d3.scaleBand().domain(barChartData.map(d=>d.genre))
    // .rangeRound([0, barchart_height])
    // .paddingInner(0.25);
    //垂直空間的分配 - 平均分布給Top 15
    let yScale = d3.scaleBand()
        .domain(barChartData.map(d => d.title))
        .rangeRound([0, barchart_height])
        .paddingInner(0.25);

    //Draw bars
    // const bars = this_svg.selectAll('.bar').data(barChartData).enter()
    //                      .append('rect')
    //                        .attr('class','bar')
    // .attr('x',0).attr('y',d=>yScale(d.genre))
    // .attr('width',d=>xScale_v3(d.revenue))
    // .attr('height',yScale.bandwidth())
    // .style('fill','dodgerblue'); 
    const bars = this_svg.append('g').attr('class', 'bars');
    //Draw header
    let header = this_svg.append('g')
        .attr('class', 'bar-header')
        .attr('transform', `translate(0,${-barchart_margin.top / 2})`)
        .append('text');
    //header.append('tspan').text('Total revenue by genre in $US'); 
    header.append('tspan')
        .text('Top 15 XXX movies');
    header.append('tspan')
        .text('Years:2000-2009')
        .attr('x', 0)
        .attr('y', 20)
        .style('font-size', '0.8em')
        .style('fill', '#555');

    //tickSizeInner : the length of the tick lines
    //tickSizeOuter : the length of the square ends of the domain path 
    let xAxis = d3.axisTop(xScale_v3)
        .ticks(5)
        .tickFormat(formatTicks)
        .tickSizeInner(-barchart_height)
        .tickSizeOuter(0);
    //this_svg.append('g').attr('class','x axis').call(xAxis);
    let xAxisDraw = this_svg.append('g')
        .attr('class', 'x axis');
    //tickSize : set tickSizeInner & Outer
    let yAxis = d3.axisLeft(yScale)
        .tickSize(0);
    //const yAxisDraw = this_svg.append('g').attr('class','y axis').call(yAxis); 
    let yAxisDraw = this_svg.append('g')
        .attr('class', 'y axis');
    yAxisDraw.selectAll('text')
        .attr('dx', '-0.6em');

    update(barChartData);
}

//Main
function ready(movies) {
    const movieClean = filterData(movies);
    //Get Top 15 revenue movies
    const revenueData = chooseData("revenue", movieClean); 
    setupCanvas(revenueData, movieClean);
}

//Load Data
d3.csv('./data/movies.csv', type).then(
    result => {
        ready(result)
        // console.log(result); 
        // debugger;
    }
)

function chooseData(metric, movieClean) {
    
    const thisData = movieClean.sort((a, b) => b[metric] - a[metric]).filter((d, i) => i < 15);

    return thisData;
}