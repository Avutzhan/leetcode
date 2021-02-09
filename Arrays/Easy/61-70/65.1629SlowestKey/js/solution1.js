/**
 * @param {number[]} releaseTimes
 * @param {string} keysPressed
 * @return {character}
 */
let slowestKey = (A, keys, best = 0, ans = '0') => {
    keys.split('').forEach((key, i) => {

        let time = 0 < i ? A[i] - A[i - 1] : A[i];

        if (best < time || (best == time && ans.localeCompare(key) < 0))
            best = time,
                ans = key;
    });

    return ans;
};