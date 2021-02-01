/**
 * @param {number[]} prices
 * @return {number[]}
 */
var finalPrices = function(prices) {
    for(let i=0;i<prices.length;i++){
        let j=i+1;
        while(j<prices.length){
            if(prices[j]<=prices[i]){
                prices[i]=prices[i]-prices[j];
                break;
            }
            j++;
        }
    }
    return prices;
};