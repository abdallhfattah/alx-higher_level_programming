#!/usr/bin/node

function add (a, b) {
  if (a === undefined || b === undefined) {
    return undefined;
  } else {
    return parseInt(a) + parseInt(b);
  }
}
console.log(add(process.argv[2], process.argv[3]));
