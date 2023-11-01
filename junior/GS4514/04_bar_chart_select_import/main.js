import { 
  type,
  ready
} from './utilities.js';

//Load Data
d3.csv('./data/movies.csv', type).then(
  result => {
      ready(result)
  }
)