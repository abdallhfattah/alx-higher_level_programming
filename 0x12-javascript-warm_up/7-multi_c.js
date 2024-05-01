#!/usr/bin/node

if (process.argv[2] === undefined || isNaN(parseInt(process.argv[2]))) {
  console.log('Missing number of occurrences');
} else {
  for (let index = 0; index < parseInt(process.argv[2]); index++) {
    console.log('C is fun');
  }
}
