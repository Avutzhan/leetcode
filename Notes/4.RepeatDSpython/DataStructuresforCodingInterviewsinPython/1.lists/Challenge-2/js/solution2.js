let merge = (arr1, arr2) => {
  let index1 = 0;
  let index2 = 0;

  while (index1 < arr1.length && index2 < arr2.length) {
    if (arr1[index1] > arr2[index2]) {
      arr1.splice(index1, 0, arr2[index2]);
      index1++;
      index2++;
    } else {
      index1++;
    }
  }

  if (index2 < arr2.length) {
    arr1.push(...arr2.splice(index2));
  }

  return arr1;
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

