#!/usr/bin/node
function fact (n) {
  if (n < 0) {
    return (-1);
  }
  if (n === 0 || isNaN(n)) {
    return 1;
  }

  return n * fact(n - 1);
}

console.log(fact(Number(process.argv[2])));
