let find_sum = (arr, k) => {
  for (let i = 0; i < arr.length; i++) {
    for (let j = 0; j < arr.length; j++) {
      if (arr[i] + arr[j] == k && i != j) {
        return [arr[i], arr[j]];
      }
    }
  }
}

result =  find_sum([1, 21, 3, 14, 5, 60, 7, 6],81);
expected = [21, 60];

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

