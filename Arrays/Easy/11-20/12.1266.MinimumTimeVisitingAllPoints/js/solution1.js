/**
 * @param {number[][]} points
 * @return {number}
 */
var minTimeToVisitAllPoints = function(points) {
    let ans = 0;

    for (let i = 1; i < points.length; i++) {
        let current = points[i];
        let prev = points[i - 1];

        ans += Math.max(Math.abs(current[0] - prev[0]), Math.abs(current[1] - prev[1]));
    }

    return ans;
};