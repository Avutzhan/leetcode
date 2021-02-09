/**
 * @param {number[]} bits
 * @return {boolean}
 */
var isOneBitCharacter = function(bits) {
    var isMidCharacter = false
    for(let i = 0; i < bits.length - 1; i++){
        isMidCharacter = (bits[i] === 1 && !isMidCharacter)
    }
    return !isMidCharacter
};