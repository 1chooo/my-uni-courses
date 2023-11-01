/*
 * This code is to do the test for get
 * data from local and internet with 
 * the format .csv and .json.
 */

// get csv file
// d3.csv('./data/harry_potter.csv').then(
//     res => {
//         console.log('Local CSV:', res);
//         // use typeof() then we can check the type 
//         console.log(typeof(res));   // type: object
//     }
// );

// get json file
// d3.json('data/harry_potter.json').then(
//     res => {
//         console.log('Local json:', res);
//     }
// );

// get local multi-files
// const potter = d3.csv('data/harry_potter.csv'); 
// const rings = d3.csv('data/lord_of_the_rings.csv');

// Promise.all([potter, rings]).then( 
//     res =>{
//         console.log('potter:',res[0]);
//         console.log('rigns:',res[1]); 
//     }
// );

// get internet multi-files
// const potter = d3.csv('https://raw.githubusercontent.com/ryanchung403/dataset/main/harry_potter.csv'); 
// const rings = d3.csv('https://raw.githubusercontent.com/ryanchung403/dataset/main/lord_of_the_rings.csv');

// Promise.all([potter, rings]).then( 
//     res =>{
//         console.log('potter:',res[0]);
//         console.log('rigns:',res[1]); 
//     }
// );

// merge local multi-files
// const potter = d3.csv('data/harry_potter.csv'); 
// const rings = d3.csv('data/lord_of_the_rings.csv');
// Promise.all([potter, rings]).then( 
//     res =>{
//         console.log('Multiple Request:',res); 
//         console.log('Concat:',[...res[0],...res[1]]); 
//         //console.log('potter:',res[0]); 
//         //console.log('rigns:',res[1]);
//     } 
// );


// merge internet multi-files
// const potter = d3.csv('https://raw.githubusercontent.com/ryanchung403/dataset/main/harry_potter.csv'); 
// const rings = d3.csv('https://raw.githubusercontent.com/ryanchung403/dataset/main/lord_of_the_rings.csv');
// Promise.all([potter, rings]).then( 
//     res =>{
//         console.log('Multiple Request:',res); 
//         console.log('Concat:',[...res[0],...res[1]]); 
//         //console.log('potter:',res[0]); 
//         //console.log('rigns:',res[1]);
//     } 
// );

// get internet json
// this need the api key.
// d3.json('https://api.themoviedb.org/3/search/movie?api_key=YourKeyHere&language=zh-TW&query=%E7%80%91%E5%B8%83').then(
//     res =>{
//         console.log('API json:',res);
//     } 
// );

// get internet json
d3.json('https://api.chucknorris.io/jokes/search?query=dog').then(
    res =>{
        console.log('API json:',res);
        console.log(res.result);
        console.log(res.result[0].value);
    } 
);