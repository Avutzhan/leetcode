/**
 * @param {number[][]} coordinates
 * @return {boolean}
 */
var checkStraightLine = function(coords) {
    let n = coords.length;

    for (let i = 0; i < n - 2; i++) {
        let x1 = coords[i][0] * coords[i + 1][1] + coords[i + 1][0] * coords[i + 2][1] + coords[i + 2][0] * coords[i][1];
        let x2 = coords[i][1] * coords[i + 1][0] + coords[i + 1][1] * coords[i + 2][0] + coords[i + 2][1] * coords[i][0];
        let x3 = x1 - x2;
        let area = Math.abs(1/2 * x3);

        if (area > 0) {
            return false;
        }
    }

    return true;
};