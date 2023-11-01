// Group countries by continent
const continents = d3.nest()
    .key(d => d.Continent)
    .rollup(values => values.length)
    .entries(result);

// Log the count of countries by continent
continents.forEach(continent => {
    console.log(`${continent.key}: ${continent.value}`);
});


function getContinent(countryCode) {

    const asia = ['AFG', 'BHR', 'BGD', 'BRN', 'BTN', 'KHM', 'CHN', 'HKG', 'IND', 'IDN', 'IRN', 'IRQ', 'ISR', 'JPN', 'JOR', 'KAZ', 'KWT', 'KGZ', 'LAO', 'LBN', 'MAC', 'MYS', 'MDV', 'MNG', 'MMR', 'NPL', 'PRK', 'OMN', 'PAK', 'PHI', 'QAT', 'SAU', 'SGP', 'KOR', 'LKA', 'SYR', 'TJK', 'THA', 'TLS', 'TUR', 'TKM', 'ARE', 'UZB', 'VNM', 'YEM'];
    const africa = ['DZA', 'AGO', 'BEN', 'BWA', 'BFA', 'BDI', 'CPV', 'CMR', 'CAF', 'TCD', 'COM', 'COG', 'COD', 'CIV', 'DJI', 'EGY', 'GNQ', 'ERI', 'ETH', 'GAB', 'GMB', 'GHA', 'GIN', 'GNB', 'KEN', 'LSO', 'LBR', 'LBY', 'MDG', 'MWI', 'MLI', 'MRT', 'MUS', 'MYT', 'MAR', 'MOZ', 'NAM', 'NER', 'NGA', 'STP', 'REU', 'RWA', 'SHN', 'STP', 'SEN', 'SYC', 'SLE', 'SOM', 'ZAF', 'SSD', 'SDN', 'SWZ', 'TZA', 'TGO', 'TUN', 'UGA', 'ESH', 'ZMB', 'ZWE'];
    const europe = ['ALB', 'AND', 'ARM', 'AUT', 'AZE', 'BLR', 'BEL', 'BIH', 'BGR', 'HRV', 'CYP', 'CZE', 'DEN', 'EST', 'FIN', 'FRA', 'GEO', 'DEU', 'GIB', 'GRC', 'HUN', 'ISL', 'IRL', 'ITA', 'KOS', 'LVA', 'LIE', 'LTU', 'LUX', 'MKD', 'MLT', 'MDA', 'MCO', 'MNE', 'NLD', 'NOR', 'POL', 'PRT', 'ROU', 'RUS', 'SMR', 'SRB', 'SVK', 'SVN', 'ESP', 'SWE', 'CHE', 'UKR', 'GBR', 'VAT'];
    const oceania = ['ASM', 'AUS', 'COK', 'FJI', 'PYF', 'GUM', 'KIR', 'MHL', 'FSM', 'NRU', 'NZL', 'NCL', 'NIU', 'NFK', 'MNP', 'PLW', 'PNG', 'WSM', 'SLB', 'TKL', 'TON', 'TUV', 'VUT', 'WLF'];
    const americas = ['ANT', 'ARG', 'ABW', 'BHS', 'BRB', 'BLZ', 'BMU', 'BOL', 'BRA', 'CAN', 'CAY', 'CHI', 'COL', 'CRC', 'CUB', 'DMA', 'DOM', 'ECU', 'ESA', 'GRN', 'GUA', 'GUY', 'HAI', 'HON', 'JAM', 'MEX', 'MNT', 'NCA', 'PAN', 'PAR', 'PER', 'PUR', 'SKN', 'LCA', 'VIN', 'SUR', 'TRI', 'USA', 'ISV', 'URY', 'VEN'];

    if (asia.includes(countryCode)) {
        return "Asia";
    } else if (africa.includes(countryCode)) {
        return "Africa";
    } else if (europe.includes(countryCode)) {
        return "Europe";
    } else if (oceania.includes(countryCode)) {
        return "Oceanin";
    } else if (americas.includes(countryCode)) {
        return "Americas";
    } else {
        return "Other";
    }
}

// 將數據按照 NOC 屬於的洲進行分組
const countriesByContinent = data.reduce((acc, curr) => {

    const continent = getContinent(curr.NOC);
    if (!acc[continent]) {
        acc[continent] = [];
    }
    acc[continent].push(curr);
    return acc;
}, {});



function setupCanvas(barChartData) {

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

    // To find the element in the html <div class=bar-chart-container>.
    const this_svg = d3.select('.bar-chart-container')
        .append('svg')
        .attr('width', svg_width)
        .attr('height', svg_height)
        .append('g')
        .attr('transform', `translate(${chart_margin.left}, ${chart_margin.top})`);

    // scale
    // V1.d3.extent find the max & min in revenue
    const xExtent = d3.extent(barChartData, d => d.Global_Sales);
    const xScale_v1 = d3.scaleLinear()
        .domain(xExtent)
        .range([0, chart_width]); //V2.0 ~ max
    const xMax = d3.max(barChartData, d => d.Global_Sales);
    const xScale_v2 = d3.scaleLinear()
        .domain([0, xMax])
        .range([0, chart_width]); //V3.Short writing for v2
    const xScale_v3 = d3.scaleLinear([0, xMax], [0, chart_width]);
    //垂直空間的分配 - 平均分布給各種類
    const yScale = d3.scaleBand()
        .domain(barChartData.map(d => d.Genre))
        .rangeRound([0, chart_height])
        .paddingInner(0.25);

    //Draw bars
    const bars = this_svg.selectAll('.bar')
        .data(barChartData)
        .enter()
        .append('rect')
        .attr('class', 'bar')
        .attr('x', 0).attr('y', d => yScale(d.Genre))
        .attr('width', d => xScale_v3(d.revenue))
        .attr('height', yScale.bandwidth())
        .style('fill', 'dodgerblue')

    //Draw header
    const header = this_svg.append('g')
        .attr('class', 'bar-header')
        .attr('transform', `translate(0,${-chart_margin.top / 2})`)
        .append('text');
    header.append('tspan')
        .text('Total revenue by genre in $US');
    header.append('tspan')
        .text('Years:2000-2009')
        .attr('x', 0)
        .attr('y', 20)
        .style('font-size', '0.8em')
        .style('fill', '#555');

    // tickSizeInner : the length of the tick lines
    // tickSizeOuter : the length of the square ends of the domain path 
    const xAxis = d3.axisTop(xScale_v3)
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

function formatTicks(d) {
    return d3.format('~s')(d).
        replace('M', 'mil')
        .replace('G', 'bil')
        .replace('T', 'tri')
}


const xScale_v1 = d3.scaleLinear()
        .domain(xExtent)
        .range([0, chart_width]); //V2.0 ~ max
const xScale_v2 = d3.scaleLinear()
    .domain([0, xMax])
    .range([0, chart_width]); //V3.Short writing for v2

function countColumnTypes(data, columnName) {

    const types = d3.group(data, d => d[columnName]);
    console.log(`${columnName} types: ${types.size}`);
    types.forEach((value, key) => {
        console.log(`- ${key}`);
    });
}

function formatTicks(d){ 
    
    return d3.format('~s')(d) 
        .replace('M','mil') 
        .replace('G','bil') 
        .replace('T','tri')
}

const parseNA = string => (string === '' ? undefined : string);
const parseDate = string => d3.timeParse('%Y-%m-%d')(string);

function type(d) {

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
    }
}

function filterSecondData(videoGameData) {

    console.log(typeof (videoGameData))       // object

    return videoGameData.filter(
        d => {
            return (
                // we want to observe the data in ten years 

                d.Global_Sales > 0 &&
                d.Platform &&
                d.Name
            );
        }
    );
}

function prepareFirstBarChartData(videoGameData) {

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


function setupFirstCanvas(barChartData) {

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
        .text('Total Global_Sales by Genre ');
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