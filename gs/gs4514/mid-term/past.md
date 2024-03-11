原先想說之後要留學，所以找了很多靈學相關的資料，不過原始資料偏少，於是開始以多年份、種類多的方向去查找


```JS
function type(d) {

    return {
        Age: +d.Age,
        City: d.City.trim(),
        // Event: d.Event.trim(),
        // Games: d.Games.trim(),
        Medal: d.Medal.trim(),
        NOC: d.NOC.trim(),
        Name: d.Name.trim(),
        // Season: d.Season.trim(),
        Sex: d.Sex.trim(),
        Sport: d.Sport.trim(),
        Team: d.Team.trim(),
        Year: +d.Year,
    }
}

function countColumnTypes(data, columnName) {
    const types = d3.group(data, d => d[columnName]);
    console.log(`${columnName} types: ${types.size}`);
    types.forEach((value, key) => {
        console.log(`- ${key}`);
    });
}

// Load the Data
d3.csv('./data/Athletes_summer_games.csv', type).then(
    result => {
        // delete the first column
        result.forEach(obj => {
            delete obj[""];
        });

        console.log(result);

        // countColumnTypes(result, "Medal");      // 4
        countColumnTypes(result, "Sport");      // 70
        // countColumnTypes(result, "Team");       // 1169
        // countColumnTypes(result, "Year");       // 30
        // countColumnTypes(result, "Games");       // 30
        // countColumnTypes(result, "Event");       // 30
        countColumnTypes(result, "City");       // 23
    }
)
```

## Planning

1. find the data which are highly depended on area.
2. more types of data.
3. large numbers of data.

可以請問你，如果我想要找到一份資料集，是關於各年度，申請美國百大大學的人數、錄取率、申請人地區、成績要求等⋯⋯請問我有哪些管道可以去查找


https://data.gov.tw
https://catalog.data.gov/

1. 比數多一點
2. 要有分類

* [US Schools Dataset](https://www.kaggle.com/datasets/andrewmvd/us-schools-dataset?select=Public_Schools.csv)
* [University of California 1994-2016 Admission Stats](https://www.kaggle.com/datasets/oscarm524/university-of-california-19942016-admission-stats?select=HS_by_Year_data.csv)
* [University of California Applicants Details](https://www.kaggle.com/datasets/rainbowpiss/university-of-california-applicants-details)
* [US graduate schools's admission parameters](https://www.kaggle.com/datasets/musfiq47/us-graduate-schoolss-admission-parameters)
* [U.S. News and World Report’s College Data](https://www.kaggle.com/datasets/flyingwombat/us-news-and-world-reports-college-data)
* [Engineering Graduate Salary Prediction](https://www.kaggle.com/datasets/manishkc06/engineering-graduate-salary-prediction)


### With more years
* [Global Terrorism Database](https://www.kaggle.com/datasets/START-UMD/gtd)
* [Olympics 124 years Dataset(till 2020)](https://www.kaggle.com/datasets/nitishsharma01/olympics-124-years-datasettill-2020)