export function divideintofive(videoGameClean){
    // 這個function會把資料分成以五年為單位做切割
    // console.log(videoGameClean);
    const extnets = d3.extent(videoGameClean, d=>d.Year_of_Release);
    const Ymin = extnets[0];
    const Ymax = extnets[1];
    // 下面存放每五年會有的不同資料
    const groupdatainfive = [];
    for (let x = Ymin; x < Ymax; x += 5){
        let obj = {start:x, end:x+4, content:[]};
        groupdatainfive.push(obj);
    }
    for(let x = 0; x < videoGameClean.length; x++){
        let year = videoGameClean[x].Year_of_Release;
        for (let j = 0;j < groupdatainfive.length; j++){
            // console.log(groupdatainfive[j].start >= year && year <= groupdatainfive[j].end);
            if (year >= groupdatainfive[j].start && year <= groupdatainfive[j].end){
                groupdatainfive[j].content.push(videoGameClean[x]);
            }
        }
    }
    // consequence
    // console.log(groupdatainfive);
    return groupdatainfive;
}

export function addSelect(Datas){
    // 增加指定的select到body
    // 若有需要可以改成到特定元素
    // 參數為 array
    let FirstCanvasSelect = document.createElement('select');
    FirstCanvasSelect.id = "selection";
    for (let i = 0; i < Datas.length; i++){
        let option = document.createElement("option");
        option.text = `${Datas[i].start} - ${Datas[i].end}`;
        option.value = i;
        FirstCanvasSelect.add(option);
    }

    return FirstCanvasSelect;
}
export function addSelectGenre(genres){
    let FirstCanvasSelect = document.createElement('select');
    FirstCanvasSelect.id = "selection";
    for (let i = 0; i < genres.length; i++){
        let option = document.createElement("option");
        option.text = `${genres[i]}`;
        option.value = i;
        FirstCanvasSelect.add(option);
    }

    return FirstCanvasSelect;   
}