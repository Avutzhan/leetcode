<?php
//получаем отсортированный массив и значение
//если это значение есть в массиве возвращаем индекс
//если нет то null
function binarySearch($needle, $array, $start, $end) {
    //следим в какой части массива проводится поиск
    //начало и конец
    //создаем петлю пока low меньше или равно high выполняем код
    if ($start > $end) {
        return null;
    }

    while ($start <= $end) {
        //середина массива если значение не четно то округляем в меньшую сторону
        $middle = floor(($start + $end) / 2);

        //если в массиве элемент под этим индексом равен искомому значению то возвращаем этот индекс
        if ($array[$middle] == $needle) {
            return $middle;
        }

        //если значение под этим индексов больше искомого значения
        //то сдвигаем конец на середину если меньше то сдвигаем начало на середину
        if ($array[$middle] > $needle) {
            $end = $middle - 1;
        } else {
            $start = $middle + 1;
        }
    }
}

$array = [1, 3, 5, 7, 9];
echo binarySearch(3, $array, 0, count($array)) . "\n";
echo binarySearch(-1, $array, 0, count($array)) . "\n";