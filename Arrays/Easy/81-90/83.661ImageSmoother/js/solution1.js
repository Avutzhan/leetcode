/**
 * @param {number[][]} M
 * @return {number[][]}
 */
var imageSmoother = function(M) {
    const dirs = [[-1,0],[-1,-1],[1,0],[1,1],[0,1],[0,-1],[1,-1],[-1,1]]
    const sliceM = [...new Array(M.length)].map(() => [...new Array(M[0].length)].fill(0))

    for(let i = 0; i < M.length; i ++){
        for(let j = 0; j < M[i].length; j ++){
            let sum = M[i][j]
            let count = 1

            for(let k = 0; k < dirs.length; k ++){
                let newI = i + dirs[k][0]
                let newJ = j + dirs[k][1]

                if(newI >= 0 && newI < M.length && newJ >= 0 && newJ < M[i].length){
                    sum += M[newI][newJ];
                    count ++
                }
            }

            sliceM[i][j] = Math.floor(sum / count)
        }
    }

    return sliceM
};