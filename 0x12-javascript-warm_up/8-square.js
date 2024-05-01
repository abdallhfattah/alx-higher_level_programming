#!/usr/bin/node

if (process.argv[2] === undefined || isNaN(parseInt(process.argv[2]))) {
  console.log('Missing size');
} else {
  for (let index = 0; index < parseInt(process.argv[2]); index++) {
    for (let i = 0; i < parseInt(process.argv[2]); i++) {
      process.stdout.write('X');
    }
    console.log();
  }
}
