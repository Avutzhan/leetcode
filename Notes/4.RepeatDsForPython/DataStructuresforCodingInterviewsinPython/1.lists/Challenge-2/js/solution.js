let merge = (arr1, arr2) => {
  let index1 = 0;
  let index2 = 0;
  let index_res = 0;
  let res = [];

  for (let i = 0; i < arr1.length + arr2.length; i++) {
    res.push(0);
  }

  while ((index1 < arr1.length) && (index2 < arr2.length)) {
    if (arr1[index1] < arr2[index2]) {
      res[index_res] = arr1[index1];
      index1 ++;
      index_res ++;
    } else {
      res[index_res] = arr2[index2];
      index2 ++;
      index_res ++;
    }
  }

  while(index1 < arr1.length) {
    res[index_res] = arr1[index1];
    index1 ++;
    index_res ++;
  }

  while(index2 < arr2.length) {
    res[index_res] = arr2[index2];
    index2 ++;
    index_res ++;
  }

  return res;
}

result =  merge([1, 3, 4, 5],[2, 6, 7, 8]);
expected = [1, 2, 3, 4, 5, 6, 7, 8];

let equalArrays = (a,b) => {
  if (a.length != b.length) return false;
  for(var i = 0; i < a.length; i++) {
    if (a[i] !== b[i]) return false;
  }
  return true;
}

if (equalArrays(result, expected)) {
  console.log("Success");
} else {
  console.log("Failure");
}

