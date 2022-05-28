let remove_even = (arr) => {
  let res = [];
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] % 2 != 0) {
      res.push(arr[i]);
    }
  }
  return res;
}

