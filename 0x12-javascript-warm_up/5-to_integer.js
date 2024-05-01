#!/usr/bin/node

function isNumber (value) {
  return parseInt(value);
}

if (isNaN(isNumber(process.argv[2]))) {
  console.log('Not a number');
} else {
  console.log('My number : ', parseInt(process.argv[2]));
}
