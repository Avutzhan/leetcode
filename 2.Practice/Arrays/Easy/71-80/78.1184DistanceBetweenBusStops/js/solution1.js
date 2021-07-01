/**
 * @param {number[]} distance
 * @param {number} start
 * @param {number} destination
 * @return {number}
 */
var distanceBetweenBusStops = function(distance, start, destination) {
    if (start > destination) {
        let temp = destination;
        destination = start;
        start = temp;
    }

    const front = distance.slice(start, destination).reduce((acc, curr) => acc + curr, 0);
    const back = [...distance.slice(destination), ...distance.slice(0, start)].reduce((acc, curr) => acc + curr, 0);

    return Math.min.call(null, front, back);
};