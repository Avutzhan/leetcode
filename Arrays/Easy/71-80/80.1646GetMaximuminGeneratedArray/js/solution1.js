/**
 * @param {number} n
 * @return {number}
 */
var getMaximumGenerated = function(n) {
    if(n<2){ return n; }

    let arr = new Array(n+1);
    arr[0]=0; arr[1]=1;

    for(let ind=2; ind<=n; ++ind){
        let i = Math.floor(ind/2);
        if( ind % 2 == 0){
            arr[ind] = arr[i];
        }
        else{
            arr[ind] = arr[i] + arr[i+1];
        }
    }

    return Math.max(...arr);
};