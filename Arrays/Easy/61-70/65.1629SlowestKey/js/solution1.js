/**
 * @param {number[]} releaseTimes
 * @param {string} keysPressed
 * @return {character}
 */
let slowestKey = (releaseTimes, keysPressed) => {
    let k = keysPressed[0], t = releaseTimes[0];

    for (let i = 1; i < keysPressed.length; i++) {
        let time = releaseTimes[i] - releaseTimes[i-1];

        if (time > t || (time == t && keysPressed[i] > k)) {
            t = time;
            k = keysPressed[i];
        }

    }

    return k;
};