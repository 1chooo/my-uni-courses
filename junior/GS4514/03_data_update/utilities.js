export function click() {
    const thisFruitList = friends[this.dataset.name];
    update(thisFruitList);
}

export function update(data) {

    thisSVG.selectAll('text')
           .data(data, d => d)
           .join(
               enter => {
                   enter.append('text')
                        .text(d => d)
                        .attr('x', -100)
                        .attr('y', (d, i) => 50 + i * 30)
                        .style('fill', 'green')
                        .transition()
                        .attr('x', 30)
               },
               update => {
                   update.transition()
                         .style('fill', 'red')
                         .attr('y', (d, i) => 50 + i * 30)
               },
               exit => {
                   exit.transition()
                       .attr('x', 150)
                       .style('fill', 'yellow')
                       .remove()
               }
           );
}