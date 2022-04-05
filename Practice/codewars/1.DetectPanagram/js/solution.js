function format(string) {
  let res = "";

  string.toLowerCase() //to lowercase
        .replace(/\s/g, "") //delete whitespaces
        .split("") // make string array
        .forEach(ch => { //foreach i in array
    if (res.indexOf(ch) === -1) {
      res += ch
    }
  })

  return res
}

function isPangram(string){
  let alphabet = "abcdefghijklmnopqrstuvwxyz";
  let counter = 0;

  format(string).split("").forEach(ch => {
    if (alphabet.indexOf(ch) !== -1) {
      counter++;
    }
  });

  if (counter >= alphabet.length) {
    return true;
  } else {
    return false;
  }
}

