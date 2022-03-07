<?php

//init
$arr = [];

//dinamyc adding
$arr[] = 'test';
$arr[] = 'rest';
$arr[] = 2;

//adding by key
$arr[3] = 5;
$arr[] = 6;

//changed
$arr[0] = 'changed';

//init array with data
//нет фиксированной длинны
$arr2 = [1,2,3,4,5];
$arr2[] = 6;

//если нужна фиксированная длинна но лучше не использовать
$array = new SplFixedArray(3);
$array[0] = 1;
$array[1] = 2;
$array[2] = 3;
// $array[3] = 4; // RuntimeException

//associate array
$arrmarr = [
  "key" => 22,
  "pey" => 33,
  "ley" => "String"
];

var_dump($arrmarr["ley"]);

