/**
 * @param {number[]} nums
 * @return {number[]}
 */
var frequencySort = function(A) {
    //создать базу данных
    let m = new Map();
    // console.log('init map', m);

    //посчитать частоту появления цифр и вставить данные в бд в виде ключ => значение
    A.forEach(x => m.set(x, 1 + (m.get(x) || 0)));
    // console.log('A', m);
    // console.log('map', m);

    //вернуть данные в виде массива [ключ, значение] и отсортировать массивы
    // console.log('Pre P', m.entries());
    // Если несколько значений имеют одинаковую частоту,
    // отсортируйте их в порядке убывания.
    let P = [...m.entries()].sort(function(a, b) {
        // console.log('a', a);
        // console.log('a1', a[1]);
        // console.log('b', b);
        // console.log('b1', b[1]);
        return a[1] == b[1] ? b[0] - a[0] : a[1] - b[1]
    });

    //создать массивы ключ/value = значние/frequency
    console.log('P', P);
    let preflat = P.map(function([x, cnt]) {
        console.log('x', x);
        console.log('cnt', cnt);
        return Array(cnt).fill(x)
    });

    console.log('preflat', preflat)
    return _.flatten(P.map(([x, cnt]) => Array(cnt).fill(x)));
};