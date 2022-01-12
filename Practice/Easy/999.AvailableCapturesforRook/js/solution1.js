/**
 * @param {character[][]} board
 * @return {number}
 */
var canCapture = function(board, i, j) {
    let captures = 0, dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];

    for (let dir of dirs) {
        let r = i + dir[0], c = j + dir[1];

        while (r >= 0 && r < 8 && c >= 0 && c < 8) {
            if (board[r][c] === 'p') { captures++; }
            if (board[r][c] !== '.') { break; }

            r += dir[0];
            c += dir[1];
        }
    }

    return captures
};

const numRookCaptures = board => {
    for (let i = 0; i < 8; i++) {
        for (let j = 0; j < 8; j++) {
            if (board[i][j] === 'R') {
                return canCapture(board, i, j);
            }
        }
    }
};