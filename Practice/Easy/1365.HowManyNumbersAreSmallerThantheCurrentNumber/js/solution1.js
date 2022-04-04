/**
 * @param {number[]} nums
 * @return {number[]}
 * Трассировка
 */

var smallerNumbersThanCurrent = function(nums) {
    console.log('input       ', nums);

    const sorted = [...nums].sort((a, b) => a - b); //т меньшего к большему

    console.log('sorted      ', sorted);

    return nums.map(function(num) {
        console.log('map num ', num);
        console.log('indexOf num ', sorted.indexOf(num));
        return sorted.indexOf(num);

    });

    //пробегаемся по входящему массиву и находим индексы элементов в сортированном массиве
    //и добавляем в новый массив
};

console.log(smallerNumbersThanCurrent([8,1,2,2,3]));

/**
 * @param {number[]} nums
 * @return {number[]}
 * Трассировка
 */
var smallerNumbersThanCurrent = function(nums) {
    console.log('input       ', nums);

    const sorted = [...nums].sort((a, b) => b - a); //от большего к меньшему
    console.log('sorted array', sorted);


    const map = new Map(sorted.map(function(num, index) {
        console.log('index => val', index, num );
        console.log('nums.length ', nums.length - 1 - index);
        return [num, nums.length - index - 1]
    }));

    // вычисляем сколько чисел меньше текущего элемента (числа)
    // так как входящий массив отсортирован от большего к меньшему
    // мы сравниваем индексы отсортированного массива с индексами не отсортированного
    // Map содержит пары ключ-значение и сохраняет порядок вставки
    // [num, nums.length - index - 1] передаем Мапу массив в котором массивы ключ значение

    // num = в нашем случае ключ это каждый элемент отсортированного массива

    // nums.length - index - 1 = а значение это индес текущего элемента изза отсортированного массива минус
    // количество элементов в не отсортированном массиве - 1

    //потому что начало любого массива 0.Problem
    // и в джс всегда количество элементов внутри цикла будет больше чем 1 это изза условий цикла
    // изза того что в условии есть < то оно будет всегда на 1 больше элементов итерировать можно сделать <=

    console.log('counted     ', map);

    const res = nums.map(num => map.get(num));

    console.log('res         ', res);

    return res;
};

console.log(smallerNumbersThanCurrent([8,1,2,2,3]));
