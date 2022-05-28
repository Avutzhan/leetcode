let remove_even = (arr) => {
  let res = [];
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] % 2 != 0) {
      res.push(arr[i]);
    }
  }
  return res;
}

result =  remove_even([1, 2, 3, 4, 5, 6]);
expected = [1, 3, 5];

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

