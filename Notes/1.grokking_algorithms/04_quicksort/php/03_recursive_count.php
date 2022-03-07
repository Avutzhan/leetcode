<?php
//посчитайте сколько элементов в массиве
function recursiveCount($list) {
    //base case если массив пустой вернуть 0
    if (count($list) === 0) {
        return 0;
    }
    //если не пустой то 1 добавляем к рекурсивному вызову функции с каждым разом удаляя первый элемент
    //и каждый раз она будет возвращать 1 пока есть элементы в массиве
    return 1 + recursiveCount(array_splice($list, 1));
}

echo count([0, 1, 2, 3, 4, 5]); // 6
