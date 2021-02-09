/**
 * @param {string} s
 * @return {number[][]}
 */
var largeGroupPositions = function(S) {
    var index = [0, 0];
    var res = [];
    for (var i=0; i<S.length; i++) {
        if (i===S.length-1 || S[i] !== S[i+1]) {
            index[1] = i;
            if (index[1] - index[0] >= 2) {
                res.push(index);
            }
            index = [i+1, i+1];
        }
    }
    return res;
};