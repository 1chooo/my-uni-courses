import {
    setupCanvas
} from './setCanvas.js'

// Data utilities
// '===' is the judgement of the data type.
// if we meet the data type which is 'NA', 
// we change it into the 'undefined',
// or we keep the original string.
const parseNA = string => (string === 'NA' ? undefined : string);
// Solving the format of the date.
const parseDate = string => d3.timeParse('%Y-%m-%d')(string);


export function type(d) {
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
export function filterData(data) {
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

export function prepareBarChartData(data) {
  console.log(data);
  const dataMap = d3.rollup(
      data,
      v => d3.sum(v, leaf => leaf.revenue), // Sum up the revenue.
      d => d.genre // categorize the movie with groupby
  );
  const dataArray = Array.from(dataMap, d => ({ genre: d[0], revenue: d[1] }));
  return dataArray;
}

export function formatTicks(d) {
  return d3.format('~s')(d).
      replace('M', 'mil')
      .replace('G', 'bil')
      .replace('T', 'tri')
}

export function chooseData(metric, movieClean) {

    const thisData = movieClean.sort((a, b) => b[metric] - a[metric]).filter((d, i) => i < 15);

    return thisData;
}

export function ready(movies) {
    const movieClean = filterData(movies);
    //Get Top 15 revenue movies
    const revenueData = chooseData("revenue", movieClean); 
    setupCanvas(revenueData, movieClean);
}