import { 
  countColumnTypes, 
  type, 
  filterData,
} from './utilities.js';
import { 
  prepareFirstBarChartData, 
  prepareSecondBarChartData,
  prepareThirdBarChartData,
  prepareForthBarChartData,
  preparePSPlatformBarChartDataGlobal,
} from './chartData.js';
import { 
    setupFirstCanvas, 
    setupSecondCanvas,
    setupThirdCanvas,
    setupForthCanvas,
} from './MidCanvas.js';
import { 
    setupPSCanvas,
    // setupPSCanvasPie,
} from './FinalCanvas.js';


function ready(videoGameData) {

  const videoGameClean = filterData(videoGameData);
  const firstBarChartData = prepareFirstBarChartData(videoGameClean).sort(
      (a, b) => {
          return d3.descending(a.Global_Sales, b.Global_Sales);
      }
  );
  const secondBarChartData = prepareSecondBarChartData(videoGameClean).sort(
      (a, b) => {
          return d3.descending(a.Global_Sales, b.Global_Sales);
      }
  );
  const filteredSecondBarChartData = secondBarChartData.filter(d => d.Global_Sales >= 100);
  const thirdBarChartData = prepareThirdBarChartData(videoGameClean).sort(
      (a, b) => {
          return d3.descending(a.Global_Sales, b.Global_Sales);
      }
  );
  const forthBarChartData = prepareForthBarChartData(videoGameClean).sort(
      (a, b) => {
          return d3.descending(a.Global_Sales, b.Global_Sales);
      }
  );

  const PSBarChartData = preparePSPlatformBarChartDataGlobal(videoGameClean).sort(
    (a, b) => {
        return d3.descending(a.Global_Sales, b.Global_Sales);
    }
);


  // console.log(forthBarChartData.a);

//   console.log(firstBarChartData);
  setupFirstCanvas(firstBarChartData);
  setupSecondCanvas(filteredSecondBarChartData);
  setupThirdCanvas(thirdBarChartData);
  setupForthCanvas(forthBarChartData);

  setupPSCanvas(PSBarChartData);
  // setupPSCanvasPie(PSBarChartData);
}

// Load the Data
d3.csv('./data/Video_Games_Sales_as_at_22_Dec_2016.csv', type).then(
  result => {

      // console.log(result);
      ready(result)

      // countColumnTypes(result, "Genre");          // 13
      // countColumnTypes(result, "Platform");       // 31
    // countColumnTypes(result, "Platform");       // 31
    
  }
)


