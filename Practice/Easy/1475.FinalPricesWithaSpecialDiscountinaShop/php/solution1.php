<?php

class Solution {

    /**
     * @param Integer[] $prices
     * @return Integer[]
     */
    function finalPrices($prices) {
        for($i=0;$i<count($prices);$i++){
            $j=$i+1;
            while($j<count($prices)){
                if($prices[$j]<=$prices[$i]){
                    $prices[$i]=$prices[$i]-$prices[$j];
                    break;
                }
                $j++;
            }
        }
        return $prices;
    }
}